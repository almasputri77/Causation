#
# Almas, 2025/11/26
# File: Customer_Analysis.py
# Analyze Customer Data 
# 
#

import pandas as pd

# 1. Input
df = pd.read_csv("customer_data.csv")
top5 = df[
    [
        "customer_id",
        "purchase_amount",
        "purchase_frequency",
        "satisfaction_score",
        "exp_checkout_efficiency",
        "exp_online_usability",
    ]
].head()

print(top5)

print(df.shape)

# 2. Process

# 3. Output


