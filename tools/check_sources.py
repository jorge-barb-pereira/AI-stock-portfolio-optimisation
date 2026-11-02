"""Inventory the historical source/data without running portfolio searches."""
from pathlib import Path
import ast,csv,hashlib,json
from datetime import date
root=Path(__file__).resolve().parents[1]
ast.parse((root/'otimizador.py').read_text(encoding='utf-8'))
manifest=json.loads((root/'docs/source-manifest.json').read_text(encoding='utf-8'))
notebook=root/manifest['published']
assert hashlib.sha256(notebook.read_bytes()).hexdigest()==manifest['published_sha256']
nb=json.loads(notebook.read_text(encoding='utf-8'))
for cell in nb['cells']:
    if cell['cell_type']=='code':
        assert not cell['outputs'] and cell['execution_count'] is None
        ast.parse(''.join(cell['source']))
files=sorted((root/'archive').glob('*.csv'))
assert len(files)==100, f'Expected 100 original stock files, got {len(files)}'
calendar=None;items=[]
for path in files:
    with path.open(encoding='utf-8',newline='') as stream:
        reader=csv.DictReader(stream)
        assert {'Date','Close'}<=set(reader.fieldnames or []),path.name
        dates={date.fromisoformat(row['Date']) for row in reader}
    assert dates,path.name
    calendar=dates if calendar is None else calendar & dates
    items.append(dict(asset=path.stem,dates=len(dates),first=min(dates).isoformat(),last=max(dates).isoformat()))
print(json.dumps(dict(stock_files=len(files),common_dates=len(calendar),
                      earliest=min(x['first'] for x in items),latest=max(x['last'] for x in items),
                      scope='Syntax and calendar inventory only; not financial or optimisation validation.'),indent=2))
