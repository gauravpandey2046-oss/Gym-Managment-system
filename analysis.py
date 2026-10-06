import pandas as pd
import matplotlib.pyplot as plt

try:
    # Load the dataset
    df = pd.read_csv("admissions.csv")
    print("Dataset Loaded Successfully!\n")
    print(df.head())

    # Group data by Branch and sum applications
    branch_data = df.groupby("Branch")["Applications"].sum()

    # Plotting the data
    branch_data.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Total College Admissions Applications by Branch")
    plt.xlabel("Branch")
    plt.ylabel("Applications")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error: {e}")