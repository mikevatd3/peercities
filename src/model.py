import numpy as np


def expand_weights(weights, repeats):
    """
    Takes a weights matrix that is of shape (a, b) where a is each weight
    iteration and b is the number of 'categories' in the analysis. It also
    takes a repeats list that says how many times to repeat each *column*
    of a.

    Returns a expanded weights matrix of size (1, c, a) where a is each iteration
    and c is the sum of the repeats list. Essentially returns a wider version of
    the original that will match the width of the observations matrix.
    """

    repeated = np.repeat(weights, repeats, axis=1)

    return repeated.reshape(1, repeated.shape[1], repeated.shape[0])


def cart_prod_differences(weighted_cube):
    """
    Takes a weighted cube array with size (a, b, c) where:
        a is the number of observations
        b is the number of variables
        c is the number of weight schemes

    It returns an array with size (a, a, b, c). Where each sub
    array is a collection of distance vectors from each array
    to all others under each weight scheme.
    """

    # Reshape for broadcasting
    expanded = weighted_cube[:, np.newaxis, :, :]  # Shape: (a, 1, b, d)
    expanded_rotated = weighted_cube[np.newaxis, :, :, :]  # Shape: (1, a, b, d)

    return expanded - expanded_rotated  # Shape: (a, a, b, d)


def apply_scale(
    zscores,
    weights,
    repeats,
) -> np.ndarray:
    """
    This function takes the observations matrix of size (a, b) where
        a is the number of observations and
        b is the number of variables
    weights has shape (c, d) where
        c is the number of weight instances to test in the batch
        d is the number of variable categories to weight
    repeats is a 1-dim array of the number of variables in each category
    to apply the corresponding weight to.
    """

    # Returns scale shaped to broadcast correctly with the zscores
    scale = expand_weights(weights, repeats)

    # have to add singluar depth dim to broadcast with scale
    return zscores[:, :, np.newaxis] * scale


def weighted_distances(
    scaled_z_scores: np.ndarray,
) -> np.ndarray:
    """
    Several shapes and transformations happening here:
        Arguments:
        observations has shape (a, b) where
            a is the number of observations
            b is the number of variables

        Outputs:
        distances has shape (a, a, c) where, as above,
            a is the number of observations
            c is the number of weight instances
    """
    # remember this comes out with shape (a, a, b, c)
    differences = cart_prod_differences(scaled_z_scores)

    # we use this to get down to (a, a, c)
    return np.linalg.norm(differences, axis=2)


def select_n_closest(mat, select=11):
    """
    This takes the 3d array that comes out of weighted_distances of
    size (a, a, c) where
        a is the number of observations
        c is the number of weight schemes

    and 'selects' the closest n observations in each column by placing a
    1 in those positions and a zero everywhere else. The array it returns
    is the same as the array that it is provided.
    """

    assert (
        select <= mat.shape[0]
    ), "Select parameter cannot be larger than the number of observations"

    # Get the indices of the sorted distances
    sorted_indices = np.argsort(mat, axis=1)

    # Create a result array filled with zeros
    result = np.zeros_like(mat, dtype=int)

    # Use advanced indexing to place 1s in the positions of the closest n observations
    rows = np.arange(mat.shape[0])[:, np.newaxis, np.newaxis]
    cols = np.arange(mat.shape[2])[np.newaxis, np.newaxis, :]
    closest_indices = sorted_indices[:, :select, :]

    result[rows, closest_indices, cols] = 1

    return result
