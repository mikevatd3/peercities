import os
from pathlib import Path
import pandas as pd


"""
This script opens the raw downloads from NHGIS and NOAA and saves everything
to the county level.
"""


raw_dir = Path.cwd() / "raw"
prepped_dir = Path.cwd() / "prepped" / "1980"

df = pd.read_csv(raw_dir / "nhgis0015_csv" / "nhgis0015_ds110_1980_county.csv")

df[["STATEA", "STATE", "COUNTYA", "COUNTY", "DR7001", "DR7002"]].rename(
    columns={
        "STATEA": "state_code",
        "STATE": "state",
        "COUNTYA": "county_code",
        "COUNTY": "county",
        "DR7001": "worked_35_plus",
        "DR7002": "worked_1_to_34_hours",
    }
).assign(
    state_code=lambda df: df["state_code"].apply(lambda s: f"{s:02}"),
    county_code=lambda df: df["county_code"].apply(lambda s: f"{s:03}"),
).to_csv(
    prepped_dir / "work_hours.csv", index=False
)


df = pd.read_csv(raw_dir / "nhgis0015_csv" / "nhgis0015_ds107_1980_county.csv")


df[
    [
        "STATEA",
        "COUNTYA",
        "DHD001",
        "DHD002",
        "DHD003",
        "DHD004",
        "DHD005",
        "DHD006",
        "DHE001",
        "DHE002",
        "DHE003",
        "DHE004",
        "DHE005",
        "DHE006",
        "DHE007",
        "DHE008",
    ]
].rename(
    columns={
        "STATEA": "state_code",
        "COUNTYA": "county_code",
        "DHD001": "car_truck_or_van__drive_alone",
        "DHD002": "car_truck_or_van__carpool",
        "DHD003": "public_transportation",
        "DHD004": "walked_only",
        "DHD005": "other_means",
        "DHD006": "worked_at_home",
        "DHE001": "commute_lt_5",
        "DHE002": "commute_5_to_9",
        "DHE003": "commute_10_to_14",
        "DHE004": "commute_15_to_20",
        "DHE005": "commute_20_to_29",
        "DHE006": "commute_30_to_44",
        "DHE007": "commute_45_to_59",
        "DHE008": "commute_gt_60",
    }
).assign(
    state_code=lambda df: df["state_code"].apply(lambda s: f"{s:02}"),
    county_code=lambda df: df["county_code"].apply(lambda s: f"{s:03}"),
).to_csv(
    prepped_dir / "transport_commute.csv", index=False
)

df = pd.read_csv(raw_dir / "nhgis0015_csv" / "nhgis0015_ds104_1980_county.csv")

df[
    [
        "STATEA",
        "COUNTYA",
        "C67001",
        "C67002",
        "C67003",
        "C67004",
        "C67005",
        "C67006",
        "C67007",
        "C67008",
        "C67009",
        "C67010",
        "C67011",
        "C67012",
        "C67013",
        "C67014",
        "C67015",
        "C67016",
        "C67017",
        "C67018",
        "C67019",
        "C67020",
        "C67021",
        "C67022",
        "C67023",
        "C67024",
        "C67025",
        "C67026",
    ]
].rename(
    columns={
        "STATEA": "state_code",
        "COUNTYA": "county_code",
        "C67001": "age_lt_1",
        "C67002": "age_1_to_2",
        "C67003": "age_3_to_4",
        "C67004": "age_5",
        "C67005": "age_6",
        "C67006": "age_7_to_9",
        "C67007": "age_10_to_13",
        "C67008": "age_14",
        "C67009": "age_15",
        "C67010": "age_16",
        "C67011": "age_17",
        "C67012": "age_18",
        "C67013": "age_19",
        "C67014": "age_20",
        "C67015": "age_21",
        "C67016": "age_22_to_24",
        "C67017": "age_25_to_29",
        "C67018": "age_30_to_34",
        "C67019": "age_35_to_44",
        "C67020": "age_45_to_54",
        "C67021": "age_55_to_59",
        "C67022": "age_60_to_61",
        "C67023": "age_62_to_64",
        "C67024": "age_65_to_74",
        "C67025": "age_75_to_84",
        "C67026": "age_gt_85",
    }
).assign(
    state_code=lambda df: df["state_code"].apply(lambda s: f"{s:02}"),
    county_code=lambda df: df["county_code"].apply(lambda s: f"{s:03}"),
).to_csv(
    prepped_dir / "age_brackets.csv", index=False
)


