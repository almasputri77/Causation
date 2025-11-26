#
# Almas, 2025/11/26
# File: Customer_Analysis.py
# Analyze Customer Data 
# 
#

import pandas as pd

# 1. Input
df = pd.read_csv("customer_data.csv")

summary = df[
    ["purchase_amount", "purchase_frequency", "satisfaction_score"]
    ].describe().loc[["count", "mean", "std", "min", "max"]]
summary

print(summary)

# 2. Process

# 3. Output


