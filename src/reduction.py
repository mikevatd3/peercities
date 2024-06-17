from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sn
import matplotlib.pyplot as plt

from datastructure import engineered_variables


cbsas = pd.read_csv(
    Path.cwd() / 
    "prepped" /
    "1980" /
    "cbsas_engineered.csv"
)


cbsas[engineered_variables] = cbsas[engineered_variables].fillna(
    cbsas[engineered_variables].mean(axis=0)
)

cbsas["persons"] = np.log(cbsas["persons"])


indentifiers = cbsas[["cbsa_code", "cbsa_title"]]
variables = cbsas[engineered_variables].values

residuals = variables - variables.mean(axis=0)
std_deviation = np.sqrt(
    (residuals * residuals).sum(axis=0) / residuals.shape[0]
)

scaled_z_scores = (residuals / std_deviation)


pca = PCA(n_components="mle")
model = pca.fit(cbsas[engineered_variables])
compos = model.components_


plt.figure(figsize=(16,16))

sn.heatmap(pd.DataFrame(
    np.cov(scaled_z_scores.T),
    index=engineered_variables,
    columns=engineered_variables,
))

plt.show()


"""
pd.concat([
    pd.Series(engineered_variables),
    pd.DataFrame(compos.T),
], axis=1).round(8)


for i, col in enumerate(engineered_variables):
    print(f"{col: <22}{' '.join([f'{i: 5}' for i in np.round(compos.T[i, :], 2)])}")
"""
