"""
create_linkedin_images.py
-------------------------
Creates 9 professional LinkedIn portfolio images for the Heart Disease project.
All images are 1600x900 (16:9 landscape) for LinkedIn compatibility.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import os


# Color scheme - professional blue/teal palette
DARK_BG = '#0a1628'
CARD_BG = '#1a2744'
ACCENT_BLUE = '#4fc3f7'
ACCENT_TEAL = '#26a69a'
ACCENT_ORANGE = '#ff7043'
TEXT_WHITE = '#ffffff'
TEXT_LIGHT = '#b0bec5'
TEXT_DIM = '#78909c'
GREEN = '#66bb6a'
RED = '#ef5350'


def create_01_project_cover():
    """Project cover image - 1600x900."""
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor(DARK_BG)
    
    # Decorative line
    ax.plot([1, 15], [6.5, 6.5], color=ACCENT_BLUE, linewidth=2, alpha=0.5)
    ax.plot([1, 15], [2.5, 2.5], color=ACCENT_BLUE, linewidth=2, alpha=0.5)
    
    # Title
    ax.text(8, 7.2, 'Heart Disease Prediction', ha='center', va='center',
            fontsize=42, fontweight='bold', color=TEXT_WHITE, family='sans-serif')
    
    # Subtitle
    ax.text(8, 5.5, 'Synthetic Dataset  |  Python  |  Data Visualization  |  Kaggle',
            ha='center', va='center', fontsize=18, color=ACCENT_BLUE, family='sans-serif')
    
    # Stats boxes
    stats = [('100', 'Patients'), ('20', 'Features'), ('50/50', 'Balance'), ('14', 'Charts')]
    for i, (val, label) in enumerate(stats):
        x = 2.5 + i * 3.5
        ax.add_patch(plt.Rectangle((x-1, 3.2), 2.5, 1.5, fill=True,
                                    facecolor=CARD_BG, edgecolor=ACCENT_BLUE, linewidth=1.5,
                                    alpha=0.8, transform=ax.transAxes if False else ax.transData))
        ax.text(x + 0.25, 4.3, val, ha='center', va='center', fontsize=28,
                fontweight='bold', color=ACCENT_BLUE)
        ax.text(x + 0.25, 3.6, label, ha='center', va='center', fontsize=12,
                color=TEXT_LIGHT)
    
    # Footer
    ax.text(8, 1.5, 'Arul Maria Agnes  |  Data Visualization Project',
            ha='center', va='center', fontsize=14, color=TEXT_DIM)
    
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join('linkedin', 'images', '01_project_cover.png'),
                dpi=150, bbox_inches='tight', facecolor=DARK_BG)
    plt.close()


def create_02_source_dataset():
    """Source dataset info graphic."""
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor(DARK_BG)
    
    ax.text(8, 8.2, 'Source Dataset Analysis', ha='center', va='center',
            fontsize=32, fontweight='bold', color=TEXT_WHITE)
    ax.plot([2, 14], [7.8, 7.8], color=ACCENT_BLUE, linewidth=2, alpha=0.5)
    
    # Source info cards
    info = [
        ('BRFSS 2015', 'CDC Behavioral Risk Factor\nSurveillance System'),
        ('253,680', 'Survey Records'),
        ('22', 'Health Indicators'),
        ('9.4%', 'Heart Disease\nPrevalence')
    ]
    
    for i, (val, desc) in enumerate(info):
        x = 2 + i * 3.5
        ax.add_patch(plt.Rectangle((x-1.2, 5.2), 2.8, 2.2, fill=True,
                                    facecolor=CARD_BG, edgecolor=ACCENT_TEAL, linewidth=1.5))
        ax.text(x + 0.2, 6.8, val, ha='center', va='center', fontsize=26,
                fontweight='bold', color=ACCENT_TEAL)
        ax.text(x + 0.2, 5.8, desc, ha='center', va='center', fontsize=11,
                color=TEXT_LIGHT, linespacing=1.4)
    
    ax.text(8, 4.2, 'Used as reference for realistic risk-factor patterns only',
            ha='center', va='center', fontsize=14, color=TEXT_DIM, style='italic')
    
    # Variables list
    ax.text(8, 3.2, 'Key Variables Referenced:', ha='center', va='center',
            fontsize=16, fontweight='bold', color=TEXT_WHITE)
    
    vars_text = 'BMI  |  Smoker  |  Diabetes  |  HighBP  |  HighChol  |  PhysActivity  |  Age  |  Sex'
    ax.text(8, 2.4, vars_text, ha='center', va='center', fontsize=13, color=ACCENT_BLUE)
    
    ax.text(8, 1.2, 'No records copied  |  Different clinical variables used in synthetic data',
            ha='center', va='center', fontsize=12, color=TEXT_DIM)
    
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join('linkedin', 'images', '02_source_dataset.png'),
                dpi=150, bbox_inches='tight', facecolor=DARK_BG)
    plt.close()


def create_03_synthetic_dataset():
    """Synthetic dataset overview."""
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor(DARK_BG)
    
    ax.text(8, 8.2, 'Synthetic Dataset Overview', ha='center', va='center',
            fontsize=32, fontweight='bold', color=TEXT_WHITE)
    ax.plot([2, 14], [7.8, 7.8], color=ACCENT_BLUE, linewidth=2, alpha=0.5)
    
    # Main stats
    ax.add_patch(plt.Rectangle((2, 4.5), 4.5, 2.8, fill=True,
                                facecolor=CARD_BG, edgecolor=ACCENT_BLUE, linewidth=2))
    ax.text(4.25, 6.8, '100', ha='center', va='center', fontsize=48,
            fontweight='bold', color=ACCENT_BLUE)
    ax.text(4.25, 5.5, 'Patient Records', ha='center', va='center', fontsize=16,
            color=TEXT_LIGHT)
    ax.text(4.25, 4.9, 'P001 - P100', ha='center', va='center', fontsize=13,
            color=TEXT_DIM)
    
    ax.add_patch(plt.Rectangle((9.5, 4.5), 4.5, 2.8, fill=True,
                                facecolor=CARD_BG, edgecolor=ACCENT_TEAL, linewidth=2))
    ax.text(11.75, 6.8, '20', ha='center', va='center', fontsize=48,
            fontweight='bold', color=ACCENT_TEAL)
    ax.text(11.75, 5.5, 'Clinical Features', ha='center', va='center', fontsize=16,
            color=TEXT_LIGHT)
    ax.text(11.75, 4.9, 'Including Target Variable', ha='center', va='center', fontsize=13,
            color=TEXT_DIM)
    
    # Column list
    cols = ['Patient_ID', 'Age', 'Sex', 'Chest_Pain_Type', 'Resting_BP', 'Cholesterol',
            'Fasting_Blood_Sugar', 'Resting_ECG', 'Max_Heart_Rate', 'Exercise_Induced_Angina',
            'ST_Depression', 'ST_Slope', 'Num_Major_Vessels', 'Thalassemia', 'BMI',
            'Smoking', 'Diabetes', 'Family_History', 'Physical_Activity', 'Heart_Disease']
    
    ax.text(8, 3.8, 'All 20 Columns:', ha='center', va='center',
            fontsize=14, fontweight='bold', color=TEXT_WHITE)
    
    for i in range(0, 20, 5):
        row_text = '  |  '.join(cols[i:i+5])
        ax.text(8, 3.2 - i*0.28, row_text, ha='center', va='center',
                fontsize=10, color=ACCENT_BLUE, family='monospace')
    
    ax.text(8, 1.0, 'Probabilistic risk scoring  |  No deterministic rules  |  Realistic variation',
            ha='center', va='center', fontsize=12, color=TEXT_DIM)
    
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join('linkedin', 'images', '03_synthetic_dataset.png'),
                dpi=150, bbox_inches='tight', facecolor=DARK_BG)
    plt.close()


def create_04_target_distribution():
    """Target distribution visualization."""
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor(DARK_BG)
    
    ax.text(8, 8.2, 'Target Distribution', ha='center', va='center',
            fontsize=32, fontweight='bold', color=TEXT_WHITE)
    ax.plot([2, 14], [7.8, 7.8], color=ACCENT_BLUE, linewidth=2, alpha=0.5)
    
    # Large donut chart
    sizes = [46, 54]
    colors_pie = [ACCENT_ORANGE, ACCENT_BLUE]
    wedges, texts = ax.pie(sizes, colors=colors_pie, startangle=90,
                           wedgeprops=dict(width=0.4, edgecolor=DARK_BG),
                           labels=['', ''])
    
    ax.text(0, 0.3, '100', ha='center', va='center', fontsize=36,
            fontweight='bold', color=TEXT_WHITE)
    ax.text(0, -0.2, 'Total', ha='center', va='center', fontsize=14,
            color=TEXT_LIGHT)
    
    # Labels
    ax.text(5.5, 1.5, 'Heart Disease = 1', ha='left', va='center',
            fontsize=16, color=ACCENT_ORANGE, fontweight='bold')
    ax.text(5.5, 0.7, '46 patients  (46%)', ha='left', va='center',
            fontsize=14, color=TEXT_LIGHT)
    
    ax.text(5.5, -0.5, 'Heart Disease = 0', ha='left', va='center',
            fontsize=16, color=ACCENT_BLUE, fontweight='bold')
    ax.text(5.5, -1.3, '54 patients  (54%)', ha='left', va='center',
            fontsize=14, color=TEXT_LIGHT)
    
    ax.text(8, 3.0, 'Balanced Dataset for ML Training', ha='center', va='center',
            fontsize=18, fontweight='bold', color=GREEN)
    ax.text(8, 2.3, '45-55 per class  |  No class imbalance  |  Suitable for classification',
            ha='center', va='center', fontsize=12, color=TEXT_DIM)
    
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join('linkedin', 'images', '04_target_distribution.png'),
                dpi=150, bbox_inches='tight', facecolor=DARK_BG)
    plt.close()


def create_05_correlation_heatmap():
    """Correlation heatmap with professional styling."""
    # Load data
    csv_path = os.path.join('data', 'synthetic', 'synthetic_heart_disease_100.csv')
    df = pd.read_csv(csv_path)
    
    fig, ax = plt.subplots(figsize=(16, 9))
    fig.patch.set_facecolor(DARK_BG)
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    corr = df[numeric_cols].corr()
    
    # Custom colormap
    from matplotlib.colors import LinearSegmentedColormap
    colors_cm = ['#1a237e', '#4fc3f7', '#ffffff', '#ff7043', '#b71c1c']
    cmap = LinearSegmentedColormap.from_list('custom', colors_cm, N=256)
    
    sns_heatmap = ax.imshow(corr.values, cmap=cmap, vmin=-1, vmax=1, aspect='auto')
    
    # Add correlation values (full matrix)
    for i in range(len(corr)):
        for j in range(len(corr)):
            val = corr.iloc[i, j]
            color = TEXT_WHITE if abs(val) < 0.5 else DARK_BG
            ax.text(j, i, f'{val:.2f}', ha='center', va='center', fontsize=7,
                    color=color, fontweight='bold' if abs(val) > 0.3 else 'normal')
    
    n = len(numeric_cols)
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    short_names = ['Age', 'Sex', 'CP', 'BP', 'Chol', 'FS', 'ECG',
                   'MHR', 'Ang', 'STD', 'STS', 'Ves', 'Thal', 'BMI',
                   'Smk', 'Dia', 'FH', 'PA', 'HD']
    ax.set_xticklabels(short_names[:n], rotation=45, ha='right', fontsize=9, color=TEXT_LIGHT)
    ax.set_yticklabels(short_names[:n], fontsize=9, color=TEXT_LIGHT)
    
    ax.set_title('Feature Correlation Heatmap', fontsize=20, fontweight='bold',
                 color=TEXT_WHITE, pad=20)
    
    cbar = plt.colorbar(sns_heatmap, ax=ax, shrink=0.8, fraction=0.046)
    cbar.ax.tick_params(colors=TEXT_LIGHT)
    cbar.set_label('Correlation', color=TEXT_LIGHT, fontsize=12)
    
    plt.tight_layout()
    plt.savefig(os.path.join('linkedin', 'images', '05_correlation_heatmap.png'),
                dpi=150, bbox_inches='tight', facecolor=DARK_BG)
    plt.close()


def create_06_dashboard():
    """Copy and enhance the existing dashboard for LinkedIn."""
    # Load data
    csv_path = os.path.join('data', 'synthetic', 'synthetic_heart_disease_100.csv')
    df = pd.read_csv(csv_path)
    
    fig = plt.figure(figsize=(16, 9))
    fig.patch.set_facecolor(DARK_BG)
    
    fig.suptitle('Heart Disease Synthetic Dataset - Dashboard',
                 fontsize=20, fontweight='bold', color=TEXT_WHITE, y=0.97)
    
    gs = fig.add_gridspec(3, 4, hspace=0.5, wspace=0.4, left=0.05, right=0.95, top=0.9, bottom=0.08)
    
    # Top row metrics
    metrics = [
        ('100', 'Patients', ACCENT_BLUE),
        ('46', 'Heart Disease', ACCENT_ORANGE),
        ('54', 'No Heart Disease', GREEN),
        (f"{df['Age'].mean():.0f}", 'Avg Age (yrs)', ACCENT_TEAL)
    ]
    
    for i, (val, label, color) in enumerate(metrics):
        ax = fig.add_subplot(gs[0, i])
        ax.set_facecolor(CARD_BG)
        ax.text(0.5, 0.65, val, ha='center', va='center', fontsize=32,
                fontweight='bold', color=color, transform=ax.transAxes)
        ax.text(0.5, 0.2, label, ha='center', va='center', fontsize=11,
                color=TEXT_LIGHT, transform=ax.transAxes)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        for spine in ax.spines.values():
            spine.set_edgecolor(ACCENT_BLUE)
            spine.set_linewidth(1.5)
    
    # Middle row: distributions
    ax1 = fig.add_subplot(gs[1, 0])
    ax1.set_facecolor(CARD_BG)
    counts = df['Heart_Disease'].value_counts().sort_index()
    ax1.pie(counts.values, colors=[ACCENT_BLUE, ACCENT_ORANGE],
            autopct='%1.0f%%', startangle=90, textprops={'fontsize': 9, 'color': TEXT_WHITE})
    ax1.set_title('HD Distribution', color=TEXT_WHITE, fontsize=11, fontweight='bold')
    
    ax2 = fig.add_subplot(gs[1, 1])
    ax2.set_facecolor(CARD_BG)
    ax2.hist(df['BMI'], bins=10, color=ACCENT_TEAL, edgecolor=DARK_BG, alpha=0.8)
    ax2.set_title(f'BMI (avg {df["BMI"].mean():.1f})', color=TEXT_WHITE, fontsize=11, fontweight='bold')
    ax2.tick_params(colors=TEXT_LIGHT, labelsize=8)
    for spine in ax2.spines.values(): spine.set_color(TEXT_DIM)
    
    ax3 = fig.add_subplot(gs[1, 2])
    ax3.set_facecolor(CARD_BG)
    ax3.hist(df['Cholesterol'], bins=10, color=ACCENT_ORANGE, edgecolor=DARK_BG, alpha=0.8)
    ax3.set_title(f'Cholesterol (avg {df["Cholesterol"].mean():.0f})', color=TEXT_WHITE, fontsize=11, fontweight='bold')
    ax3.tick_params(colors=TEXT_LIGHT, labelsize=8)
    for spine in ax3.spines.values(): spine.set_color(TEXT_DIM)
    
    ax4 = fig.add_subplot(gs[1, 3])
    ax4.set_facecolor(CARD_BG)
    ax4.hist(df['Resting_BP'], bins=10, color='#ab47bc', edgecolor=DARK_BG, alpha=0.8)
    ax4.set_title(f'Resting BP (avg {df["Resting_BP"].mean():.0f})', color=TEXT_WHITE, fontsize=11, fontweight='bold')
    ax4.tick_params(colors=TEXT_LIGHT, labelsize=8)
    for spine in ax4.spines.values(): spine.set_color(TEXT_DIM)
    
    # Bottom row: risk factors
    ax5 = fig.add_subplot(gs[2, 0])
    ax5.set_facecolor(CARD_BG)
    smoking_counts = df['Smoking'].value_counts().sort_index()
    ax5.pie(smoking_counts.values, colors=[GREEN, ACCENT_ORANGE],
            autopct='%1.0f%%', startangle=90, textprops={'fontsize': 9, 'color': TEXT_WHITE})
    ax5.set_title('Smoking', color=TEXT_WHITE, fontsize=11, fontweight='bold')
    
    ax6 = fig.add_subplot(gs[2, 1])
    ax6.set_facecolor(CARD_BG)
    diabetes_counts = df['Diabetes'].value_counts().sort_index()
    ax6.pie(diabetes_counts.values, colors=[GREEN, ACCENT_ORANGE],
            autopct='%1.0f%%', startangle=90, textprops={'fontsize': 9, 'color': TEXT_WHITE})
    ax6.set_title('Diabetes', color=TEXT_WHITE, fontsize=11, fontweight='bold')
    
    ax7 = fig.add_subplot(gs[2, 2])
    ax7.set_facecolor(CARD_BG)
    activity_counts = df['Physical_Activity'].value_counts().sort_index()
    ax7.pie(activity_counts.values, colors=[ACCENT_ORANGE, ACCENT_BLUE, GREEN],
            autopct='%1.0f%%', startangle=90, textprops={'fontsize': 9, 'color': TEXT_WHITE})
    ax7.set_title('Activity', color=TEXT_WHITE, fontsize=11, fontweight='bold')
    
    ax8 = fig.add_subplot(gs[2, 3])
    ax8.set_facecolor(CARD_BG)
    sex_counts = df['Sex'].value_counts().sort_index()
    ax8.pie(sex_counts.values, colors=['#e91e63', '#2196f3'],
            autopct='%1.0f%%', startangle=90, textprops={'fontsize': 9, 'color': TEXT_WHITE})
    ax8.set_title('Sex', color=TEXT_WHITE, fontsize=11, fontweight='bold')
    
    plt.savefig(os.path.join('linkedin', 'images', '06_dashboard.png'),
                dpi=150, bbox_inches='tight', facecolor=DARK_BG)
    plt.close()


def create_07_data_pipeline():
    """Data pipeline infographic."""
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor(DARK_BG)
    
    ax.text(8, 8.4, 'Data Pipeline Workflow', ha='center', va='center',
            fontsize=30, fontweight='bold', color=TEXT_WHITE)
    ax.plot([2, 14], [8.0, 8.0], color=ACCENT_BLUE, linewidth=2, alpha=0.5)
    
    steps = [
        ('BRFSS 2015\nDataset', ACCENT_BLUE),
        ('Data\nInspection', ACCENT_TEAL),
        ('Risk-Factor\nAnalysis', '#ab47bc'),
        ('Synthetic\nGeneration', GREEN),
        ('Risk Score\nCalculation', ACCENT_ORANGE),
        ('Target\nGeneration', RED),
        ('Validation\nAll PASS', GREEN),
        ('Visualization\n14 Charts', ACCENT_BLUE),
        ('Kaggle\nUpload', ACCENT_TEAL),
        ('GitHub\nPortfolio', '#ab47bc')
    ]
    
    for i, (label, color) in enumerate(steps):
        x = 0.8 + i * 1.5
        y = 5.5
        ax.add_patch(plt.Rectangle((x-0.5, y-0.6), 1.3, 1.2, fill=True,
                                    facecolor=CARD_BG, edgecolor=color, linewidth=2))
        ax.text(x + 0.15, y + 0.1, label, ha='center', va='center', fontsize=9,
                color=color, fontweight='bold', linespacing=1.3)
        
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + 1.0, y), xytext=(x + 0.9, y),
                        arrowprops=dict(arrowstyle='->', color=TEXT_DIM, lw=1.5))
    
    # Bottom labels
    ax.text(8, 3.5, 'Probabilistic  |  Reproducible  |  Validated  |  Visualized',
            ha='center', va='center', fontsize=14, color=TEXT_LIGHT)
    ax.text(8, 2.8, 'Random Seed: 42  |  100 Patients  |  20 Features  |  ~50/50 Balance',
            ha='center', va='center', fontsize=12, color=TEXT_DIM)
    
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join('linkedin', 'images', '07_data_pipeline.png'),
                dpi=150, bbox_inches='tight', facecolor=DARK_BG)
    plt.close()


def create_08_kaggle_preview():
    """Kaggle publication ready graphic."""
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor(DARK_BG)
    
    ax.text(8, 8.2, 'Kaggle Dataset Published', ha='center', va='center',
            fontsize=32, fontweight='bold', color=TEXT_WHITE)
    ax.plot([2, 14], [7.8, 7.8], color=ACCENT_BLUE, linewidth=2, alpha=0.5)
    
    # Kaggle-style card
    ax.add_patch(plt.Rectangle((3, 3.5), 10, 3.8, fill=True,
                                facecolor=CARD_BG, edgecolor=ACCENT_BLUE, linewidth=2))
    
    ax.text(8, 6.7, 'arulmariaagnes/synthetic-heart-disease-100',
            ha='center', va='center', fontsize=16, color=ACCENT_BLUE, family='monospace')
    
    ax.text(8, 5.8, 'Synthetic Heart Disease Dataset - 100 Patients',
            ha='center', va='center', fontsize=14, color=TEXT_WHITE, fontweight='bold')
    
    ax.text(8, 5.0, '100 synthetic patient records  |  20 clinical features  |  Balanced target',
            ha='center', va='center', fontsize=12, color=TEXT_LIGHT)
    
    ax.text(8, 4.2, 'Educational ML practice  |  Not real patient data  |  Not for diagnosis',
            ha='center', va='center', fontsize=11, color=TEXT_DIM, style='italic')
    
    # Status badges
    badges = [('CSV', GREEN), ('Cover Image', GREEN), ('Metadata', GREEN), ('README', GREEN)]
    for i, (label, color) in enumerate(badges):
        x = 4.5 + i * 2
        ax.add_patch(plt.Rectangle((x-0.6, 3.0), 1.5, 0.5, fill=True,
                                    facecolor=color, alpha=0.3, edgecolor=color))
        ax.text(x + 0.15, 3.25, label, ha='center', va='center', fontsize=9,
                color=color, fontweight='bold')
    
    ax.text(8, 2.0, 'Dataset URL: kaggle.com/datasets/arulmariaagnes/synthetic-heart-disease-100',
            ha='center', va='center', fontsize=12, color=TEXT_LIGHT)
    
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join('linkedin', 'images', '08_kaggle_preview.png'),
                dpi=150, bbox_inches='tight', facecolor=DARK_BG)
    plt.close()


def create_09_github_preview():
    """GitHub portfolio preview graphic."""
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor(DARK_BG)
    
    ax.text(8, 8.2, 'GitHub Portfolio Project', ha='center', va='center',
            fontsize=32, fontweight='bold', color=TEXT_WHITE)
    ax.plot([2, 14], [7.8, 7.8], color=ACCENT_BLUE, linewidth=2, alpha=0.5)
    
    # Repository card
    ax.add_patch(plt.Rectangle((2, 3.5), 12, 4.0, fill=True,
                                facecolor=CARD_BG, edgecolor=ACCENT_TEAL, linewidth=2))
    
    ax.text(8, 7.0, 'ArulAgnes / Data-Visualization-Heart-disease',
            ha='center', va='center', fontsize=16, color=ACCENT_TEAL, family='monospace')
    
    ax.text(8, 6.2, 'Heart Disease Prediction - Synthetic Dataset',
            ha='center', va='center', fontsize=14, color=TEXT_WHITE, fontweight='bold')
    
    # File tree preview
    tree = [
        'data/synthetic/synthetic_heart_disease_100.csv',
        'src/run_all.py',
        'outputs/images/ (14 visualizations)',
        'kaggle/ (dataset metadata)',
        'README.md  |  requirements.txt'
    ]
    
    for i, item in enumerate(tree):
        ax.text(8, 5.4 - i*0.4, item, ha='center', va='center',
                fontsize=11, color=TEXT_LIGHT, family='monospace')
    
    # Tech badges
    techs = [('Python', ACCENT_BLUE), ('Pandas', ACCENT_TEAL), ('Matplotlib', GREEN),
             ('Seaborn', '#ab47bc'), ('Kaggle', ACCENT_ORANGE)]
    for i, (tech, color) in enumerate(techs):
        x = 3.5 + i * 2
        ax.add_patch(plt.Rectangle((x-0.5, 3.0), 1.4, 0.5, fill=True,
                                    facecolor=color, alpha=0.3, edgecolor=color))
        ax.text(x + 0.2, 3.25, tech, ha='center', va='center', fontsize=10,
                color=color, fontweight='bold')
    
    ax.text(8, 2.0, 'github.com/ArulAgnes/Data-Visualization-Heart-disease',
            ha='center', va='center', fontsize=12, color=TEXT_LIGHT)
    
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join('linkedin', 'images', '09_github_preview.png'),
                dpi=150, bbox_inches='tight', facecolor=DARK_BG)
    plt.close()


def generate_all_linkedin_images():
    """Generate all 9 LinkedIn images."""
    print("Generating LinkedIn images...")
    
    create_01_project_cover()
    print("  [1/9] Project Cover")
    
    create_02_source_dataset()
    print("  [2/9] Source Dataset")
    
    create_03_synthetic_dataset()
    print("  [3/9] Synthetic Dataset")
    
    create_04_target_distribution()
    print("  [4/9] Target Distribution")
    
    create_05_correlation_heatmap()
    print("  [5/9] Correlation Heatmap")
    
    create_06_dashboard()
    print("  [6/9] Dashboard")
    
    create_07_data_pipeline()
    print("  [7/9] Data Pipeline")
    
    create_08_kaggle_preview()
    print("  [8/9] Kaggle Preview")
    
    create_09_github_preview()
    print("  [9/9] GitHub Preview")
    
    print("\nAll 9 LinkedIn images saved to: linkedin/images/")


if __name__ == "__main__":
    generate_all_linkedin_images()
