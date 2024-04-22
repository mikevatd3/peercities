from pathlib import Path
import pandas as pd
# from scipy.stats import entropy

from datastructure import engineered_variables

cbsas = pd.read_csv(
    Path.cwd() / "prepped" / "1980" / "cbsa_details_1980.csv",
    dtype={"cbsa_code": "str", "cbsa_title": "str"},
)


# Variables for percent calculations

commute_universe = cbsas[
    [
        "commute_lt_5",
        "commute_5_to_9",
        "commute_10_to_14",
        "commute_15_to_20",
        "commute_20_to_29",
        "commute_30_to_44",
        "commute_45_to_59",
        "commute_gt_60",  # 8
    ]
].sum(axis=1)

age_universe = cbsas[
    [
        "age_lt_1",
        "age_1_to_2",
        "age_3_to_4",
        "age_5",
        "age_6",
        "age_7_to_9",
        "age_10_to_13",
        "age_14",
        "age_15",
        "age_16",
        "age_17",
        "age_18",
        "age_19",
        "age_20",
        "age_21",
        "age_22_to_24",
        "age_25_to_29",
        "age_30_to_34",
        "age_35_to_44",
        "age_45_to_54",
        "age_55_to_59",
        "age_60_to_61",
        "age_62_to_64",
        "age_65_to_74",
        "age_75_to_84",
        "age_ge_85",  # 27
    ]
].sum(axis=1)

income_universe = cbsas[
    [
        "inc_lt_2500",
        "inc_2500_4999",
        "inc_5000_7499",
        "inc_7500_9999",
        "inc_10000_12499",
        "inc_12500_14999",
        "inc_15000_17499",
        "inc_17500_19999",
        "inc_20000_22499",
        "inc_22500_24999",
        "inc_25000_27499",
        "inc_27500_29999",
        "inc_30000_34999",
        "inc_35000_39999",
        "inc_40000_49999",
        "inc_50000_74999",
        "inc_ge_75000",
    ]
].sum(axis=1)


industry_universe = cbsas[
    [
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
        "public_admin",  # 15
    ]
].sum(axis=1)


cbsas.assign(
    pct_commute_lt_15=lambda df: df[
        [
            "commute_lt_5",
            "commute_5_to_9",
            "commute_10_to_14",
        ]
    ].sum(axis=1)
    / commute_universe,
    pct_commute_15_to_44=lambda df: df[
        [
            "commute_10_to_14",
            "commute_15_to_20",
            "commute_20_to_29",
            "commute_30_to_44",
        ]
    ].sum(axis=1)
    / commute_universe,
    pct_commute_ge_45=lambda df: df[
        [
            "commute_45_to_59",
            "commute_gt_60",
        ]
    ].sum(axis=1)
    / commute_universe,
    min_ave_monthy_temp=lambda df: df[
        [
            "jan_ave_temp",
            "feb_ave_temp",
            "mar_ave_temp",
            "apr_ave_temp",
            "may_ave_temp",
            "june_ave_temp",
            "july_ave_temp",
            "aug_ave_temp",
            "sept_ave_temp",
            "oct_ave_temp",
            "nov_ave_temp",
            "dec_ave_temp",
        ]
    ].min(axis=1),
    max_ave_monthy_temp=lambda df: df[
        [
            "jan_ave_temp",
            "feb_ave_temp",
            "mar_ave_temp",
            "apr_ave_temp",
            "may_ave_temp",
            "june_ave_temp",
            "july_ave_temp",
            "aug_ave_temp",
            "sept_ave_temp",
            "oct_ave_temp",
            "nov_ave_temp",
            "dec_ave_temp",
        ]
    ].max(axis=1),
    min_ave_monthy_precip=lambda df: df[
        [
            "jan_precip",
            "feb_precip",
            "mar_precip",
            "apr_precip",
            "may_precip",
            "june_precip",
            "july_precip",
            "aug_precip",
            "sept_precip",
            "oct_precip",
            "nov_precip",
            "dec_precip",
        ]
    ].min(axis=1),
    max_ave_monthy_precip=lambda df: df[
        [
            "jan_precip",
            "feb_precip",
            "mar_precip",
            "apr_precip",
            "may_precip",
            "june_precip",
            "july_precip",
            "aug_precip",
            "sept_precip",
            "oct_precip",
            "nov_precip",
            "dec_precip",
        ]
    ].max(axis=1),
    pct_age_lt_10=lambda df: df[
        [
            "age_lt_1",
            "age_1_to_2",
            "age_3_to_4",
            "age_5",
            "age_6",
            "age_7_to_9",
        ]
    ].sum(axis=1)
    / age_universe,
    pct_age_10_to_19=lambda df: df[
        [
            "age_10_to_13",
            "age_14",
            "age_15",
            "age_16",
            "age_17",
            "age_18",
            "age_19",
        ]
    ].sum(axis=1)
    / age_universe,
    pct_age_20_to_29=lambda df: df[
        [
            "age_20",
            "age_21",
            "age_22_to_24",
            "age_25_to_29",
            "age_30_to_34",
        ]
    ].sum(axis=1)
    / age_universe,
    pct_age_35_to_54=lambda df: df[
        [
            "age_35_to_44",
            "age_45_to_54",
        ]
    ].sum(axis=1)
    / age_universe,
    pct_age_55_to_64=lambda df: df[
        [
            "age_55_to_59",
            "age_60_to_61",
            "age_62_to_64",
        ]
    ].sum(axis=1)
    / age_universe,
    pct_age_ge_65=lambda df: df[
        [
            "age_65_to_74",
            "age_75_to_84",
            "age_ge_85",
        ]
    ].sum(axis=1) / age_universe,
    low_inc=lambda df: df[
        [
            "inc_lt_2500",
            "inc_2500_4999",
            "inc_5000_7499",
            "inc_7500_9999",
            "inc_10000_12499",
            "inc_12500_14999",
        ]
    ].sum(axis=1) / income_universe,
    mid_inc=lambda df: df[
        [
            "inc_15000_17499",
            "inc_17500_19999",
            "inc_20000_22499",
            "inc_22500_24999",
            "inc_25000_27499",
            "inc_27500_29999",
        ]
    ].sum(axis=1) / income_universe,
    hi_inc=lambda df: df[
        [
            "inc_30000_34999",
            "inc_35000_39999",
            "inc_40000_49999",
            "inc_50000_74999",
            "inc_ge_75000",
        ]
    ].sum(axis=1) / income_universe,
    labor=lambda df: df[
        [
            "ag_forestry_fish_mining",
            "construction",
            "manufacturing_nondurable",
            "manufacturing_durable",
            "comms_and_util",
        ]
    ].sum(axis=1) / industry_universe,
    life_qual=lambda df: df[
        [
            "personal_entertainment_and_rec",
            "educational_services",
            "retail_trade",
            "health_services",
        ]
    ].sum(axis=1) / industry_universe,
    biz_financial=lambda df: df[
        [
            "other_pro_services",
            "public_admin",  # 15
            "finance_insurance_realestate",
            "business_repair",
            "wholesale_trade",
        ]
    ].sum(axis=1) / industry_universe,
)[["cbsa_code", "cbsa_title"] + engineered_variables].to_csv(
    Path.cwd() / "prepped" / "1980" / "cbsas_engineered.csv", index=False
)
