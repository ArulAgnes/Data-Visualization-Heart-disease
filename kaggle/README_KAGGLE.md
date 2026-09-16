# Synthetic Heart Disease Prediction – 100 Patient Records

> **Beginner-friendly synthetic dataset for heart disease ML practice**

## Overview

This dataset contains **exactly 100 synthetic patient records** with **20 clinical features** designed for beginner-level machine learning practice in heart disease prediction.

**This is SYNTHETIC data.** The records are algorithmically generated and do NOT represent real patients.

## Dataset Description

| Property | Value |
|----------|-------|
| Records | 100 |
| Features | 20 (including target) |
| Target | Heart_Disease (0/1) |
| Target Balance | ~50/50 (46/54) |
| Patient IDs | P001 – P100 |

## Features

| # | Feature | Type | Description |
|---|---------|------|-------------|
| 1 | Patient_ID | Identifier | P001 – P100 |
| 2 | Age | Numeric | 25 – 80 years |
| 3 | Sex | Binary | 0 = Female, 1 = Male |
| 4 | Chest_Pain_Type | Categorical | 0–3 (Typical Angina to Asymptomatic) |
| 5 | Resting_BP | Numeric | Resting blood pressure (mmHg) |
| 6 | Cholesterol | Numeric | Serum cholesterol (mg/dL) |
| 7 | Fasting_Blood_Sugar | Binary | 0 = ≤120, 1 = >120 mg/dL |
| 8 | Resting_ECG | Categorical | 0–2 (Normal to LV hypertrophy) |
| 9 | Max_Heart_Rate | Numeric | Maximum heart rate achieved |
| 10 | Exercise_Induced_Angina | Binary | 0 = No, 1 = Yes |
| 11 | ST_Depression | Numeric | 0.0 – 6.0 |
| 12 | ST_Slope | Categorical | 0–2 (Downsloping to Upsloping) |
| 13 | Num_Major_Vessels | Ordinal | 0 – 3 |
| 14 | Thalassemia | Categorical | 0–2 (Normal to Reversible Defect) |
| 15 | BMI | Numeric | 18 – 40 kg/m² |
| 16 | Smoking | Binary | 0 = No, 1 = Yes |
| 17 | Diabetes | Binary | 0 = No, 1 = Yes |
| 18 | Family_History | Binary | 0 = No, 1 = Yes |
| 19 | Physical_Activity | Categorical | 0 = Low, 1 = Moderate, 2 = High |
| 20 | Heart_Disease | Target | 0 = No, 1 = Yes |

## Usage Examples

### Load with pandas

```python
import pandas as pd

df = pd.read_csv('synthetic_heart_disease_100.csv')
print(df.shape)
print(df.head())
```

### Train a simple model

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X = df.drop(['Patient_ID', 'Heart_Disease'], axis=1)
y = df['Heart_Disease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
```

### Feature importance

```python
import matplotlib.pyplot as plt

importance = pd.Series(model.feature_importances_, index=X.columns)
importance.sort_values(ascending=True).plot(kind='barh', figsize=(10, 8))
plt.title('Feature Importance')
plt.xlabel('Importance')
plt.tight_layout()
plt.show()
```

## Data Generation

The synthetic data is generated using **probabilistic risk-factor relationships**:

- Risk score calculated from: age, sex, BMI, smoking, diabetes, family history, physical activity, BP, cholesterol, ECG, ST depression, angina, vessels, thalassemia
- Heart Disease target generated probabilistically from risk score
- Rebalanced to achieve ~50/50 class distribution

## Synthetic Data Disclaimer

> **This dataset is SYNTHETIC and for EDUCATIONAL purposes only.**
> 
> - 100 algorithmically generated patient records
> - NOT real patient data
> - NOT validated for clinical use
> - NOT for medical diagnosis
> - Risk-factor relationships are approximate
> - Intended for ML practice and learning

## Source Reference

This synthetic dataset uses risk-factor patterns inspired by the [Heart Disease Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset) (BRFSS 2015) as reference. No records are copied from the source.

## License

MIT License – Educational use

## Citation

If using this dataset, please acknowledge it as synthetic data generated for educational purposes.