df = pd.read_csv(raw_dir / "nhgis0016_csv" / "nhgis0016_ds107_1980_county.csv")

df[
    [
        "STATEA",
        "COUNTYA",
        "DIA001",
        "DIA002",
        "DIA003",
        "DIA004",
        "DIA005",
        "DIA006",
        "DIA007",
        "DIA008",
        "DIA009",
        "DIA010",
        "DIA011",
        "DIA012",
        "DIA013",
        "DIA014",
        "DIA015",
    ]
].rename(
    columns={
        "STATEA": "state_code",
        "COUNTYA": "county_code",
        "DIA001": "ag_forestry_fish_mining",
        "DIA002": "construction",
        "DIA003": "manufacturing_nondurable",
        "DIA004": "manufacturing_durable",
        "DIA005": "transportation",
        "DIA006": "comms_and_util",
        "DIA007": "wholesale_trade",
        "DIA008": "retail_trade",
        "DIA009": "finance_insurance_realestate",
        "DIA010": "business_repair",
        "DIA011": "personal_entertainment_and_rec",
        "DIA012": "health_services",
        "DIA013": "educational_services",
        "DIA014": "other_pro_services",
        "DIA015": "public_admin",
    }
).assign(
    state_code=lambda df: df["state_code"].apply(lambda s: f"{s:02}"),
    county_code=lambda df: df["county_code"].apply(lambda s: f"{s:03}"),
).to_csv(
    prepped_dir / "industry.csv", index=False
)


df[
    [
        "STATEA",
        "COUNTYA",
        "DIA001",
        "DIA002",
        "DIA003",
        "DIA004",
        "DIA005",
        "DIA006",
        "DIA007",
        "DIA008",
        "DIA009",
        "DIA010",
        "DIA011",
        "DIA012",
        "DIA013",
        "DIA014",
        "DIA015",
    ]
].rename(
    columns={
        "STATEA": "state_code",
        "COUNTYA": "county_code",
        "DIA001": "ag_forestry_fish_mining",
        "DIA002": "construction",
        "DIA003": "manufacturing_nondurable",
        "DIA004": "manufacturing_durable",
        "DIA005": "transportation",
        "DIA006": "comms_and_util",
        "DIA007": "wholesale_trade",
        "DIA008": "retail_trade",
        "DIA009": "finance_insurance_realestate",
        "DIA010": "business_repair",
        "DIA011": "personal_entertainment_and_rec",
        "DIA012": "health_services",
        "DIA013": "educational_services",
        "DIA014": "other_pro_services",
        "DIA015": "public_admin",
    }
).assign(
    state_code=lambda df: df["state_code"].apply(lambda s: f"{s:02}"),
    county_code=lambda df: df["county_code"].apply(lambda s: f"{s:03}"),
).to_csv(
    prepped_dir / "industry.csv", index=False
)

df = pd.read_csv(raw_dir / "nhgis0014_csv" / "nhgis0014_ds104_1980_county.csv")

df[["STATEA", "COUNTYA", "C7L001", "C75001",]].rename(
    columns={
        "STATEA": "state_code",
        "COUNTYA": "county_code",
        "C7L001": "persons",
        "C75001": "households",
    }
).assign(
    state_code=lambda df: df["state_code"].apply(lambda s: f"{s:02}"),
    county_code=lambda df: df["county_code"].apply(lambda s: f"{s:03}"),
).to_csv(
    prepped_dir / "population.csv", index=False
)


