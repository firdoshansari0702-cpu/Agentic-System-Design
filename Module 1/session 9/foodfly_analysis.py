import pandas as pd

# 1. Dataset Setup
orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105, 106],
    "RestaurantID": ["R01", "R02", "R01", "R03", "R02", "R04"],
    "CustomerName": ["Ananya", "Rohit", "Priya", "Dev", "Sara", "Meera"],
    "Amount": [450, 320, 560, 180, 290, 720]
})

restaurants = pd.DataFrame({
    "RestaurantID": ["R01", "R02", "R03", "R05"],
    "RestaurantName": ["Spice Garden", "The Grill House", "Curry Corner", "Pasta Palace"],
    "City": ["Delhi", "Mumbai", "Delhi", "Bengaluru"]
})

# --- Step 1 & 2: Merge and Clean ---
# I used an 'inner' join because the instructions require excluding 
# unmatched orders (R04) and restaurants with no orders (R05).
merged_df = pd.merge(orders, restaurants, on="RestaurantID", how="inner")
print("Merged DataFrame:\n", merged_df)

cleaned_df = merged_df.drop(columns=["RestaurantID"]).rename(columns={
    "Amount": "Revenue",
    "RestaurantName": "Restaurant"
})
print("\nCleaned DataFrame:\n", cleaned_df)

# --- Step 3: Single Method-Chaining Pipeline ---
city_report = (
    pd.merge(orders, restaurants, on="RestaurantID", how="inner")
    .groupby("City")
    .agg(
        Total_Revenue=("Amount", "sum"),
        Order_Count=("OrderID", "count")
    )
    .reset_index()
    .sort_values(by="Total_Revenue", ascending=False)
)

print("\nCity-Wise Report:\n", city_report)

# --- Step 4: Interpret the Output ---
# 1. Which city generated the highest total revenue, and what was the amount?
# Answer: Delhi generated the highest total revenue with an amount of 1190.

# 2. Why does Pasta Palace (R05, Bengaluru) not appear in the report?
# Answer: It does not appear because it has no matching records in the orders table, and an inner join excludes unmatched keys from the right table.

# 3. Why does Order 106 (R04) not appear in the report?
# Answer: Order 106 is excluded because its RestaurantID (R04) does not exist in the restaurants table.