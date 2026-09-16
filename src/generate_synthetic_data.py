"""
generate_synthetic_data.py
-------------------------
Generates exactly 100 synthetic patient records with realistic
risk-factor relationships for heart disease prediction.
Uses probabilistic risk scoring instead of hard rules.
"""

import pandas as pd
import numpy as np
import os

# Fixed random seed for reproducibility
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# Number of patients to generate
NUM_PATIENTS = 100


def generate_patient(pid):
    """Generate a single synthetic patient record with realistic relationships."""
    
    # --- Basic demographics ---
    age = int(np.random.uniform(25, 81))
    sex = np.random.choice([0, 1], p=[0.45, 0.55])
    
    # --- Lifestyle factors ---
    # Smoking is more common in males and varies by age
    smoking_prob = 0.30 if sex == 1 else 0.20
    if age > 55:
        smoking_prob += 0.05
    smoking = np.random.choice([0, 1], p=[1 - smoking_prob, smoking_prob])
    
    # Diabetes influenced by age and BMI
    diabetes_prob = 0.10
    if age > 50:
        diabetes_prob += 0.10
    if age > 65:
        diabetes_prob += 0.05
    diabetes = np.random.choice([0, 1], p=[1 - diabetes_prob, diabetes_prob])
    
    # Family history - some genetic predisposition
    family_history = np.random.choice([0, 1], p=[0.60, 0.40])
    
    # Physical activity - inversely related to age somewhat
    activity_probs = [0.25, 0.40, 0.35]  # Low, Moderate, High
    if age > 60:
        activity_probs = [0.35, 0.40, 0.25]
    if age > 70:
        activity_probs = [0.45, 0.35, 0.20]
    physical_activity = np.random.choice([0, 1, 2], p=activity_probs)
    
    # --- BMI ---
    # Influenced by age, smoking, physical activity
    bmi_base = np.random.normal(27, 4)
    if physical_activity == 0:  # Low activity
        bmi_base += 2
    elif physical_activity == 2:  # High activity
        bmi_base -= 1.5
    if age > 50:
        bmi_base += 1
    bmi = round(np.clip(bmi_base, 18, 40), 1)
    
    # --- Blood Pressure ---
    # Influenced by age, BMI, diabetes, smoking
    bp_base = 110 + (age - 40) * 0.5
    if bmi > 30:
        bp_base += 8
    if diabetes == 1:
        bp_base += 5
    if smoking == 1:
        bp_base += 4
    if physical_activity == 2:
        bp_base -= 5
    resting_bp = int(np.clip(bp_base + np.random.normal(0, 10), 90, 200))
    
    # --- Cholesterol ---
    # Influenced by age, BMI, diabetes, physical activity
    chol_base = 180 + (age - 40) * 0.8
    if bmi > 30:
        chol_base += 15
    if diabetes == 1:
        chol_base += 10
    if physical_activity == 0:
        chol_base += 10
    elif physical_activity == 2:
        chol_base -= 10
    cholesterol = int(np.clip(chol_base + np.random.normal(0, 25), 120, 400))
    
    # --- Fasting Blood Sugar ---
    # Strongly influenced by diabetes
    if diabetes == 1:
        fasting_bs = np.random.choice([0, 1], p=[0.30, 0.70])
    else:
        fasting_bs = np.random.choice([0, 1], p=[0.85, 0.15])
    
    # --- Resting ECG ---
    # More abnormal with age and risk factors
    ecg_probs = [0.50, 0.35, 0.15]
    if age > 55:
        ecg_probs = [0.35, 0.40, 0.25]
    if age > 70:
        ecg_probs = [0.25, 0.40, 0.35]
    resting_ecg = np.random.choice([0, 1, 2], p=ecg_probs)
    
    # --- Max Heart Rate ---
    # Inversely related to age (roughly 220 - age is max expected)
    max_hr_base = 205 - (age * 0.7)
    if smoking == 1:
        max_hr_base -= 8
    if physical_activity == 2:
        max_hr_base += 5
    max_heart_rate = int(np.clip(max_hr_base + np.random.normal(0, 12), 100, 210))
    
    # --- Chest Pain Type ---
    # More concerning patterns at higher risk
    chest_pain_probs = [0.30, 0.25, 0.25, 0.20]
    if age > 60:
        chest_pain_probs = [0.20, 0.20, 0.25, 0.35]
    chest_pain_type = np.random.choice([0, 1, 2, 3], p=chest_pain_probs)
    
    # --- Exercise-Induced Angina ---
    # More common at higher risk
    angina_prob = 0.20
    if chest_pain_type == 3:
        angina_prob += 0.15
    if age > 55:
        angina_prob += 0.10
    if resting_ecg > 0:
        angina_prob += 0.05
    exercise_angina = np.random.choice([0, 1], p=[1 - min(angina_prob, 0.70), min(angina_prob, 0.70)])
    
    # --- ST Depression ---
    # Higher with angina and abnormal ECG
    st_dep_base = np.random.uniform(0, 1.5)
    if exercise_angina == 1:
        st_dep_base += np.random.uniform(1.0, 2.5)
    if resting_ecg > 0:
        st_dep_base += 0.5
    st_depression = round(np.clip(st_dep_base, 0, 6), 1)
    
    # --- ST Slope ---
    # Related to ST depression and risk
    if st_depression > 3:
        slope_probs = [0.50, 0.40, 0.10]
    elif st_depression > 1.5:
        slope_probs = [0.25, 0.50, 0.25]
    else:
        slope_probs = [0.15, 0.30, 0.55]
    st_slope = np.random.choice([0, 1, 2], p=slope_probs)
    
    # --- Num Major Vessels ---
    # More vessels colored with higher risk
    vessel_probs = [0.60, 0.25, 0.10, 0.05]
    if age > 60:
        vessel_probs = [0.45, 0.30, 0.15, 0.10]
    if smoking == 1 and diabetes == 1:
        vessel_probs = [0.35, 0.30, 0.20, 0.15]
    num_vessels = np.random.choice([0, 1, 2, 3], p=vessel_probs)
    
    # --- Thalassemia ---
    thal_probs = [0.55, 0.20, 0.25]
    if exercise_angina == 1:
        thal_probs = [0.35, 0.25, 0.40]
    thalassemia = np.random.choice([0, 1, 2], p=thal_probs)
    
    # --- Calculate Probabilistic Risk Score ---
    risk_score = 0.0
    
    # Age contribution (0-1)
    risk_score += (age - 25) / 55 * 0.15
    
    # Sex contribution
    if sex == 1:
        risk_score += 0.05
    
    # BMI contribution
    if bmi > 30:
        risk_score += 0.08
    elif bmi > 25:
        risk_score += 0.04
    
    # Smoking contribution
    if smoking == 1:
        risk_score += 0.08
    
    # Diabetes contribution
    if diabetes == 1:
        risk_score += 0.07
    
    # Family history
    if family_history == 1:
        risk_score += 0.05
    
    # Physical activity (inverse)
    if physical_activity == 0:
        risk_score += 0.06
    elif physical_activity == 2:
        risk_score -= 0.04
    
    # Blood pressure
    if resting_bp > 140:
        risk_score += 0.08
    elif resting_bp > 130:
        risk_score += 0.04
    
    # Cholesterol
    if cholesterol > 280:
        risk_score += 0.07
    elif cholesterol > 240:
        risk_score += 0.03
    
    # Fasting blood sugar
    if fasting_bs == 1:
        risk_score += 0.04
    
    # Resting ECG
    if resting_ecg == 2:
        risk_score += 0.06
    elif resting_ecg == 1:
        risk_score += 0.03
    
    # Max heart rate (inverse - lower is worse)
    if max_heart_rate < 130:
        risk_score += 0.06
    elif max_heart_rate < 150:
        risk_score += 0.03
    
    # Chest pain type
    if chest_pain_type == 3:
        risk_score += 0.07
    elif chest_pain_type == 0:
        risk_score += 0.03
    
    # Exercise angina
    if exercise_angina == 1:
        risk_score += 0.06
    
    # ST depression
    if st_depression > 3:
        risk_score += 0.07
    elif st_depression > 1.5:
        risk_score += 0.03
    
    # ST slope
    if st_slope == 0:
        risk_score += 0.05
    
    # Major vessels
    if num_vessels >= 2:
        risk_score += 0.07
    elif num_vessels == 1:
        risk_score += 0.03
    
    # Thalassemia
    if thalassemia == 2:
        risk_score += 0.06
    elif thalassemia == 1:
        risk_score += 0.03
    
    # Add some random noise
    risk_score += np.random.normal(0, 0.05)
    
    # Clip risk score between 0 and 1
    risk_score = np.clip(risk_score, 0, 1)
    
    # Convert to probability using sigmoid-like transformation
    # This makes the boundary more natural
    probability = 1 / (1 + np.exp(-8 * (risk_score - 0.45)))
    
    # Generate target
    heart_disease = np.random.choice([0, 1], p=[1 - probability, probability])
    
    # Build the record
    record = {
        "Patient_ID": f"P{pid:03d}",
        "Age": age,
        "Sex": sex,
        "Chest_Pain_Type": chest_pain_type,
        "Resting_BP": resting_bp,
        "Cholesterol": cholesterol,
        "Fasting_Blood_Sugar": fasting_bs,
        "Resting_ECG": resting_ecg,
        "Max_Heart_Rate": max_heart_rate,
        "Exercise_Induced_Angina": exercise_angina,
        "ST_Depression": st_depression,
        "ST_Slope": st_slope,
        "Num_Major_Vessels": num_vessels,
        "Thalassemia": thalassemia,
        "BMI": bmi,
        "Smoking": smoking,
        "Diabetes": diabetes,
        "Family_History": family_history,
        "Physical_Activity": physical_activity,
        "Heart_Disease": heart_disease
    }
    
    return record


