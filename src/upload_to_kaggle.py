"""
upload_to_kaggle.py
-------------------
Helper script for uploading the synthetic dataset to Kaggle.
Uses the Kaggle CLI for authentication and upload.

SECURITY NOTE: This script does NOT store or print any API tokens.
Authentication is handled through the Kaggle CLI configuration.
"""

import os
import subprocess
import sys


def check_kaggle_installed():
    """Check if kaggle CLI is installed."""
    try:
        result = subprocess.run(
            ["kaggle", "--version"],
            capture_output=True, text=True, check=True
        )
        print(f"Kaggle CLI version: {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print("ERROR: Kaggle CLI not found.")
        print("Install with: pip install kaggle")
        return False
    except subprocess.CalledProcessError:
        print("ERROR: Kaggle CLI not working properly.")
        return False


def check_kaggle_config():
    """Check if Kaggle API token is configured."""
    kaggle_dir = os.path.join(os.path.expanduser("~"), ".kaggle")
    kaggle_json = os.path.join(kaggle_dir, "kaggle.json")
    
    if os.path.exists(kaggle_json):
        print("Kaggle API token found.")
        return True
    else:
        print("Kaggle API token NOT found.")
        print()
        print("To set up Kaggle authentication:")
        print("1. Go to https://www.kaggle.com/settings")
        print("2. Click 'Create New Token'")
        print(f"3. Place the downloaded kaggle.json in: {kaggle_dir}")
        print()
        return False


def show_upload_instructions():
    """Print step-by-step upload instructions."""
    print()
    print("=" * 60)
    print("KAGGLE UPLOAD INSTRUCTIONS")
    print("=" * 60)
    print()
    print("The kaggle/ folder contains:")
    print("  - synthetic_heart_disease_100.csv")
    print("  - dataset-metadata.json")
    print("  - README_KAGGLE.md")
    print("  - visualizations (optional)")
    print()
    print("Option 1: Create new dataset (Command Line)")
    print("-" * 50)
    print("  cd kaggle")
    print("  kaggle datasets create -p .")
    print()
    print("Option 2: Create as public dataset")
    print("-" * 50)
    print("  cd kaggle")
    print("  kaggle datasets create -p . --public")
    print()
    print("Option 3: Update existing dataset")
    print("-" * 50)
    print("  cd kaggle")
    print("  kaggle datasets version -p . -m 'Updated synthetic dataset'")
    print()
    print("IMPORTANT:")
    print("  - Replace YOUR_KAGGLE_USERNAME in dataset-metadata.json")
    print("  - Before uploading, ensure your API token is configured")
    print("  - Use --public flag only if you want the dataset publicly visible")
    print()
    print("=" * 60)


def main():
    """Main function to guide Kaggle upload."""
    print()
    print("=" * 60)
    print("KAGGLE UPLOAD HELPER")
    print("=" * 60)
    
    # Check if kaggle is installed
    if not check_kaggle_installed():
        show_upload_instructions()
        return
    
    # Check if token is configured
    if not check_kaggle_config():
        show_upload_instructions()
        return
    
    # Show instructions
    show_upload_instructions()
    
    # Ask user if they want to proceed
    print()
    response = input("Would you like to open the kaggle folder? (y/n): ").strip().lower()
    
    if response == 'y':
        kaggle_dir = os.path.join(os.getcwd(), "kaggle")
        if os.path.exists(kaggle_dir):
            print(f"\nFiles in kaggle/ folder:")
            for f in os.listdir(kaggle_dir):
                print(f"  - {f}")
            
            print()
            response2 = input("Run 'kaggle datasets create -p kaggle' now? (y/n): ").strip().lower()
            
            if response2 == 'y':
                print("\nCreating Kaggle dataset...")
                try:
                    result = subprocess.run(
                        ["kaggle", "datasets", "create", "-p", "kaggle"],
                        capture_output=True, text=True
                    )
                    print(result.stdout)
                    if result.stderr:
                        print(result.stderr)
                except Exception as e:
                    print(f"Error running kaggle command: {e}")
                    print("Please run manually: kaggle datasets create -p kaggle")
            else:
                print("\nUpload cancelled. Run manually when ready.")
        else:
            print(f"ERROR: kaggle/ folder not found at {kaggle_dir}")
    else:
        print("\nUpload cancelled. Run the upload commands manually when ready.")


if __name__ == "__main__":
    main()
