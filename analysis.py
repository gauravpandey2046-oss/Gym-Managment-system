import pandas as pd
import matplotlib.pyplot as plt

def analyze_admissions():
    # 1. Dataset Load Karein aur Error Handling
    try:
        df = pd.read_csv('admissions.csv')
    except FileNotFoundError:
        print("Error: 'admissions.csv' file nahi mili. Kripya file name check karein.")
        return

    print("==========================================")
    print("   COLLEGE ADMISSION DATA ANALYSIS SYSTEM ")
    print("==========================================")
    
    # Dataset Summary
    print("\n[INFO] First 5 Rows of Dataset:")
    print(df.head())

    # 2. Total Applications and Admissions by Branch
    branch_summary = df.groupby('Branch')[['Applications', 'Admitted']].sum()
    print("\n[INFO] Branch-wise Summary:")
    print(branch_summary)

    # 3. Matplotlib Subplots (Professional Multi-Chart Layout)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Chart 1: Branch-wise Applications vs Admitted
    branch_summary.plot(kind='bar', ax=axes[0], color=['#4C72B0', '#55A868'], edgecolor='black')
    axes[0].set_title('Applications vs Admitted by Branch', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Branch', fontsize=10)
    axes[0].set_ylabel('Count', fontsize=10)
    axes[0].set_xticklabels(branch_summary.index, rotation=0)
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)

    # Chart 2: Category-wise Total Applications (Pie Chart)
    category_apps = df.groupby('Category')['Applications'].sum()
    category_apps.plot(kind='pie', ax=axes[1], autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
    axes[1].set_title('Applications Distribution by Category', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('')  # Remove y-label for clean look

    # Layout Adjust aur Show Karein
    plt.tight_layout()
    print("\n[INFO] Generating Professional Visualizations...")
    plt.show()

if __name__ == "__main__":
    analyze_admissions()