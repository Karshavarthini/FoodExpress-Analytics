# Phase 15 - Data Science, Big Data, ML & Data Analytics

print("\n1. DATA SCIENCE")
print("Data Science uses data, programming, statistics,")
print("and machine learning to solve business problems.")

print("\n2. BIG DATA")
print("Big Data deals with very large amounts of data")
print("that may be difficult to process using traditional methods.")

print("\n3. MACHINE LEARNING")

print("Machine Learning learns patterns from historical data")
print("and uses those patterns to make predictions.")

print("\n4. DATA ANALYTICS")

print("Data Analytics examines existing data to find")
print("patterns, trends and useful business insights.")

print("\n5. MAIN DIFFERENCE")

print("Data Science  -> Solves problems using data")
print("Big Data      -> Handles very large datasets")
print("Machine Learning -> Learns patterns and predicts")
print("Data Analytics -> Analyses data to find insights")

print("\n6. BUSINESS QUESTIONS")

print("1. Which restaurant generates the highest total revenue?")
print("2. Which city has the highest number of orders?")
print("3. Does delivery distance affect order amount or delivery time?")

# PHASE 16 - DATA WRANGLING, EDA & VISUALIZATION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HAS_MATPLOTLIB = True
try:
    import matplotlib.pyplot as plt
except ImportError:
    HAS_MATPLOTLIB = False
    print("[Note] 'matplotlib' library not detected. Install via 'pip install matplotlib' to render PNG charts.")

HAS_SCIPY = True
try:
    import scipy.stats as stats
except ImportError:
    HAS_SCIPY = False
    print("[Note] 'scipy' library not detected. Install via 'pip install scipy' for Chi-Square test calculations.")

excel_filename = "orders.xlsx"

df_eda = pd.read_excel(excel_filename)

print("\n--- Loaded Data ---")
print(df_eda.head())

print("\n--- Dataset Information ---")

print("Shape:", df_eda.shape)

print("\nColumns:")
print(df_eda.columns.tolist())

print("\nMissing Values:")
print(df_eda.isnull().sum())

print("\n--- Data Wrangling ---")


# Standardize city names
df_eda["city"] = (
    df_eda["city"]
    .astype(str)
    .str.strip()
    .str.title())

df_eda["amount"] = pd.to_numeric(
    df_eda["amount"],
    errors="coerce")

if df_eda["amount"].isnull().sum() > 0:

    median_val = df_eda["amount"].median()

    df_eda["amount"] = df_eda["amount"].fillna(median_val)

    print("Missing amount values filled using median.")


print("\nCleaned City Names:")
print(df_eda["city"].unique())

orders_per_restaurant = df_eda['restaurant'].value_counts()
orders_per_city = df_eda['city'].value_counts()
min_amt, max_amt, mean_amt = df_eda['amount'].min(), df_eda['amount'].max(), df_eda['amount'].mean()

print("--- Exploratory Aggregations ---")
print(f"Order Volume per City      : {dict(orders_per_city)}")
print(f"Order Value Range (Rs.)     : Min = Rs. {min_amt}, Max = Rs. {max_amt}, Mean = Rs. {mean_amt:.2f}")

# Concept: Visualizations (Bar & Line Charts)
if HAS_MATPLOTLIB:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

    # Chart 1: Bar Chart - Orders per City
    ax1.bar(orders_per_city.index, orders_per_city.values, color=['#3498db', '#2ecc71'])
    ax1.set_title("Total Orders per City")
    ax1.set_xlabel("City")
    ax1.set_ylabel("Number of Orders")

    # Chart 2: Line Chart - Order Amount Progression
    ax2.plot(df_eda['order_id'], df_eda['amount'], marker='o', color='#e74c3c', linestyle='-')
    ax2.set_title("Order Amount Trend by Order ID")
    ax2.set_xlabel("Order ID")
    ax2.set_ylabel("Amount (Rs.)")

    plt.tight_layout()
    plt.savefig("eda_charts.png")
    plt.close()
    print("Saved Matplotlib charts to 'eda_charts.png'.")
