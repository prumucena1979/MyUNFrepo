import json

# Purpose:
# This small helper script loads a Jupyter notebook file (JSON format) and prints the
# source code of each code cell. It is intended to help debug malformed notebooks
# by showing the exact raw code contained in each code cell (joined into a single
# string) along with the cell number. This is useful when syntax-checking cells or
# when a notebook file contains broken/fragmented cell contents.

# Path to the notebook file. Update if your notebook is in a different location.
p = r'c:\Users\fabio\OneDrive - GUSCanada\VSCODEGIT\MLUNFTERM4\Week2Exercises\week02_ml_assignment.ipynb'

# Load notebook JSON. We open with utf-8 to handle most characters safely.
with open(p, encoding='utf-8') as fh:
    nb = json.load(fh)

# Iterate over cells and print code cells' source for inspection.
# We use enumerate(..., start=1) so the printed cell numbers match Jupyter's 1-based
# counting style and are easy to cross-reference with the notebook UI.
for i, cell in enumerate(nb.get('cells', []), start=1):
    # Only show code cells; skip markdown and other cell types.
    if cell.get('cell_type') == 'code':
        # Join the list of source lines into a single string so it prints as it would
        # appear when executed. We do not execute the code here; we only display it.
        src = ''.join(cell.get('source', []))

        # Print a compact header (cell number). We avoid printing internal cell IDs
        # here because notebook viewers don't always show them; if needed the script
        # includes the metadata id for debugging purposes.
        print('--- CELL', i, 'id=', cell.get('metadata', {}).get('id'))

        # Use repr(...) to show hidden characters and newlines clearly. This makes
        # unterminated strings and stray characters visible in the output.
        print(repr(src))
        print()
