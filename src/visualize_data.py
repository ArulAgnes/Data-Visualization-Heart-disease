"""
visualize_data.py
----------------
Creates visualizations for the synthetic heart disease dataset.
Generates PNG files in outputs/images/.
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for modern, clean plots
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# Color palette
COLORS = ['#2196F3', '#FF5722', '#4CAF50', '#FFC107', '#9C27B0']
DPI = 200


def load_data():
    """Load the synthetic dataset."""
    csv_path = os.path.join("data", "synthetic", "synthetic_heart_disease_100.csv")
    return pd.read_csv(csv_path)


def create_01_distribution(df):
    """Heart Disease Distribution bar chart."""
    fig, ax = plt.subplots(figsize=(8, 5))
    
    counts = df['Heart_Disease'].value_counts().sort_index()
    labels = ['No Heart Disease', 'Heart Disease']
    bars = ax.bar(labels, counts.values, color=[COLORS[0], COLORS[2]], 
                  edgecolor='white', linewidth=1.5, width=0.6)
    
    for bar, count in zip(bars, counts.values):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                str(count), ha='center', va='bottom', fontweight='bold', fontsize=13)
    
    ax.set_title('Heart Disease Distribution', fontweight='bold', pad=15)
    ax.set_ylabel('Number of Patients')
    ax.set_ylim(0, max(counts.values) + 8)
    sns.despine()
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '01_heart_disease_distribution.png'), dpi=DPI)
    plt.close()


def create_02_age_dist(df):
    """Age Distribution histogram."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    sns.histplot(data=df, x='Age', hue='Heart_Disease', bins=15, 
                 palette=[COLORS[0], COLORS[2]], edgecolor='white', 
                 linewidth=0.8, alpha=0.7, ax=ax)
    
    ax.set_title('Age Distribution by Heart Disease Status', fontweight='bold', pad=15)
    ax.set_xlabel('Age (years)')
    ax.set_ylabel('Count')
    ax.legend(['Heart Disease', 'No Heart Disease'], loc='upper right')
    sns.despine()
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '02_age_distribution.png'), dpi=DPI)
    plt.close()


def create_03_by_sex(df):
    """Heart Disease by Sex."""
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ct = pd.crosstab(df['Sex'], df['Heart_Disease'], normalize='index') * 100
    ct.columns = ['No Heart Disease', 'Heart Disease']
    ct.index = ['Female (0)', 'Male (1)']
    
    ct.plot(kind='bar', ax=ax, color=[COLORS[0], COLORS[2]], edgecolor='white', 
            linewidth=1.5, width=0.6)
    
    ax.set_title('Heart Disease by Sex', fontweight='bold', pad=15)
    ax.set_ylabel('Percentage (%)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.legend(title='Status')
    sns.despine()
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '03_heart_disease_by_sex.png'), dpi=DPI)
    plt.close()


def create_04_by_smoking(df):
    """Heart Disease by Smoking Status."""
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ct = pd.crosstab(df['Smoking'], df['Heart_Disease'], normalize='index') * 100
    ct.columns = ['No Heart Disease', 'Heart Disease']
    ct.index = ['Non-Smoker (0)', 'Smoker (1)']
    
    ct.plot(kind='bar', ax=ax, color=[COLORS[0], COLORS[2]], edgecolor='white',
            linewidth=1.5, width=0.6)
    
    ax.set_title('Heart Disease by Smoking Status', fontweight='bold', pad=15)
    ax.set_ylabel('Percentage (%)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.legend(title='Status')
    sns.despine()
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '04_heart_disease_by_smoking.png'), dpi=DPI)
    plt.close()


def create_05_by_diabetes(df):
    """Heart Disease by Diabetes Status."""
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ct = pd.crosstab(df['Diabetes'], df['Heart_Disease'], normalize='index') * 100
    ct.columns = ['No Heart Disease', 'Heart Disease']
    ct.index = ['No Diabetes (0)', 'Diabetes (1)']
    
    ct.plot(kind='bar', ax=ax, color=[COLORS[0], COLORS[2]], edgecolor='white',
            linewidth=1.5, width=0.6)
    
    ax.set_title('Heart Disease by Diabetes Status', fontweight='bold', pad=15)
    ax.set_ylabel('Percentage (%)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.legend(title='Status')
    sns.despine()
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '05_heart_disease_by_diabetes.png'), dpi=DPI)
    plt.close()


