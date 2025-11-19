import json, sys, traceback

nb_path = r"c:\Users\fabio\OneDrive - GUSCanada\VSCODEGIT\MLUNFTERM4\Week2Exercises\week02_ml_assignment.ipynb"
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

errors = []
for idx, cell in enumerate(nb.get('cells', []), start=1):
    if cell.get('cell_type') == 'code':
        src = ''.join(cell.get('source', []))
        try:
            compile(src, f'<cell {idx}>', 'exec')
        except Exception as e:
            errors.append((idx, str(e)))

if errors:
    print('Found syntax errors in the following code cells:')
    for idx, err in errors:
        print(f'  Cell {idx}: {err}')
    sys.exit(2)
else:
    print('No syntax errors detected in code cells.')
