from pathlib import Path
from scipy.stats import zscore
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt


identifiers = [
    "state_code",
    "county_code",
]


all_industries = [
    "ag_forestry_fish_mining",
    "construction",
    "manufacturing_nondurable",
    "manufacturing_durable",
    "transportation",
    "comms_and_util",
    "wholesale_trade",
    "retail_trade",
    "finance_insurance_realestate",
    "business_repair",
    "personal_entertainment_and_rec",
    "health_services",
    "educational_services",
    "other_pro_services",
    "public_admin",
]


df = pd.read_csv(Path.cwd() / "prepped" / "1980" / "industry.csv")


maxxed = df[identifiers].assign(
    total_employed=lambda df: df.sum(axis=1),
    max_ind=lambda df: df.div(
            df.sum(axis=1), 
            axis=0
        ).max(axis=1)
)

print(maxxed.iloc[(-1*maxxed["max_ind"]).argsort()])



"""
test_group = df[some_industries] / df[some_industries].sum(axis=0)
test_group = test_group[np.abs(zscore(test_group) < 1).all(axis=1)]
g = sn.PairGrid(test_group)
g.map_upper(sn.scatterplot)
g.map_diag(sn.kdeplot)
g.map_lower(sn.kdeplot)

plt.show()
"""
