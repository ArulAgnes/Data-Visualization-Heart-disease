"""Final verification audit."""
import pandas as pd
import os
import re

print("=" * 60)
print("FINAL VERIFICATION AUDIT")
print("=" * 60)

results = []

# 1. CSV verification
df = pd.read_csv("data/synthetic/synthetic_heart_disease_100.csv")
r = len(df) == 100
results.append(("CSV rows = 100", r, len(df)))
print(f"\n[1] CSV rows: {len(df)} - {'PASS' if r else 'FAIL'}")

# 2. Columns
r = len(df.columns) == 20
results.append(("CSV columns = 20", r, len(df.columns)))
print(f"[2] CSV columns: {len(df.columns)} - {'PASS' if r else 'FAIL'}")

# 3. Patient IDs
expected_ids = [f"P{i:03d}" for i in range(1, 101)]
r = df["Patient_ID"].tolist() == expected_ids
results.append(("Patient IDs P001-P100", r, ""))
print(f"[3] Patient IDs P001-P100 - {'PASS' if r else 'FAIL'}")

# 4. No duplicates
r = df.duplicated().sum() == 0
results.append(("No duplicate records", r, df.duplicated().sum()))
print(f"[4] No duplicate records: {df.duplicated().sum()} - {'PASS' if r else 'FAIL'}")

# 5. No missing values
r = df.isnull().sum().sum() == 0
results.append(("No missing values", r, df.isnull().sum().sum()))
print(f"[5] No missing values: {df.isnull().sum().sum()} - {'PASS' if r else 'FAIL'}")

# 6. Target distribution
hd1 = int(df["Heart_Disease"].sum())
hd0 = int((df["Heart_Disease"] == 0).sum())
r = 45 <= hd1 <= 55 and 45 <= hd0 <= 55
results.append(("Target balance", r, f"HD=1:{hd1}, HD=0:{hd0}"))
print(f"[6] Target distribution: HD=1:{hd1}, HD=0:{hd0} - {'PASS' if r else 'FAIL'}")

# 7. Visualizations
imgs = [f for f in os.listdir("outputs/images") if f.endswith(".png")]
r = len(imgs) >= 14
results.append(("Visualization images", r, len(imgs)))
print(f"[7] Visualization images: {len(imgs)} - {'PASS' if r else 'FAIL'}")

# 8. Dashboard
r = os.path.exists("outputs/images/heart_disease_dashboard.png")
results.append(("Dashboard exists", r, ""))
print(f"[8] Dashboard exists - {'PASS' if r else 'FAIL'}")

# 9. Pipeline diagram
r = os.path.exists("docs/data_pipeline.png")
results.append(("Pipeline diagram", r, ""))
print(f"[9] Pipeline diagram - {'PASS' if r else 'FAIL'}")

# 10. README
r = os.path.exists("README.md")
results.append(("README exists", r, ""))
print(f"[10] README exists - {'PASS' if r else 'FAIL'}")

# 11. Kaggle metadata
r = os.path.exists("kaggle/dataset-metadata.json")
results.append(("Kaggle metadata", r, ""))
print(f"[11] Kaggle metadata - {'PASS' if r else 'FAIL'}")

# 12. Requirements
r = os.path.exists("requirements.txt")
results.append(("Requirements.txt", r, ""))
print(f"[12] Requirements.txt - {'PASS' if r else 'FAIL'}")

# 13. LinkedIn images
li_imgs = [f for f in os.listdir("linkedin/images") if f.endswith(".png")]
r = len(li_imgs) >= 9
results.append(("LinkedIn images", r, len(li_imgs)))
print(f"[13] LinkedIn images: {len(li_imgs)} - {'PASS' if r else 'FAIL'}")

# 14. No credentials
creds_found = False
for root, dirs, files in os.walk("."):
    if "__pycache__" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith((".py", ".md", ".json", ".txt")):
            try:
                with open(os.path.join(root, f), "r", errors="ignore") as fh:
                    content = fh.read()
                    if re.search(r"KGAT_[a-zA-Z0-9]{20,}", content):
                        creds_found = True
                        print(f"  CREDENTIAL FOUND in {f}")
            except Exception:
                pass
r = not creds_found
results.append(("No credentials", r, ""))
print(f"[14] No credentials in files - {'PASS' if r else 'FAIL'}")

# Summary
print("\n" + "=" * 60)
passed = sum(1 for _, v, _ in results if v)
total = len(results)
print(f"AUDIT RESULT: {passed}/{total} checks passed")
if passed == total:
    print("STATUS: ALL CHECKS PASS")
else:
    failed = [name for name, v, _ in results if not v]
    print(f"FAILED: {', '.join(failed)}")
print("=" * 60)
