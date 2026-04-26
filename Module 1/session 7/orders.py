import pandas as pd

df = pd.read_csv("orders.csv")

print("shape:", df.shape)
print(df.head(3))
print(df.info())
# info() shows non-null counts: e.g. city 4/5, amount 4/5 — one missing in each.

df_ny = df[df["city"] == "New York"]

df_high = df[df["amount"].notna() & (df["amount"] > 60)]

df_sorted = df.sort_values(by="amount", ascending=False, na_position="first").reset_index(
    drop=True
)

print("nulls per column:\n", df.isna().sum())

df_imputed = df.copy()
mean_amount = df_imputed["amount"].mean()  # excludes NaN by default
df_imputed["amount"] = df_imputed["amount"].fillna(mean_amount)
df_imputed["city"] = df_imputed["city"].fillna("Unknown")

df_dropped = df.dropna(subset=["amount"])
