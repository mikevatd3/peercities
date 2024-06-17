from pathlib import Path
import logging
import pandas as pd
import numpy as np
from scipy.stats import zscore

import seaborn as sn
import matplotlib.pyplot as plt

from src.model import weighted_distances, select_n_closest, apply_scale
from src.app_logger import setup_logging
from src.datastructure import (
    engineered_variables,
    category_counts,
    VARIABLE_CATEGORIES,
)


logger = logging.getLogger("peer_cities")


def prepare_cbsa_name(name):
    return name.replace(" ", "_").replace("-", "_").replace(",", "").lower()


def single_run_through():
    cbsas = pd.read_csv(
        Path.cwd() / "prepped" / "1980" / "cbsas_engineered.csv",
        dtype={"cbsa_code": "str"},
    )

    weights = np.ones(VARIABLE_CATEGORIES).reshape(1, -1)

    """
    weights = np.array(
        [
            1,  # population (log-scaled)
            1,  # climate
            1,  # age distribution
            1,  # income distribution
            1,  # job sector distribution
            1,  # job sector diversity
        ]
    ).reshape(1, -1)
    """

    cbsas[engineered_variables] = cbsas[engineered_variables].fillna(
        cbsas[engineered_variables].mean(axis=0)
    )

    observations = cbsas[engineered_variables].values

    zscores = zscore(observations)
    scaled_z_scores = apply_scale(zscores, weights, category_counts)
    distances = weighted_distances(scaled_z_scores)
    closest = select_n_closest(distances).sum(axis=2)

    logger.info("Distances calculated, saving output.")
    np.savetxt(
        Path.cwd() / "model_output" / "equal_weight_output_20240614.csv",
        closest.astype("int"),
        delimiter=",",
        fmt="%i",
    )


def monte_carlo() -> None:
    BATCH_SIZE = 10
    BATCHES = 1000

    cbsas = pd.read_csv(
        Path.cwd() / "prepped" / "1980" / "cbsas_engineered.csv",
        dtype={"cbsa_code": "str"},
    )
    cbsas[engineered_variables] = cbsas[engineered_variables].fillna(
        cbsas[engineered_variables].mean(axis=0)
    )

    observations = cbsas[engineered_variables].values
    zscores = zscore(observations)

    result = np.zeros((observations.shape[0], observations.shape[0]))
    for batch in range(1, BATCHES + 1):
        logger.info(f"Beginning batch {batch}")

        weights = np.random.uniform(size=(BATCH_SIZE, VARIABLE_CATEGORIES))
        logger.info(f"Batch {batch} random weights:\n{np.round(weights, 6)}")

        scaled_z_scores = apply_scale(zscores, weights, category_counts)
        distances = weighted_distances(scaled_z_scores)

        result = result + select_n_closest(distances).sum(axis=2)

        logger.info(f"Ended batch {batch}")

    logger.info("Batches are complete saving output.")
    np.savetxt(
        Path.cwd() / "model_output" / "monte_carlo_output_20240615.csv",
        result.astype("int"),
        delimiter=",",
        fmt="%i",
    )


def summarize_results():
    df = pd.read_csv(
        Path.cwd() / "model_output" / "monte_carlo_output_20240615.csv",
        header=None,
    )
    print(np.log(df + 1).describe())
    # sn.histplot(.loc["mean"])
    # plt.show()


def main() -> None:
    setup_logging()
    # single_run_through()
    # monte_carlo()
    summarize_results()


if __name__ == "__main__":
    main()