# This file is how we get to fips from ncdc ids
county_ncdc_cross = pd.read_csv(raw_dir / "counties_crosswalk.csv", dtype=str)
county_ncdc_cross["state_code"] = county_ncdc_cross["POSTAL_FIPS_ID"].apply(
    lambda val: f"{val:>05}"[:2]
)
county_ncdc_cross["county_code"] = county_ncdc_cross["POSTAL_FIPS_ID"].apply(
    lambda val: f"{val:>05}"[2:]
)
county_ncdc_cross["state_ncdc"] = county_ncdc_cross["NCDC_FIPS_ID"].apply(
    lambda val: f"{val:>05}"[:2]
)
county_ncdc_cross["county_ncdc"] = county_ncdc_cross["NCDC_FIPS_ID"].apply(
    lambda val: f"{val:>05}"[2:]
)

# Average temerature and precipitation years over these
study_years = {
    "1971",
    "1972",
    "1973",
    "1974",
    "1975",
    "1976",
    "1977",
    "1978",
    "1979",
    "1980",
}


value_cols = [
    "jan_value",
    "feb_value",
    "mar_value",
    "apr_value",
    "may_value",
    "june_value",
    "july_value",
    "aug_value",
    "sept_value",
    "oct_value",
    "nov_value",
    "dec_value",
]


df = (
    (
        pd.read_csv(raw_dir / "ave_temps.csv", dtype=str)
        .astype({col: float for col in value_cols})
        .rename(
            columns={
                "state_code": "state_ncdc",
                "division_number": "county_ncdc",
                "jan_value": "jan_ave_temp",
                "feb_value": "feb_ave_temp",
                "mar_value": "mar_ave_temp",
                "apr_value": "apr_ave_temp",
                "may_value": "may_ave_temp",
                "june_value": "june_ave_temp",
                "july_value": "july_ave_temp",
                "aug_value": "aug_ave_temp",
                "sept_value": "sept_ave_temp",
                "oct_value": "oct_ave_temp",
                "nov_value": "nov_ave_temp",
                "dec_value": "dec_ave_temp",
            }
        )
        .merge(county_ncdc_cross, on=["state_ncdc", "county_ncdc"])
        .query("year in @study_years")
        .groupby(["state_code", "county_code"])
        .agg(
            {
                "state_code": "first",
                "county_code": "first",
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
            }
        )
    )
    .assign(
        state_code=lambda df: df["state_code"].apply(lambda s: f"{s:02}"),
        county_code=lambda df: df["county_code"].apply(lambda s: f"{s:03}"),
    )
    .to_csv(prepped_dir / "temperature.csv")
)


df = (
    (
        pd.read_csv(Path.cwd() / "raw" / "precip.csv", dtype=str)
        .astype({col: float for col in value_cols})
        .rename(
            columns={
                "state_code": "state_ncdc",
                "division_number": "county_ncdc",
                "jan_value": "jan_precip",
                "feb_value": "feb_precip",
                "mar_value": "mar_precip",
                "apr_value": "apr_precip",
                "may_value": "may_precip",
                "june_value": "june_precip",
                "july_value": "july_precip",
                "aug_value": "aug_precip",
                "sept_value": "sept_precip",
                "oct_value": "oct_precip",
                "nov_value": "nov_precip",
                "dec_value": "dec_precip",
            }
        )
        .merge(county_ncdc_cross, on=["state_ncdc", "county_ncdc"])
        .query("year in @study_years")
        .groupby(["state_code", "county_code"])
        .agg(
            {
                "state_code": "first",
                "county_code": "first",
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
            }
        )
    )
    .assign(
        state_code=lambda df: df["state_code"].apply(lambda s: f"{s:02}"),
        county_code=lambda df: df["county_code"].apply(lambda s: f"{s:03}"),
    )
    .to_csv(prepped_dir / "precipitation.csv", index=False)
)

compiled_filename = "counties_with_details_1980.csv"


df = pd.concat(
    [
        pd.read_csv(prepped_dir / item, dtype=str).set_index(
            ["state_code", "county_code"]
        )
        for item in os.listdir(prepped_dir)
        if item != compiled_filename
    ],
    axis=1,
)

df.to_csv(prepped_dir / compiled_filename)