else:
    print("[Visualization Skipped] Install 'matplotlib' to render chart output image.")

print("\n[HYPOTHESIS FORMULATION]")
print("  Null Hypothesis (H0)        : Customer City and Coupon Usage are independent.")
print("  Alternative Hypothesis (H1) : Coupon usage rates differ significantly between Hyderabad and Bangalore.")

# PHASE 17 : ADD STATISTICS ON TOP

amounts_arr = df_eda['amount'].values
n_obs = len(amounts_arr)

# Manual Descriptive Statistics Calculation vs Built-in Verification
mean_manual = sum(amounts_arr) / n_obs

sorted_amt = sorted(amounts_arr)
median_manual = (sorted_amt[n_obs//2 - 1] + sorted_amt[n_obs//2]) / 2.0 if n_obs % 2 == 0 else sorted_amt[n_obs//2]

var_manual = sum((x - mean_manual) ** 2 for x in amounts_arr) / (n_obs - 1)
std_manual = var_manual ** 0.5

print("--- Manual vs NumPy Built-in Statistics Verification ---")
print(f"Mean   | Manual: {mean_manual:.2f} | NumPy: {np.mean(amounts_arr):.2f}")
print(f"Median | Manual: {median_manual:.2f} | NumPy: {np.median(amounts_arr):.2f}")
print(f"Var    | Manual: {var_manual:.2f} | NumPy (ddof=1): {np.var(amounts_arr, ddof=1):.2f}")
print(f"StdDev | Manual: {std_manual:.2f} | NumPy (ddof=1): {np.std(amounts_arr, ddof=1):.2f}")

# Histogram Distribution Plot
if HAS_MATPLOTLIB:
    plt.figure(figsize=(6, 3.5))
    plt.hist(amounts_arr, bins=5, color='#9b59b6', edgecolor='black', alpha=0.7)
    plt.title("Order Amount Histogram")
    plt.xlabel("Amount (Rs.)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("amount_distribution.png")
    plt.close()
    print("\nSaved histogram to 'amount_distribution.png'.")

# Chi-Square Test of Independence
np.random.seed(42)
df_eda['delivery_distance'] = np.random.uniform(1.0, 8.0, len(df_eda)).round(1)
df_eda['delivery_time'] = (df_eda['delivery_distance'] * 4 + np.random.normal(10, 2, len(df_eda))).round(0)
df_eda['coupon_used'] = np.random.choice([True, False], size=len(df_eda), p=[0.45, 0.55])

contingency_table = pd.crosstab(df_eda['city'], df_eda['coupon_used'])
print("\n--- Chi-Square Contingency Table (City vs Coupon Used) ---")
print(contingency_table)

if HAS_SCIPY:
    chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)
    print(f"Chi2 Statistic: {chi2:.4f} | p-value: {p_val:.4f}")
    if p_val < 0.05:
        print("Conclusion: Reject H0 -> Significant difference in coupon usage by city.")
    else:
        print("Conclusion: Fail to reject H0 -> No significant difference in coupon usage by city.")
else:
    print("[SciPy Skipped] Install 'scipy' to execute scipy.stats.chi2_contingency calculation.")

# Correlation Matrix
corr_matrix = df_eda[['amount', 'delivery_distance', 'delivery_time']].corr()
print("\n--- Correlation Matrix ---")
print(corr_matrix.round(3))

# PHASE 18 : REBUILD THE NUMERIC CORE IN NUMPY

# ndarray creation, shape, dtype, ndim
daily_order_counts = np.array([45, 62, 38, 75, 50, 88, 92, 41, 55, 68, 72, 30, 95, 80, 60, 52, 48, 70, 85, 90], dtype=np.int32)
print(f"NumPy Array: {daily_order_counts}")
print(f"Array Shape: {daily_order_counts.shape} | Data Type: {daily_order_counts.dtype} | Dimensions: {daily_order_counts.ndim}")

# Slicing & Boolean Masking
high_volume_days = daily_order_counts[daily_order_counts > 50]
print(f"\nDays with > 50 orders (Boolean Indexing): {high_volume_days}")

# Copy vs View Memory Demonstration
arr_orig = np.array([10, 20, 30, 40, 50])
view_demo = arr_orig[1:4]
view_demo[0] = 999  # Mutates original array!
print(f"\nMutated View -> Original array modified: {arr_orig}")

copy_demo = arr_orig[1:4].copy()
copy_demo[0] = -777 # Does NOT mutate original array!
print(f"Mutated Copy -> Original array stays unchanged: {arr_orig}")

# 2D Reshaping, ufuncs, and Broadcasting
matrix_2d = daily_order_counts.reshape(4, 5)
print("\n--- 2D Restaurant Order Matrix (4 restaurants x 5 days) ---")
print(matrix_2d)

# Universal Function: 10% festival boost
festival_boosted = matrix_2d * 1.10

# Broadcasting
bonus_per_restaurant = np.array([[5], [10], [15], [20]])  # Shape (4, 1)
broadcasted_scores = festival_boosted + bonus_per_restaurant

print("\nBoosted & Broadcasted Matrix (with festival bonus per restaurant):")
print(np.round(broadcasted_scores, 1))

# Matrix Multiplication (Linear Algebra for Weighted Performance Score)
weights = np.array([0.3, 0.25, 0.2, 0.15, 0.1])  # 5-day weight factors
weighted_scores = np.dot(broadcasted_scores, weights)  # Matrix multiplication (@ operator)

print("\n--- Final Weighted Performance Score per Restaurant (NumPy Matrix Math) ---")
for idx, score in enumerate(weighted_scores, 1):
    print(f"  * Restaurant #{idx}: Score = {score:.2f}")

# PHASE 19 : FINISH IT IN PANDAS

df_final = pd.read_csv("orders.csv")
df_final['date'] = pd.date_range(start="2026-09-01", periods=len(df_final), freq="D")
print("\n--- Final Dataset ---")
print(df_final.head())

# Series Creation indexed by order_id
amount_series = pd.Series(df_final['amount'].values, index=df_final['order_id'], name="OrderAmount")
print("Pandas Series (First 5 orders indexed by Order ID):")
print(amount_series.head())

# Data Selection using .loc and .iloc
print("\n--- Selection using .loc (Hyderabad Orders > Rs. 400) ---")
hyd_orders = df_final.loc[(df_final['city'] == 'Hyderabad') & (df_final['amount'] > 400), ['order_id', 'restaurant', 'amount']]
print(hyd_orders.to_string(index=False))

print("\n--- Selection using .iloc (First 5 Rows, Cols 1 to 3) ---")
print(df_final.iloc[0:5, 1:4].to_string(index=False))

# Missing Data Handling (dropna vs fillna median imputation)
df_dirty = df_final.copy()
df_dirty.loc[2, 'amount'] = np.nan  # Inject sample NaNs

# dropna removes rows completely
df_dropped = df_dirty.dropna()

# fillna imputes NaNs using group-level median
df_dirty['amount'] = df_dirty.groupby('restaurant')['amount'].transform(lambda x: x.fillna(x.median()))

print(f"\nMissing Data Treatment -> Row count dropna(): {len(df_dropped)} | Row count fillna(): {len(df_dirty)}")
# Concept: Final Ranked Deliverable Table (groupby & aggregate)
final_ranked_table = df_final.groupby('restaurant').agg(
    total_revenue=('amount', 'sum'),
    average_order_value=('amount', 'mean'),
    order_count=('order_id', 'count')
).reset_index()

# Sort highest to lowest revenue
final_ranked_table = final_ranked_table.sort_values(by='total_revenue', ascending=False)

deliverable_filename = "foodexpress_final_deliverable.csv"
final_ranked_table.to_csv(deliverable_filename, index=False)

print("\n" + "="*80)
print("             FOODEXPRESS FINAL RANKED DELIVERABLE TABLE                   ")
print("="*80)
print(final_ranked_table.to_string(index=False))
print("="*80)
print(f"SUCCESS! Deliverable exported to '{deliverable_filename}'.")