def rebalance_dataset(df, target_col="Heart_Disease", target_range=(45, 55)):
    """
    Re-generate patients until target distribution is approximately 50/50.
    Tries up to 50 iterations.
    """
    best_df = df.copy()
    best_diff = abs(df[target_col].sum() - (len(df) - df[target_col].sum()))
    
    for iteration in range(50):
        count_1 = df[target_col].sum()
        count_0 = len(df) - count_1
        
        if target_range[0] <= count_1 <= target_range[1] and target_range[0] <= count_0 <= target_range[1]:
            return df
        
        # Regenerate the record with highest absolute risk score for the minority class
        # to try to balance
        if count_1 < count_0:
            # Need more positives - find a negative with high risk potential
            for idx in df[df[target_col] == 0].index:
                # Regenerate this patient
                new_record = generate_patient(df.loc[idx, "Patient_ID"])
                # Force higher risk
                new_record["Heart_Disease"] = 1
                for col in df.columns:
                    df.loc[idx, col] = new_record[col]
                count_1 = df[target_col].sum()
                count_0 = len(df) - count_1
                if count_1 >= target_range[0]:
                    break
        else:
            # Need more negatives
            for idx in df[df[target_col] == 1].index:
                new_record = generate_patient(df.loc[idx, "Patient_ID"])
                new_record["Heart_Disease"] = 0
                for col in df.columns:
                    df.loc[idx, col] = new_record[col]
                count_1 = df[target_col].sum()
                count_0 = len(df) - count_1
                if count_0 >= target_range[0]:
                    break
        
        # Check if this iteration is better
        diff = abs(count_1 - count_0)
        if diff < best_diff:
            best_diff = diff
            best_df = df.copy()
    
    return best_df


