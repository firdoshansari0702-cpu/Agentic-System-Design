import pandas as pd

# Step 1: Create DataFrame
projects = pd.DataFrame({
    "ProjectID": ["P01", "P02", "P03", "P04", "P05", "P06"],
    "City": ["Pune", "Pune", "Mumbai", "Mumbai", "Mumbai", "Nashik"],
    "ProjectName": ["Water", "Lights", "Clinic", "School", "Garden", "Skills"],
    "Budget_Lakh": [12.5, 8.0, 25.0, 18.5, 6.0, 9.5],
    "Volunteers": [10, 14, 22, 30, 8, 12],
    "internal_only": ["x", "x", "x", "x", "x", "x"],   # junk
    "legacy_flag": [0, 0, 0, 0, 0, 0]                # junk
})

# Step 2: Drop junk columns
projects = projects.drop(["internal_only", "legacy_flag"], axis=1)

# Step 3: Groupby report
report = projects.groupby("City").agg(
    Num_Projects=("ProjectID", "count"),
    Total_Budget_Lakh=("Budget_Lakh", "sum"),
    Avg_Volunteers=("Volunteers", "mean")
)

# Step 4: Print output
print("NGO Summary by City")
print(report)

# Step 5 (optional): Reset index
print("\nWith reset index:")
print(report.reset_index())
