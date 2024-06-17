from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt


df = pd.read_csv(Path.cwd() / "prepped" / "1980" / "cbsas_engineered.csv")

fig, (ax_t, ax_b) = plt.subplots(2, 1)


sn.histplot(df["persons"], ax=ax_t)
sn.histplot(np.log(df["persons"].rename("log_persons")), ax=ax_b)

plt.show()
