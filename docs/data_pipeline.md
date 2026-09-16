# Data Pipeline

This document describes the data processing workflow for the Heart Disease Synthetic Dataset project.

## Mermaid Workflow Diagram

```mermaid
flowchart TD
    A["Original Kaggle Dataset<br/>BRFSS 2015<br/>(253,680 records)"] --> B["Data Inspection<br/>Shape, columns, types<br/>Missing values, duplicates"]
    B --> C["Risk-Factor Reference<br/>Distribution analysis<br/>Pattern identification"]
    C --> D["Synthetic Patient Generation<br/>100 patients<br/>20 clinical features"]
    D --> E["Risk Score Calculation<br/>Probabilistic scoring<br/>Multi-factor combination"]
    E --> F["Target Generation<br/>Heart_Disease label<br/>Based on risk score"]
    F --> G["Rebalancing<br/>~50/50 class distribution<br/>45-55 per class"]
    G --> H["Validation<br/>Ranges, types, uniqueness<br/>All checks PASS"]
    H --> I["Visualization<br/>14 charts + dashboard<br/>PNG output"]
    H --> J["CSV Output<br/>100 rows, 20 columns<br/>synthetic_heart_disease_100.csv"]
    H --> K["Tables<br/>Preview, statistics<br/>Target distribution"]
    J --> L["Kaggle Upload<br/>metadata.json<br/>README_KAGGLE.md"]
    
    style A fill:#E3F2FD,stroke:#1565C0,stroke-width:2px
    style D fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px
    style H fill:#FFF3E0,stroke:#E65100,stroke-width:2px
    style I fill:#F3E5F5,stroke:#6A1B9A,stroke-width:2px
    style J fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px
    style L fill:#E3F2FD,stroke:#1565C0,stroke-width:2px
```

## Pipeline Steps

### 1. Original Kaggle Dataset
- Source: BRFSS 2015 Health Indicators
- 253,680 survey records, 22 features
- Used as reference for risk-factor patterns only

### 2. Data Inspection
- Load and verify source CSV
- Analyze column names, data types, missing values
- Compute basic statistics
- Identify target distribution (HeartDiseaseorAttack)

### 3. Risk-Factor Reference
- Study relationships between risk factors
- Understand distribution of age, BMI, BP, cholesterol
- Note correlation patterns for reference

### 4. Synthetic Patient Generation
- Generate 100 unique patient records (P001–P100)
- 20 clinical features per record
- Age-dependent probabilities for lifestyle factors
- Clinical measurements influenced by demographics and risk factors

### 5. Risk Score Calculation
- Calculate probabilistic risk score from multiple factors
- Combine: age, sex, BMI, smoking, diabetes, family history, physical activity, BP, cholesterol, ECG, ST depression, angina, vessels, thalassemia
- Add random noise for natural variation

### 6. Target Generation
- Convert risk score to probability using sigmoid transformation
- Generate Heart_Disease label probabilistically
- NOT deterministic — some high-risk patients may be negative

### 7. Rebalancing
- Iterate until 45–55 records per class
- Maintain realistic risk-factor relationships
- Approximately 50/50 distribution

### 8. Validation
- 100 rows, 20 columns, correct column order
- Patient IDs P001–P100, no duplicates
- All categorical values in valid set
- All numeric values in valid range
- No missing values

### 9. Visualization
- 13 individual charts + 1 dashboard
- High-resolution PNG files (200+ DPI)
- Modern, clean styling

### 10. CSV Output
- Final dataset: `data/synthetic/synthetic_heart_disease_100.csv`
- No index column, no missing values
- Ready for ML training

### 11. Kaggle Upload
- Dataset metadata JSON
- Kaggle README
- Upload via CLI
