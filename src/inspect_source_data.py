"""
inspect_source_data.py
---------------------
Reads and inspects the original BRFSS heart disease dataset.
Prints shape, columns, info, missing values, duplicates, and basic statistics.
"""

import pandas as pd
import os

def inspect_source():
    """Load and inspect the original source CSV file."""
    
    # Path to source file
    source_path = os.path.join("data", "source", "heart_disease_health_indicators_BRFSS2015.csv")
    
    print("=" * 60)
    print("SOURCE DATA INSPECTION")
    print("=" * 60)
    
    # Check if file exists
    if not os.path.exists(source_path):
        print(f"ERROR: Source file not found at {source_path}")
        return None
    
    print(f"\nFile: {source_path}")
    print(f"File size: {os.path.getsize(source_path) / (1024*1024):.2f} MB")
    
    # Read the CSV
    df = pd.read_csv(source_path)
    
    # Basic info
    print(f"\nShape (rows, columns): {df.shape}")
    print(f"\nColumn names:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")
    
    # Data types
    print(f"\nData Types:")
    print(df.dtypes)
    
    # First 5 rows
    print(f"\nHead (first 5 rows):")
    print(df.head())
    
    # Missing values
    print(f"\nMissing Values:")
    print(df.isnull().sum())
    
    # Duplicates
    print(f"\nDuplicate rows: {df.duplicated().sum()}")
    
    # Describe
    print(f"\nDescriptive Statistics:")
    print(df.describe())
    
    # Target distribution (if HeartDiseaseorAttack exists)
    if "HeartDiseaseorAttack" in df.columns:
        print(f"\nTarget Distribution (HeartDiseaseorAttack):")
        print(df["HeartDiseaseorAttack"].value_counts())
        print(f"\nTarget Percentages:")
        print(df["HeartDiseaseorAttack"].value_counts(normalize=True) * 100)
    
    # Summary
    print("\n" + "=" * 60)
    print("SOURCE DATA SUMMARY")
    print("=" * 60)
    print(f"- Total records: {df.shape[0]}")
    print(f"- Total features: {df.shape[1]}")
    print(f"- Missing values: {df.isnull().sum().sum()}")
    print(f"- Duplicate rows: {df.duplicated().sum()}")
    print(f"\nNOTE: This BRFSS dataset contains survey-level health indicators.")
    print("It is used ONLY as a reference for realistic risk-factor patterns.")
    print("The synthetic dataset uses DIFFERENT clinical variable definitions.")
    print("=" * 60)
    
    return df

if __name__ == "__main__":
    inspect_source()
