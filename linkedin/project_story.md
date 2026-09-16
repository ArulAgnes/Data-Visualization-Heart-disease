# Project Story – Heart Disease Prediction

## 1. Starting Point

I wanted to create a data visualization portfolio project that demonstrated end-to-end data skills: data generation, validation, visualization, and publication. Heart disease prediction is a well-known ML problem, making it ideal for a beginner portfolio piece.

## 2. Source Dataset

I found the Heart Disease Health Indicators Dataset on Kaggle, containing 253,680 CDC BRFSS 2015 survey records with 22 health indicators. This became my reference for understanding how risk factors relate to heart disease.

However, the source dataset has survey-level variables (HighBP, Smoker, BMI) that differ from clinical variables (Resting_BP, Cholesterol, ST_Depression) used in standard heart disease datasets. I decided to create a synthetic dataset with clinical-style variables.

## 3. Data Understanding

I analyzed the source dataset and identified key patterns:

- Heart disease prevalence: ~9.4%
- Strong correlations: age, high BP, high cholesterol, diabetes, smoking
- Risk increases with multiple factors combined
- Physical activity has a protective (inverse) effect

These patterns became the foundation for my synthetic data generation rules.

## 4. Synthetic Data Design

I designed 20 columns combining:

- Patient identifiers (Patient_ID)
- Demographics (Age, Sex)
- Clinical measurements (Resting_BP, Cholesterol, Max_Heart_Rate, ST_Depression)
- Diagnostic indicators (Chest_Pain_Type, Resting_ECG, Thalassemia)
- Lifestyle risk factors (BMI, Smoking, Diabetes, Physical_Activity, Family_History)
- Target variable (Heart_Disease)

## 5. Risk-Based Target Generation

Instead of randomly assigning heart disease labels, I implemented a probabilistic risk-scoring system:

- Each risk factor contributes to a composite score
- Age increases BP and cholesterol probability
- Smoking increases BP and reduces max heart rate
- Physical activity reduces BMI and BP
- ST depression relates to ECG abnormality
- The final score converts to probability via sigmoid transformation

This creates realistic variation where most high-risk patients have heart disease, but some exceptions exist.

## 6. Validation

I created comprehensive validation checking:

- Exactly 100 rows and 20 columns
- Patient IDs P001 to P100
- No duplicates or missing values
- All categorical values in valid sets
- All numeric values in valid ranges
- Target balance between 45 and 55 per class

All 10 checks passed.

## 7. Visualization

I generated 14 visualizations using matplotlib and seaborn:

- Distribution charts (age, BMI, cholesterol, BP, heart rate, ST depression)
- Grouped bar charts (heart disease by sex, smoking, diabetes, activity)
- Correlation heatmap
- Risk factor comparison box plots
- Summary dashboard

All images saved at 200+ DPI for professional quality.

## 8. Kaggle Publication

I prepared the dataset for Kaggle publication:

- Dataset with 100 CSV records
- Metadata JSON with complete schema
- README with synthetic data disclaimer
- Cover image (dashboard)

Published at: arulmariaagnes/synthetic-heart-disease-100

## 9. GitHub Publication

I organized the complete project on GitHub with:

- Clean folder structure
- Professional README with workflow diagram
- Requirements file
- License and gitignore
- LinkedIn portfolio assets

Repository: github.com/ArulAgnes/Data-Visualization-Heart-disease

## 10. Learning Outcomes

Through this project I practiced:

- Synthetic data generation techniques
- Probabilistic modeling for realistic variation
- Data validation methodology
- Professional visualization design
- Documentation and project organization
- Kaggle and GitHub publication workflows

## 11. Limitations

This project has clear limitations:

- 100 records is small for real ML training
- Synthetic data cannot capture all real-world complexity
- Risk-factor relationships are approximate
- Not validated by medical professionals
- Intended for education only

These limitations are clearly documented throughout the project.
