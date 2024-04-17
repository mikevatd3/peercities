from pathlib import Path
import pandas as pd


"""
This file takes the counties detail file and aggregates to CBSAs.
"""


counties = pd.read_csv(
    Path.cwd() / "prepped" / "1980" / "counties_with_details_1980.csv",
    dtype={"state_code": "str", "county_code": "str"},
)

available_variables = [
    # Identification
    "state_code",
    "county_code",
    "state",
    "county",  # 4
    # Population -> add
    "persons",
    "households",  # 2
    # Hours worked -> add
    "worked_35_plus",
    "worked_1_to_34_hours",  # 2
    # Commute transport -> add
    "car_truck_or_van__drive_alone",
    "car_truck_or_van__carpool",
    "public_transportation",
    "walked_only",
    "other_means",
    "worked_at_home",  # 6
    # Commute length -> add
    "commute_lt_5",
    "commute_5_to_9",
    "commute_10_to_14",
    "commute_15_to_20",
    "commute_20_to_29",
    "commute_30_to_44",
    "commute_45_to_59",
    "commute_gt_60",  # 8
    # Industry -> add
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
    # Temperature -> mean
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
    "dec_ave_temp",  # 12
    # Precipitation -> mean
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
    "dec_precip",  # 12
    # Ages -> add
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
    "age_gt_85",  # 27
]


cbsa_crosswalk = pd.read_csv(
    Path.cwd() / "raw" / "cbsa_crosswalk.csv",
    dtype={"state_code": "str", "county_code": "str"},
)[["state_code", "county_code", "cbsa_code", "cbsa_title"]]


counties.merge(cbsa_crosswalk, on=["state_code", "county_code"]).groupby(
    "cbsa_code"
).agg(
    {
        "cbsa_title": "first",
        "persons": "sum",
        "households": "sum",
        "worked_35_plus": "sum",
        "worked_1_to_34_hours": "sum",
        "car_truck_or_van__drive_alone": "sum",
        "car_truck_or_van__carpool": "sum",
        "public_transportation": "sum",
        "walked_only": "sum",
        "other_means": "sum",
        "worked_at_home": "sum",
        "commute_lt_5": "sum",
        "commute_5_to_9": "sum", "commute_10_to_14": "sum",
        "commute_15_to_20": "sum",
        "commute_20_to_29": "sum",
        "commute_30_to_44": "sum",
        "commute_45_to_59": "sum",
        "commute_gt_60": "sum",
        "ag_forestry_fish_mining": "sum",
        "construction": "sum",
        "manufacturing_nondurable": "sum",
        "manufacturing_durable": "sum",
        "transportation": "sum",
        "comms_and_util": "sum",
        "wholesale_trade": "sum",
        "retail_trade": "sum",
        "finance_insurance_realestate": "sum",
        "business_repair": "sum",
        "personal_entertainment_and_rec": "sum",
        "health_services": "sum",
        "educational_services": "sum",
        "other_pro_services": "sum",
        "public_admin": "sum",
        "jan_ave_temp": "mean",
        "feb_ave_temp": "mean",
        "mar_ave_temp": "mean",
        "apr_ave_temp": "mean",
        "may_ave_temp": "mean",
        "june_ave_temp": "mean",
        "july_ave_temp": "mean",
        "aug_ave_temp": "mean",
        "sept_ave_temp": "mean",
        "oct_ave_temp": "mean",
        "nov_ave_temp": "mean",
        "dec_ave_temp": "mean",
        "jan_precip": "mean",
        "feb_precip": "mean",
        "mar_precip": "mean",
        "apr_precip": "mean",
        "may_precip": "mean",
        "june_precip": "mean",
        "july_precip": "mean",
        "aug_precip": "mean",
        "sept_precip": "mean",
        "oct_precip": "mean",
        "nov_precip": "mean",
        "dec_precip": "mean",
        "age_lt_1": "sum",
        "age_1_to_2": "sum",
        "age_3_to_4": "sum",
        "age_5": "sum",
        "age_6": "sum",
        "age_7_to_9": "sum",
        "age_10_to_13": "sum",
        "age_14": "sum",
        "age_15": "sum",
        "age_16": "sum",
        "age_17": "sum",
        "age_18": "sum",
        "age_19": "sum",
        "age_20": "sum",
        "age_21": "sum",
        "age_22_to_24": "sum",
        "age_25_to_29": "sum",
        "age_30_to_34": "sum",
        "age_35_to_44": "sum",
        "age_45_to_54": "sum",
        "age_55_to_59": "sum",
        "age_60_to_61": "sum",
        "age_62_to_64": "sum",
        "age_65_to_74": "sum",
        "age_75_to_84": "sum",
        "age_gt_85": "sum",
    }
).to_csv(Path.cwd() / "prepped" / "1980" / "cbsa_details_1980.csv")