def create_06_by_activity(df):
    """Heart Disease by Physical Activity."""
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ct = pd.crosstab(df['Physical_Activity'], df['Heart_Disease'], normalize='index') * 100
    ct.columns = ['No Heart Disease', 'Heart Disease']
    ct.index = ['Low (0)', 'Moderate (1)', 'High (2)']
    
    ct.plot(kind='bar', ax=ax, color=[COLORS[0], COLORS[2]], edgecolor='white',
            linewidth=1.5, width=0.6)
    
    ax.set_title('Heart Disease by Physical Activity Level', fontweight='bold', pad=15)
    ax.set_ylabel('Percentage (%)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.legend(title='Status')
    sns.despine()
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '06_heart_disease_by_physical_activity.png'), dpi=DPI)
    plt.close()


def create_07_bmi(df):
    """BMI Distribution."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    sns.histplot(data=df, x='BMI', hue='Heart_Disease', bins=12,
                 palette=[COLORS[0], COLORS[2]], edgecolor='white',
                 linewidth=0.8, alpha=0.7, ax=ax)
    
    ax.set_title('BMI Distribution by Heart Disease Status', fontweight='bold', pad=15)
    ax.set_xlabel('BMI (kg/m²)')
    ax.set_ylabel('Count')
    ax.legend(['Heart Disease', 'No Heart Disease'], loc='upper right')
    sns.despine()
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '07_bmi_distribution.png'), dpi=DPI)
    plt.close()


def create_08_cholesterol(df):
    """Cholesterol Distribution."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    sns.histplot(data=df, x='Cholesterol', hue='Heart_Disease', bins=12,
                 palette=[COLORS[0], COLORS[2]], edgecolor='white',
                 linewidth=0.8, alpha=0.7, ax=ax)
    
    ax.set_title('Cholesterol Distribution by Heart Disease Status', fontweight='bold', pad=15)
    ax.set_xlabel('Cholesterol (mg/dL)')
    ax.set_ylabel('Count')
    ax.legend(['Heart Disease', 'No Heart Disease'], loc='upper right')
    sns.despine()
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '08_cholesterol_distribution.png'), dpi=DPI)
    plt.close()


def create_09_bp(df):
    """Resting Blood Pressure Distribution."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    sns.histplot(data=df, x='Resting_BP', hue='Heart_Disease', bins=12,
                 palette=[COLORS[0], COLORS[2]], edgecolor='white',
                 linewidth=0.8, alpha=0.7, ax=ax)
    
    ax.set_title('Resting Blood Pressure Distribution', fontweight='bold', pad=15)
    ax.set_xlabel('Resting BP (mmHg)')
    ax.set_ylabel('Count')
    ax.legend(['Heart Disease', 'No Heart Disease'], loc='upper right')
    sns.despine()
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '09_resting_bp_distribution.png'), dpi=DPI)
    plt.close()


def create_10_max_hr(df):
    """Max Heart Rate Distribution."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    sns.histplot(data=df, x='Max_Heart_Rate', hue='Heart_Disease', bins=12,
                 palette=[COLORS[0], COLORS[2]], edgecolor='white',
                 linewidth=0.8, alpha=0.7, ax=ax)
    
    ax.set_title('Maximum Heart Rate Distribution', fontweight='bold', pad=15)
    ax.set_xlabel('Max Heart Rate (bpm)')
    ax.set_ylabel('Count')
    ax.legend(['Heart Disease', 'No Heart Disease'], loc='upper right')
    sns.despine()
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '10_max_heart_rate_distribution.png'), dpi=DPI)
    plt.close()


