from pathlib import Path
import datetime
import pandas as pd
import numpy as np

from datastructure import engineered_variables, scale


today = datetime.datetime.today().strftime("%Y%m%d")
cbsas = pd.read_csv(
    Path.cwd() / "prepped" / "1980" / "cbsas_engineered.csv",
    dtype={"cbsa_code": "str"},
)

# This is a stop-gap before figuring out missing counties from some CBSAs
cbsas[engineered_variables] = cbsas[engineered_variables].fillna(
    cbsas[engineered_variables].mean(axis=0)
)


indentifiers = cbsas[["cbsa_code", "cbsa_title"]]
variables = cbsas[engineered_variables].values

residuals = variables - variables.mean(axis=0)
std_deviation = np.sqrt(
    (residuals * residuals).sum(axis=0) / residuals.shape[0]
)

scaled_z_scores = (residuals / std_deviation) * scale

comparisons = np.linalg.norm(
    scaled_z_scores[:, np.newaxis, :] - scaled_z_scores, axis=2
).argsort(axis=1)


def prepare_cbsa_name(name):
    return name.replace(" ", "_").replace("-", "_").replace(",", "").lower()


for row in comparisons:
    if prepare_cbsa_name(cbsas.iloc[row[0], 1]).endswith("mi"):
        cbsas.iloc[row[:11], :3].to_csv(
            Path.cwd()
            / "model_output"
            / f"{prepare_cbsa_name(cbsas.iloc[row[0], 1])}.csv",
            index=False,
        )
