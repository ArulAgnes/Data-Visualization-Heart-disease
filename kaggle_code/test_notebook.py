"""Test notebook code cells locally with correct paths."""
import json
import os
import sys

os.chdir(r"D:\M.E CSE\Data V\Assesment\Heart_Disease_Synthetic_Project")
os.makedirs("kaggle_code/outputs", exist_ok=True)

with open("kaggle_code/synthetic-heart-disease-dataset.ipynb") as f:
    nb = json.load(f)

code_cells = [c for c in nb["cells"] if c["cell_type"] == "code"]
print("Testing {} code cells...".format(len(code_cells)))

# Shared namespace for exec
ns = {}

all_ok = True
for i, cell in enumerate(code_cells):
    code = "".join(cell["source"])

    # Skip the Kaggle input path cell - replace with local path
    if "kaggle/input" in code and "rglob" in code:
        csv_path = os.path.join(os.getcwd(), "data", "synthetic", "synthetic_heart_disease_100.csv")
        code = (
            "from pathlib import Path\n"
            "import os\n"
            "files = [Path(r'{}')]\n".format(csv_path) +
            "print(f'Found {len(files)} file(s)')\n"
            "if files:\n"
            "    print(f'Using: {files[0]}')\n"
            "    df = pd.read_csv(files[0])\n"
            "print(f'\\nDataset loaded successfully!')\n"
            "print(f'Shape: {df.shape}')\n"
            "print(f'Columns: {list(df.columns)}')"
        )

    # Fix saving paths for local test
    code = code.replace("'outputs/01_", "'kaggle_code/outputs/01_")
    code = code.replace("'outputs/02_", "'kaggle_code/outputs/02_")
    code = code.replace("'outputs/03_", "'kaggle_code/outputs/03_")
    code = code.replace("'outputs/04_", "'kaggle_code/outputs/04_")
    code = code.replace("'outputs/05_", "'kaggle_code/outputs/05_")
    code = code.replace("'outputs/06_", "'kaggle_code/outputs/06_")
    code = code.replace("'outputs/07_", "'kaggle_code/outputs/07_")
    code = code.replace("'outputs/08_", "'kaggle_code/outputs/08_")
    code = code.replace("'outputs/09_", "'kaggle_code/outputs/09_")
    code = code.replace("'outputs/10_", "'kaggle_code/outputs/10_")
    code = code.replace("'outputs/11_", "'kaggle_code/outputs/11_")
    code = code.replace("'outputs/12_", "'kaggle_code/outputs/12_")
    code = code.replace("'outputs/13_", "'kaggle_code/outputs/13_")
    code = code.replace("'outputs/14_", "'kaggle_code/outputs/14_")
    code = code.replace("'outputs/15_", "'kaggle_code/outputs/15_")
    code = code.replace("'outputs/16_", "'kaggle_code/outputs/16_")
    code = code.replace("'outputs/17_", "'kaggle_code/outputs/17_")
    code = code.replace("'outputs/validation_report.csv'", "'kaggle_code/outputs/validation_report.csv'")
    code = code.replace("'outputs/dataset_summary.csv'", "'kaggle_code/outputs/dataset_summary.csv'")
    code = code.replace("'outputs/heart_disease_visualizations.zip'", "'kaggle_code/outputs/heart_disease_visualizations.zip'")
    code = code.replace("f'outputs/{fname}'", "f'kaggle_code/outputs/{fname}'")

    # Replace plt.show with plt.close
    code = code.replace("plt.show()", "plt.close('all')")

    try:
        exec(code, ns)
        print("  [{:2d}] PASS".format(i + 1))
    except Exception as e:
        print("  [{:2d}] FAIL - {}: {}".format(i + 1, type(e).__name__, e))
        all_ok = False

print("\n" + "=" * 50)
if all_ok:
    print("RESULT: ALL CELLS PASS")
else:
    print("RESULT: SOME CELLS FAILED")

outputs = os.listdir("kaggle_code/outputs") if os.path.exists("kaggle_code/outputs") else []
pngs = [f for f in outputs if f.endswith(".png")]
csvs = [f for f in outputs if f.endswith(".csv")]
zips = [f for f in outputs if f.endswith(".zip")]
print("\nGenerated files:")
print("  PNG images: {}".format(len(pngs)))
print("  CSV files: {}".format(len(csvs)))
print("  ZIP files: {}".format(len(zips)))
for f in sorted(outputs):
    print("    - {}".format(f))