def create_11_st_dep(df):
    """ST Depression Distribution."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    sns.histplot(data=df, x='ST_Depression', hue='Heart_Disease', bins=15,
                 palette=[COLORS[0], COLORS[2]], edgecolor='white',
                 linewidth=0.8, alpha=0.7, ax=ax)
    
    ax.set_title('ST Depression Distribution', fontweight='bold', pad=15)
    ax.set_xlabel('ST Depression')
    ax.set_ylabel('Count')
    ax.legend(['Heart Disease', 'No Heart Disease'], loc='upper right')
    sns.despine()
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '11_st_depression_distribution.png'), dpi=DPI)
    plt.close()


def create_12_correlation(df):
    """Correlation Heatmap."""
    fig, ax = plt.subplots(figsize=(14, 11))
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr = df[numeric_cols].corr()
    
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    
    sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r',
                center=0, square=True, linewidths=0.5, 
                cbar_kws={"shrink": 0.8}, ax=ax,
                annot_kws={'size': 8})
    
    ax.set_title('Feature Correlation Heatmap', fontweight='bold', pad=15, fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=9)
    plt.yticks(fontsize=9)
    
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '12_correlation_heatmap.png'), dpi=DPI)
    plt.close()


def create_13_risk_factors(df):
    """Risk Factors vs Heart Disease."""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    
    risk_factors = [
        ('Age', 'Age'),
        ('BMI', 'BMI'),
        ('Cholesterol', 'Cholesterol (mg/dL)'),
        ('Resting_BP', 'Resting BP (mmHg)'),
        ('Max_Heart_Rate', 'Max Heart Rate (bpm)'),
        ('ST_Depression', 'ST Depression')
    ]
    
    for idx, (col, label) in enumerate(risk_factors):
        row, col_idx = idx // 3, idx % 3
        ax = axes[row, col_idx]
        
        sns.boxplot(data=df, x='Heart_Disease', y=col, ax=ax,
                    palette=[COLORS[0], COLORS[2]], width=0.5)
        
        ax.set_title(f'{label} by Heart Disease', fontweight='bold', fontsize=12)
        ax.set_xticklabels(['No HD', 'HD'])
        ax.set_xlabel('')
        sns.despine(ax=ax)
    
    plt.suptitle('Risk Factors vs Heart Disease Status', fontweight='bold', 
                 fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'images', '13_risk_factors_vs_heart_disease.png'), dpi=DPI)
    plt.close()


def create_dashboard(df):
    """Create a summary dashboard image."""
    fig = plt.figure(figsize=(16, 10))
    fig.patch.set_facecolor('#f8f9fa')
    
    # Title
    fig.suptitle('Heart Disease Synthetic Dataset - Summary Dashboard',
                 fontsize=18, fontweight='bold', y=0.98)
    
    # Grid layout
    gs = fig.add_gridspec(3, 4, hspace=0.4, wspace=0.35)
    
    # --- Top row: Key metrics ---
    metric_data = [
        ('Total Patients', '100', COLORS[0]),
        ('Heart Disease', str(int(df['Heart_Disease'].sum())), COLORS[2]),
        ('No Heart Disease', str(int((df['Heart_Disease'] == 0).sum())), COLORS[0]),
        ('Avg Age', f"{df['Age'].mean():.1f} yrs", COLORS[1])
    ]
    
    for i, (label, value, color) in enumerate(metric_data):
        ax = fig.add_subplot(gs[0, i])
        ax.text(0.5, 0.6, value, ha='center', va='center', fontsize=28, fontweight='bold', color=color)
        ax.text(0.5, 0.2, label, ha='center', va='center', fontsize=10, color='#555')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        ax.add_patch(plt.Rectangle((0.05, 0.05), 0.9, 0.9, fill=True, 
                                    facecolor='white', edgecolor='#ddd', 
                                    linewidth=1.5, transform=ax.transAxes))
    
    # --- Second row: Heart Disease distribution ---
    ax1 = fig.add_subplot(gs[1, 0])
    counts = df['Heart_Disease'].value_counts().sort_index()
    ax1.pie(counts.values, labels=['No HD', 'HD'], colors=[COLORS[0], COLORS[2]],
            autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
    ax1.set_title('HD Distribution', fontweight='bold', fontsize=11)
    
    # --- Second row: BMI distribution ---
    ax2 = fig.add_subplot(gs[1, 1])
    ax2.hist(df['BMI'], bins=10, color=COLORS[1], edgecolor='white', alpha=0.8)
    ax2.set_title(f'Avg BMI: {df["BMI"].mean():.1f}', fontweight='bold', fontsize=11)
    ax2.set_xlabel('BMI')
    ax2.set_ylabel('Count')
    sns.despine(ax=ax2)
    
    # --- Second row: Cholesterol distribution ---
    ax3 = fig.add_subplot(gs[1, 2])
    ax3.hist(df['Cholesterol'], bins=10, color=COLORS[3], edgecolor='white', alpha=0.8)
    ax3.set_title(f'Avg Cholesterol: {df["Cholesterol"].mean():.0f}', fontweight='bold', fontsize=11)
    ax3.set_xlabel('Cholesterol (mg/dL)')
    ax3.set_ylabel('Count')
    sns.despine(ax=ax3)
    
    # --- Second row: Resting BP distribution ---
    ax4 = fig.add_subplot(gs[1, 3])
    ax4.hist(df['Resting_BP'], bins=10, color=COLORS[4], edgecolor='white', alpha=0.8)
    ax4.set_title(f'Avg Resting BP: {df["Resting_BP"].mean():.0f}', fontweight='bold', fontsize=11)
    ax4.set_xlabel('BP (mmHg)')
    ax4.set_ylabel('Count')
    sns.despine(ax=ax4)
    
    # --- Third row: Smoking and Diabetes pie charts ---
    ax5 = fig.add_subplot(gs[2, 0])
    smoking_counts = df['Smoking'].value_counts().sort_index()
    ax5.pie(smoking_counts.values, labels=['Non-Smoker', 'Smoker'], 
            colors=[COLORS[0], COLORS[1]], autopct='%1.1f%%', startangle=90,
            textprops={'fontsize': 9})
    ax5.set_title(f'Smoking ({df["Smoking"].sum()} smokers)', fontweight='bold', fontsize=11)
    
    ax6 = fig.add_subplot(gs[2, 1])
    diabetes_counts = df['Diabetes'].value_counts().sort_index()
    ax6.pie(diabetes_counts.values, labels=['No Diabetes', 'Diabetes'],
            colors=[COLORS[0], COLORS[2]], autopct='%1.1f%%', startangle=90,
            textprops={'fontsize': 9})
    ax6.set_title(f'Diabetes ({df["Diabetes"].sum()} diabetic)', fontweight='bold', fontsize=11)
    
    ax7 = fig.add_subplot(gs[2, 2])
    activity_counts = df['Physical_Activity'].value_counts().sort_index()
    ax7.pie(activity_counts.values, labels=['Low', 'Moderate', 'High'],
            colors=[COLORS[1], COLORS[3], COLORS[2]], autopct='%1.1f%%', startangle=90,
            textprops={'fontsize': 9})
    ax7.set_title('Physical Activity', fontweight='bold', fontsize=11)
    
    ax8 = fig.add_subplot(gs[2, 3])
    sex_counts = df['Sex'].value_counts().sort_index()
    ax8.pie(sex_counts.values, labels=['Female', 'Male'],
            colors=['#E91E63', '#2196F3'], autopct='%1.1f%%', startangle=90,
            textprops={'fontsize': 9})
    ax8.set_title('Sex Distribution', fontweight='bold', fontsize=11)
    
    plt.savefig(os.path.join('outputs', 'images', 'heart_disease_dashboard.png'), dpi=DPI, 
                bbox_inches='tight')
    plt.close()


def generate_all_visualizations():
    """Generate all visualizations."""
    print("=" * 60)
    print("VISUALIZATION GENERATION")
    print("=" * 60)
    
    df = load_data()
    print(f"Loaded dataset: {len(df)} rows, {len(df.columns)} columns")
    
    print("\nGenerating visualizations...")
    
    create_01_distribution(df)
    print("  [1/13] Heart Disease Distribution")
    
    create_02_age_dist(df)
    print("  [2/13] Age Distribution")
    
    create_03_by_sex(df)
    print("  [3/13] Heart Disease by Sex")
    
    create_04_by_smoking(df)
    print("  [4/13] Heart Disease by Smoking")
    
    create_05_by_diabetes(df)
    print("  [5/13] Heart Disease by Diabetes")
    
    create_06_by_activity(df)
    print("  [6/13] Heart Disease by Physical Activity")
    
    create_07_bmi(df)
    print("  [7/13] BMI Distribution")
    
    create_08_cholesterol(df)
    print("  [8/13] Cholesterol Distribution")
    
    create_09_bp(df)
    print("  [9/13] Resting BP Distribution")
    
    create_10_max_hr(df)
    print("  [10/13] Max Heart Rate Distribution")
    
    create_11_st_dep(df)
    print("  [11/13] ST Depression Distribution")
    
    create_12_correlation(df)
    print("  [12/13] Correlation Heatmap")
    
    create_13_risk_factors(df)
    print("  [13/13] Risk Factors vs Heart Disease")
    
    create_dashboard(df)
    print("  [Dashboard] Summary Dashboard")
    
    print(f"\nAll visualizations saved to: outputs/images/")
    print("=" * 60)


if __name__ == "__main__":
    generate_all_visualizations()
