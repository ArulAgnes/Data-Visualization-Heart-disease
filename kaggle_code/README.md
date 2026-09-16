# Kaggle Code Notebook

## Synthetic Heart Disease Dataset | EDA & Visualization

**Notebook URL:** https://www.kaggle.com/code/arulmariaagnes/synthetic-heart-disease-dataset

**Dataset URL:** https://www.kaggle.com/datasets/arulmariaagnes/synthetic-heart-disease-100

---

## Purpose

This notebook performs complete Exploratory Data Analysis (EDA) and visualization on the synthetic heart disease prediction dataset. It is designed to run directly on Kaggle and display all charts inline.

---

## Notebook Sections

| # | Section | Description |
|---|---------|-------------|
| 1 | Project Overview | Dataset description and disclaimer |
| 2 | Import Libraries | pandas, numpy, matplotlib, seaborn |
| 3 | Load Dataset | Auto-locate CSV from /kaggle/input/ |
| 4 | Dataset Information | shape, info, describe, missing values |
| 5 | Dataset Validation | 7 comprehensive validation checks |
| 6 | Target Distribution | Bar chart with counts and percentages |
| 7 | Age Distribution | Histogram with mean line |
| 8 | Heart Disease by Sex | Grouped bar chart |
| 9 | Heart Disease by Smoking | Grouped bar chart |
| 10 | Heart Disease by Diabetes | Grouped bar chart |
| 11 | Physical Activity Analysis | Grouped bar chart |
| 12 | BMI Analysis | Histogram + boxplot |
| 13 | Cholesterol Analysis | Histogram + boxplot |
| 14 | Resting BP Analysis | Histogram + boxplot |
| 15 | Max Heart Rate Analysis | Histogram + boxplot |
| 16 | ST Depression Analysis | Histogram + boxplot |
| 17 | Chest Pain Type Analysis | Count + cross-tabulation |
| 18 | ECG Analysis | Grouped bar chart |
| 19 | Major Vessels Analysis | Grouped bar chart |
| 20 | Correlation Heatmap | Full correlation matrix |
| 21 | Risk Factor Summary | 6-box panel comparison |
| 22 | Dashboard Summary | Multi-panel dashboard |
| 23 | Final Findings | Text summary of observations |
| 24 | Save Downloadable Outputs | ZIP, CSV exports |
| 25 | Conclusion | Summary and links |

---

## Visualizations

17 PNG images generated:

1. `01_target_distribution.png`
2. `02_age_distribution.png`
3. `03_heart_disease_by_sex.png`
4. `04_heart_disease_by_smoking.png`
5. `05_heart_disease_by_diabetes.png`
6. `06_physical_activity.png`
7. `07_bmi_analysis.png`
8. `08_cholesterol_analysis.png`
9. `09_resting_bp_analysis.png`
10. `10_max_heart_rate_analysis.png`
11. `11_st_depression_analysis.png`
12. `12_chest_pain_analysis.png`
13. `13_ecg_analysis.png`
14. `14_major_vessels_analysis.png`
15. `15_correlation_heatmap.png`
16. `16_risk_factor_summary.png`
17. `17_dashboard_summary.png`

---

## Output Files

| File | Description |
|------|-------------|
| `heart_disease_visualizations.zip` | All 17 PNG visualizations |
| `validation_report.csv` | Validation check results |
| `dataset_summary.csv` | Descriptive statistics |

---

## How to Reproduce

### On Kaggle
1. Open the notebook URL
2. Click "Run All"
3. All charts display inline
4. Download outputs from /kaggle/working/outputs/

### Locally
```bash
pip install pandas numpy matplotlib seaborn
cd kaggle_code
jupyter notebook synthetic-heart-disease-dataset.ipynb
```

Note: When running locally, place `synthetic_heart_disease_100.csv` in the same directory or update the file path in the load cell.

---

## Synthetic Data Disclaimer

This notebook uses a **synthetic educational dataset**. The 100 patient records are algorithmically generated and do **NOT** represent real patients. They are not intended for diagnosis, treatment, or clinical decision-making.

---

## Links

- **Dataset:** https://www.kaggle.com/datasets/arulmariaagnes/synthetic-heart-disease-100
- **GitHub:** https://github.com/ArulAgnes/Data-Visualization-Heart-disease
