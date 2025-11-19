MLUNFTERM4 — Week 2 Exercises (Wine classification)

Short description
-----------------
This repository contains the Week 2 machine learning assignment: a single Jupyter notebook that walks through a supervised classification workflow (PART A–F) on scikit-learn's Wine dataset. It includes helper scripts for validating notebook syntax and inspecting code cells, plus saved model artifacts produced when you run the notebook.

Repository layout
-----------------
Week2Exercises/
  - week02_ml_assignment.ipynb         # Main notebook (PART A–F)
  - assignment_instructions.txt        # Human-friendly explanation of what each PART does
  - generated_files_summary.txt        # Concise list of files the notebook can produce
  - nb_syntax_check.py                 # Compile-only checker for notebook code cells
  - inspect_nb_cells.py                # Prints raw code for each code cell (useful for debugging)
  - models/                            # Folder where trained models and scaler joblibs are saved
  - metrics-wine-*.csv                 # Example metrics CSV files produced by the notebook (timestamped)

Quick start
-----------
1. Create a Python environment (recommended):

   # Using venv
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

2. Install required packages:

   pip install -r Week2Exercises/requirements.txt

   If you prefer, install individually: pandas scikit-learn matplotlib seaborn joblib

3. Open `Week2Exercises/week02_ml_assignment.ipynb` in VS Code or Jupyter and run cells in order.

Helpful helper scripts
----------------------
- `nb_syntax_check.py`: quickly detects syntax errors in code cells by trying to compile each cell's source. Run it before executing the notebook to find malformed cells.
- `inspect_nb_cells.py`: prints repr(...) of each code cell's source. Useful to find unterminated strings or invisible unicode characters.

Persisted artifacts
-------------------
- The notebook saves a metrics CSV and the best model + scaler into `models/` with timestamped filenames.
- See `Week2Exercises/generated_files_summary.txt` for a concise table describing these files.

Next steps / suggestions
------------------------
- If you want saved PNG plots, I can patch the notebook to call `plt.savefig(...)` and create a `plots/` folder.
- I can also run the notebook non-interactively here and report the files created.

Contact / notes
---------------
Open an issue or message me here with which additional artifacts you'd like saved automatically (plots, executed notebook, logs).