def generate_dataset():
    """Generate the complete synthetic dataset of 100 patients."""
    
    print("=" * 60)
    print("SYNTHETIC DATA GENERATION")
    print("=" * 60)
    
    # Reset random seed for reproducibility
    np.random.seed(RANDOM_SEED)
    
    # Generate all patients
    records = []
    for i in range(1, NUM_PATIENTS + 1):
        record = generate_patient(i)
        records.append(record)
    
    # Create DataFrame
    df = pd.DataFrame(records)
    
    # Rebalance to get approximately 50/50 distribution
    print("\nRebalancing dataset for ~50/50 target distribution...")
    df = rebalance_dataset(df)
    
    # Ensure exactly 100 rows
    df = df.head(NUM_PATIENTS)
    
    # Reset Patient_ID to ensure P001-P100
    df["Patient_ID"] = [f"P{i:03d}" for i in range(1, NUM_PATIENTS + 1)]
    df = df.reset_index(drop=True)
    
    # Print summary
    print(f"\nGenerated {len(df)} patient records")
    print(f"\nTarget Distribution:")
    print(f"  Heart Disease = 1: {df['Heart_Disease'].sum()}")
    print(f"  Heart Disease = 0: {(df['Heart_Disease'] == 0).sum()}")
    
    print(f"\nBasic Statistics:")
    print(f"  Average Age: {df['Age'].mean():.1f}")
    print(f"  Average BMI: {df['BMI'].mean():.1f}")
    print(f"  Average Cholesterol: {df['Cholesterol'].mean():.1f}")
    print(f"  Average Resting BP: {df['Resting_BP'].mean():.1f}")
    print(f"  Smoking %: {(df['Smoking'].sum() / len(df) * 100):.1f}%")
    print(f"  Diabetes %: {(df['Diabetes'].sum() / len(df) * 100):.1f}%")
    
    # Save to CSV
    output_path = os.path.join("data", "synthetic", "synthetic_heart_disease_100.csv")
    df.to_csv(output_path, index=False)
    print(f"\nDataset saved to: {output_path}")
    print("=" * 60)
    
    return df


if __name__ == "__main__":
    generate_dataset()
