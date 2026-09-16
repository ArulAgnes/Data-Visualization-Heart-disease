"""
validate_dataset.py
------------------
Validates the synthetic heart disease dataset against all required constraints.
Prints a clear validation report.
"""

import pandas as pd
import os

# Expected column names in exact order
EXPECTED_COLUMNS = [
    "Patient_ID", "Age", "Sex", "Chest_Pain_Type", "Resting_BP",
    "Cholesterol", "Fasting_Blood_Sugar", "Resting_ECG", "Max_Heart_Rate",
    "Exercise_Induced_Angina", "ST_Depression", "ST_Slope",
    "Num_Major_Vessels", "Thalassemia", "BMI", "Smoking",
    "Diabetes", "Family_History", "Physical_Activity", "Heart_Disease"
]


def validate_dataset():
    """Run all validation checks on the synthetic dataset."""
    
    csv_path = os.path.join("data", "synthetic", "synthetic_heart_disease_100.csv")
    
    print("=" * 60)
    print("DATASET VALIDATION")
    print("=" * 60)
    
    # Load dataset
    try:
        df = pd.read_csv(csv_path)
        print(f"\nLoaded: {csv_path}")
    except Exception as e:
        print(f"\nERROR: Could not load CSV: {e}")
        return False
    
    results = {}
    
    # 1. Check exactly 100 rows
    results["Rows"] = len(df) == 100
    print(f"\nRows: {len(df)} - {'PASS' if results['Rows'] else 'FAIL'}")
    
    # 2. Check exactly 20 columns
    results["Columns"] = len(df.columns) == 20
    print(f"Columns: {len(df.columns)} - {'PASS' if results['Columns'] else 'FAIL'}")
    
    # 3. Check exact column order
    results["Column Order"] = list(df.columns) == EXPECTED_COLUMNS
    print(f"Column Order - {'PASS' if results['Column Order'] else 'FAIL'}")
    if not results["Column Order"]:
        print(f"  Expected: {EXPECTED_COLUMNS}")
        print(f"  Got: {list(df.columns)}")
    
    # 4. Check Patient_ID format P001-P100
    expected_ids = [f"P{i:03d}" for i in range(1, 101)]
    actual_ids = df["Patient_ID"].tolist()
    results["Patient IDs"] = actual_ids == expected_ids
    print(f"Patient IDs (P001-P100) - {'PASS' if results['Patient IDs'] else 'FAIL'}")
    
    # 5. Check no duplicate IDs
    results["No Duplicate IDs"] = df["Patient_ID"].nunique() == 100
    print(f"No Duplicate IDs - {'PASS' if results['No Duplicate IDs'] else 'FAIL'}")
    
    # 6. Check no duplicate complete records
    results["No Duplicate Records"] = df.duplicated().sum() == 0
    print(f"No Duplicate Records - {'PASS' if results['No Duplicate Records'] else 'FAIL'}")
    
    # 7. Check no missing values
    results["No Missing Values"] = df.isnull().sum().sum() == 0
    missing = df.isnull().sum().sum()
    print(f"No Missing Values: {missing} - {'PASS' if results['No Missing Values'] else 'FAIL'}")
    
    # 8. Check ranges for numeric/categorical columns
    range_checks = {
        "Age": (25, 80),
        "Sex": (0, 1),
        "Chest_Pain_Type": (0, 3),
        "Resting_BP": (80, 210),
        "Cholesterol": (100, 400),
        "Fasting_Blood_Sugar": (0, 1),
        "Resting_ECG": (0, 2),
        "Max_Heart_Rate": (80, 220),
        "Exercise_Induced_Angina": (0, 1),
        "ST_Depression": (0, 6),
        "ST_Slope": (0, 2),
        "Num_Major_Vessels": (0, 3),
        "Thalassemia": (0, 2),
        "BMI": (18, 40),
        "Smoking": (0, 1),
        "Diabetes": (0, 1),
        "Family_History": (0, 1),
        "Physical_Activity": (0, 2),
        "Heart_Disease": (0, 1)
    }
    
    all_ranges_pass = True
    for col, (min_val, max_val) in range_checks.items():
        col_min = df[col].min()
        col_max = df[col].max()
        col_pass = col_min >= min_val and col_max <= max_val
        if not col_pass:
            all_ranges_pass = False
            print(f"  {col}: FAIL (min={col_min}, max={col_max}, expected {min_val}-{max_val})")
    
    results["Ranges"] = all_ranges_pass
    print(f"Ranges - {'PASS' if results['Ranges'] else 'FAIL'}")
    
    # 9. Check categorical values
    categorical_checks = {
        "Sex": [0, 1],
        "Chest_Pain_Type": [0, 1, 2, 3],
        "Fasting_Blood_Sugar": [0, 1],
        "Resting_ECG": [0, 1, 2],
        "Exercise_Induced_Angina": [0, 1],
        "ST_Slope": [0, 1, 2],
        "Num_Major_Vessels": [0, 1, 2, 3],
        "Thalassemia": [0, 1, 2],
        "Smoking": [0, 1],
        "Diabetes": [0, 1],
        "Family_History": [0, 1],
        "Physical_Activity": [0, 1, 2],
        "Heart_Disease": [0, 1]
    }
    
    all_categorical_pass = True
    for col, valid_vals in categorical_checks.items():
        actual_vals = sorted(df[col].unique().tolist())
        if actual_vals != sorted(valid_vals):
            all_categorical_pass = False
            print(f"  {col}: FAIL (values={actual_vals}, expected={valid_vals})")
    
    results["Categorical Values"] = all_categorical_pass
    print(f"Categorical Values - {'PASS' if results['Categorical Values'] else 'FAIL'}")
    
    # 10. Check target balance (45-55 for each class)
    hd_count = df["Heart_Disease"].sum()
    no_hd_count = len(df) - hd_count
    results["Target Balance"] = (45 <= hd_count <= 55) and (45 <= no_hd_count <= 55)
    print(f"Target Balance: HD={hd_count}, No HD={no_hd_count} - {'PASS' if results['Target Balance'] else 'FAIL'}")
    
    # Overall status
    all_pass = all(results.values())
    print(f"\n{'=' * 60}")
    print(f"OVERALL STATUS: {'PASS' if all_pass else 'FAIL'}")
    print(f"{'=' * 60}")
    
    if all_pass:
        print("\nAll validation checks passed successfully!")
    else:
        failed = [k for k, v in results.items() if not v]
        print(f"\nFailed checks: {', '.join(failed)}")
    
    return all_pass


if __name__ == "__main__":
    validate_dataset()
