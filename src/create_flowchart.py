"""
create_flowchart.py
-------------------
Creates the data pipeline flowchart image using matplotlib.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os


def create_flowchart():
    """Create the data pipeline flowchart."""
    
    fig, ax = plt.subplots(figsize=(14, 18))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 20)
    ax.axis('off')
    fig.patch.set_facecolor('white')
    
    # Title
    ax.text(5, 19.3, 'Heart Disease Synthetic Dataset', 
            ha='center', va='center', fontsize=18, fontweight='bold', color='#1a237e')
    ax.text(5, 18.8, 'Data Pipeline Workflow', 
            ha='center', va='center', fontsize=14, color='#555')
    
    # Define boxes
    boxes = [
        (5, 17.5, 'Original Kaggle Dataset\nBRFSS 2015\n(253,680 records)', '#E3F2FD', '#1565C0'),
        (5, 15.8, 'Data Inspection\nShape, columns, types\nMissing values, duplicates', '#E8EAF6', '#283593'),
        (5, 14.1, 'Risk-Factor Reference\nDistribution analysis\nPattern identification', '#F3E5F5', '#6A1B9A'),
        (5, 12.4, 'Synthetic Patient Generation\n100 patients × 20 features\nProbabilistic generation', '#E8F5E9', '#2E7D32'),
        (5, 10.7, 'Risk Score Calculation\nMulti-factor scoring\nSigmoid transformation', '#FFF3E0', '#E65100'),
        (5, 9.0, 'Target Generation\nHeart_Disease label\nProbabilistic assignment', '#FCE4EC', '#C62828'),
        (5, 7.3, 'Rebalancing\n~50/50 distribution\n45-55 per class', '#FFF8E1', '#F57F17'),
        (5, 5.6, 'Validation\nAll checks PASS\n100 rows, 20 cols', '#E0F2F1', '#00695C'),
        (3, 3.6, 'Visualization\n14 charts + dashboard\nPNG output', '#F3E5F5', '#6A1B9A'),
        (7, 3.6, 'CSV Output\n100 rows, 20 columns\nFinal dataset', '#E8F5E9', '#2E7D32'),
        (5, 1.8, 'Kaggle Upload\nmetadata.json\nREADME_KAGGLE.md', '#E3F2FD', '#1565C0'),
    ]
    
    # Draw boxes
    for x, y, text, facecolor, edgecolor in boxes:
        bbox = dict(boxstyle='round,pad=0.5', facecolor=facecolor, edgecolor=edgecolor, linewidth=2)
        ax.text(x, y, text, ha='center', va='center', fontsize=10,
                bbox=bbox, fontweight='normal', color='#333')
    
    # Draw arrows
    arrow_style = dict(arrowstyle='->', color='#555', linewidth=2, mutation_scale=15)
    
    # Vertical arrows
    for y_start, y_end in [(17.1, 16.2), (15.4, 14.5), (13.7, 12.8), 
                            (12.0, 11.1), (10.3, 9.4), (8.6, 7.7), (6.9, 6.0)]:
        ax.annotate('', xy=(5, y_end), xytext=(5, y_start),
                    arrowprops=arrow_style)
    
    # Split arrows
    ax.annotate('', xy=(3, 4.0), xytext=(5, 5.2),
                arrowprops=arrow_style)
    ax.annotate('', xy=(7, 4.0), xytext=(5, 5.2),
                arrowprops=arrow_style)
    
    # Merge arrows
    ax.annotate('', xy=(5, 2.2), xytext=(3, 3.2),
                arrowprops=arrow_style)
    ax.annotate('', xy=(5, 2.2), xytext=(7, 3.2),
                arrowprops=arrow_style)
    
    plt.tight_layout()
    
    output_path = os.path.join('docs', 'data_pipeline.png')
    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Flowchart saved to: {output_path}")


if __name__ == "__main__":
    create_flowchart()
