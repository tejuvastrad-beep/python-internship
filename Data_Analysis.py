"""
Task 3: Data Analysis with Pandas

Objective:
- Load a CSV dataset
- Clean missing values
- Filter records
- Group and aggregate data
"""

import pandas as pd

print("=" * 60)
print("        DATA ANALYSIS WITH PANDAS")
print("=" * 60)

try:
    df = pd.read_csv("students.csv")

    print("\nOriginal Dataset")
    print("-" * 40)
    print(df)

    print("\nDataset Information")
    print("-" * 40)
    df.info()

    # Fill missing marks with average marks
    average_marks = df["Marks"].mean()
    df["Marks"] = df["Marks"].fillna(average_marks)

    print("\nDataset After Cleaning")
    print("-" * 40)
    print(df)

    # Filter students scoring above 85
    print("\nStudents Scoring Above 85")
    print("-" * 40)
    high_scores = df[df["Marks"] > 85]
    print(high_scores)

    # Group by department
    print("\nAverage Marks by Department")
    print("-" * 40)
    dept_avg = df.groupby("Department")["Marks"].mean()
    print(dept_avg)

    # Statistics
    print("\nOverall Statistics")
    print("-" * 40)
    print("Highest Marks :", df["Marks"].max())
    print("Lowest Marks  :", df["Marks"].min())
    print("Average Marks :", round(df["Marks"].mean(), 2))

    # Insights
    print("\nInsights")
    print("-" * 40)
    print("1. Missing marks were replaced with the average marks.")
    print("2. Students scoring above 85 were identified.")
    print("3. Department-wise average marks were calculated.")

except FileNotFoundError:
    print("[ERROR] students.csv file not found.")

except Exception as e:
    print("[ERROR]", e)

finally:
    print("\n[SUCCESS] Program completed successfully.")