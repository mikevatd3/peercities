from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
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


indentifiers = cbsas[["cbsa_code", "cbsa_title"]]
variables = cbsas[engineered_variables].values

residuals = variables - variables.mean(axis=0)
std_deviation = np.sqrt(
    (residuals * residuals).sum(axis=0) / residuals.shape[0]
)

scaled_z_scores = (residuals / std_deviation)


pca = PCA(
    n_components="mle"
)

compos = pca.fit(cbsas[engineered_variables]).components_

print(compos.shape)

for i, col in enumerate(engineered_variables):
    print(f"{col: <22}{' '.join([f'{i: 6}' for i in np.round(compos.T[i, :], 3)])}")


