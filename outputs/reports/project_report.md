# Project Report – Heart Disease Synthetic Dataset

## Executive Summary

This project successfully generated a synthetic heart disease prediction dataset containing exactly **100 patient records** with **20 clinical features**. The dataset is designed for educational purposes and beginner-level machine learning practice.

## Project Metadata

| Property | Value |
|----------|-------|
| Project Name | Heart Disease Prediction – Synthetic Dataset |
| Total Records | 100 |
| Total Features | 20 (including target) |
| Target Variable | Heart_Disease (binary) |
| Target Distribution | 46 Heart Disease / 54 No Heart Disease |
| Random Seed | 42 |
| Generation Method | Probabilistic risk scoring |

## Key Statistics

### Demographics

| Feature | Mean | Min | Max |
|---------|------|-----|-----|
| Age | 52.0 years | 25 | 80 |
| Sex | 55% Male | — | — |
| BMI | 28.0 kg/m² | 18.0 | 40.0 |

### Clinical Measurements

| Feature | Mean | Min | Max |
|---------|------|-----|-----|
| Resting BP | 119.8 mmHg | 90 | 200 |
| Cholesterol | 196.8 mg/dL | 120 | 400 |
| Max Heart Rate | ~150 bpm | 100 | 210 |
| ST Depression | ~1.5 | 0.0 | 6.0 |

### Risk Factors

| Factor | Prevalence |
|--------|-----------|
| Smoking | 28% |
| Diabetes | 17% |
| Family History | 40% |
| Low Physical Activity | 25-35% |

## Validation Results

All validation checks passed:

- ✅ Exactly 100 rows
- ✅ Exactly 20 columns
- ✅ Correct column order
- ✅ Patient IDs P001–P100
- ✅ No duplicate IDs
- ✅ No duplicate records
- ✅ No missing values
- ✅ All ranges valid
- ✅ All categorical values valid
- ✅ Target balance within 45–55

## Data Generation Method

The synthetic data was generated using a **probabilistic risk-scoring approach**:

1. Demographics generated first (age, sex)
2. Lifestyle factors generated with age-dependent probabilities
3. Clinical measurements influenced by demographics and lifestyle
4. Composite risk score calculated from all factors
5. Heart Disease target generated probabilistically
6. Dataset rebalanced to ~50/50 distribution

### Risk-Factor Relationships Implemented

- Age → higher BP, cholesterol, ECG abnormality probability
- Smoking → higher BP, lower max heart rate
- Diabetes → higher BP, cholesterol, fasting blood sugar
- BMI → higher BP, cholesterol
- Physical Activity → lower BMI, BP, cholesterol (inverse)
- ECG abnormality → higher ST depression probability
- ST depression → different ST slope distributions

## Visualizations Generated

14 high-resolution visualization files created:

1. Heart Disease distribution (bar chart)
2. Age distribution (histogram)
3. Heart Disease by sex (grouped bar)
4. Heart Disease by smoking (grouped bar)
5. Heart Disease by diabetes (grouped bar)
6. Heart Disease by physical activity (grouped bar)
7. BMI distribution (histogram)
8. Cholesterol distribution (histogram)
9. Resting BP distribution (histogram)
10. Max heart rate distribution (histogram)
11. ST depression distribution (histogram)
12. Correlation heatmap
13. Risk factors vs heart disease (box plots)
14. Summary dashboard (multi-panel)

## Output Files

| File | Description |
|------|-------------|
| `data/synthetic/synthetic_heart_disease_100.csv` | Final dataset |
| `outputs/images/*.png` | Visualization images |
| `outputs/tables/dataset_preview.csv` | First 10 rows |
| `outputs/tables/dataset_summary.csv` | Descriptive statistics |
| `outputs/tables/target_distribution.csv` | Class distribution |
| `docs/data_pipeline.png` | Workflow diagram |

## Limitations

1. Synthetic data — not real patient records
2. 100 records — small for production ML
3. Probabilistic relationships — approximate correlations
4. No temporal or imaging data
5. Not validated for clinical use

## Conclusion

This project demonstrates a complete beginner-level data science workflow:

- Data inspection and exploration
- Synthetic data generation with realistic relationships
- Comprehensive validation
- Professional visualization
- Clean project structure
- Kaggle-ready documentation

The dataset is suitable for educational ML practice, student assessments, and learning data science workflows.
