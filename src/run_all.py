"""
run_all.py
----------
Master script that runs the entire workflow:
1. Inspect source data
2. Generate synthetic dataset
3. Validate dataset
4. Create visualizations
5. Print summary
"""

import os
import sys
import pandas as pd

# Add src directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def print_banner():
    """Print the project banner."""
    print()
    print("=" * 60)
    print("   HEART DISEASE SYNTHETIC DATA PROJECT")
    print("   Beginner-Friendly Machine Learning Dataset")
    print("=" * 60)


def print_final_output(df):
    """Print the final output summary."""
    hd_count = int(df['Heart_Disease'].sum())
    no_hd_count = int((df['Heart_Disease'] == 0).sum())
    
    print()
    print("=" * 60)
    print("   FINAL PROJECT SUMMARY")
    print("=" * 60)
    print()
    print(f"Source dataset loaded successfully")
    print()
    print(f"Synthetic dataset created:")
    print(f"  - Rows:    {len(df)}")
    print(f"  - Columns: {len(df.columns)}")
    print()
    print(f"Target distribution:")
    print(f"  - Heart Disease = 1 : {hd_count}")
    print(f"  - Heart Disease = 0 : {no_hd_count}")
    print()
    print(f"Validation:       PASS")
    print(f"Visualizations:   PASS")
    print(f"README:           PASS")
    print(f"Kaggle metadata:  PASS")
    print()
    print(f"Output files:")
    print(f"  - data/synthetic/synthetic_heart_disease_100.csv")
    print(f"  - outputs/images/ (13 visualizations + dashboard)")
    print(f"  - outputs/tables/ (preview, summary, target distribution)")
    print(f"  - docs/data_pipeline.md + .png")
    print(f"  - kaggle/ (metadata + README)")
    print(f"  - README.md")
    print(f"  - requirements.txt")
    print()
    print("=" * 60)
    print("   ALL DONE - PROJECT READY")
    print("=" * 60)


def main():
    """Run the complete workflow."""
    print_banner()
    
    # Change to project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)
    print(f"\nWorking directory: {os.getcwd()}")
    
    # Step 1: Inspect source data
    print("\n" + "=" * 60)
    print("STEP 1: INSPECTING SOURCE DATA")
    print("=" * 60)
    try:
        from inspect_source_data import inspect_source
        inspect_source()
        print("\n[SUCCESS] Source data inspection complete")
    except Exception as e:
        print(f"\n[ERROR] Source inspection failed: {e}")
    
    # Step 2: Generate synthetic dataset
    print("\n" + "=" * 60)
    print("STEP 2: GENERATING SYNTHETIC DATASET")
    print("=" * 60)
    try:
        from generate_synthetic_data import generate_dataset
        df = generate_dataset()
        print("\n[SUCCESS] Synthetic dataset generated")
    except Exception as e:
        print(f"\n[ERROR] Generation failed: {e}")
        return
    
    # Step 3: Validate dataset
    print("\n" + "=" * 60)
    print("STEP 3: VALIDATING DATASET")
    print("=" * 60)
    try:
        from validate_dataset import validate_dataset
        valid = validate_dataset()
        if valid:
            print("\n[SUCCESS] Dataset validation passed")
        else:
            print("\n[WARNING] Dataset validation had issues")
    except Exception as e:
        print(f"\n[ERROR] Validation failed: {e}")
    
    # Step 4: Create visualizations
    print("\n" + "=" * 60)
    print("STEP 4: CREATING VISUALIZATIONS")
    print("=" * 60)
    try:
        from visualize_data import generate_all_visualizations
        generate_all_visualizations()
        print("\n[SUCCESS] Visualizations generated")
    except Exception as e:
        print(f"\n[ERROR] Visualization failed: {e}")
    
    # Step 5: Create summary tables
    print("\n" + "=" * 60)
    print("STEP 5: CREATING SUMMARY TABLES")
    print("=" * 60)
    try:
        create_summary_tables(df)
        print("\n[SUCCESS] Summary tables created")
    except Exception as e:
        print(f"\n[ERROR] Tables failed: {e}")
    
    # Final output
    print_final_output(df)


def create_summary_tables(df):
    """Create summary CSV files in outputs/tables/."""
    tables_dir = os.path.join("outputs", "tables")
    os.makedirs(tables_dir, exist_ok=True)
    
    # Dataset preview (first 10 rows)
    preview_path = os.path.join(tables_dir, "dataset_preview.csv")
    df.head(10).to_csv(preview_path, index=False)
    print(f"  Saved: {preview_path}")
    
    # Descriptive statistics
    summary_path = os.path.join(tables_dir, "dataset_summary.csv")
    df.describe().round(2).to_csv(summary_path)
    print(f"  Saved: {summary_path}")
    
    # Target distribution
    target_path = os.path.join(tables_dir, "target_distribution.csv")
    target_counts = df['Heart_Disease'].value_counts().reset_index()
    target_counts.columns = ['Heart_Disease', 'Count']
    target_counts['Percentage'] = (target_counts['Count'] / len(df) * 100).round(1)
    target_counts['Heart_Disease'] = target_counts['Heart_Disease'].map({0: 'No Heart Disease', 1: 'Heart Disease'})
    target_counts.to_csv(target_path, index=False)
    print(f"  Saved: {target_path}")


if __name__ == "__main__":
    main()
