# transformations.py

import numpy as np
import pandas as pd

def matrix_to_vectors(input_matrix):
    input_matrix = input_matrix.stack()
    # Create arrays for x, y, and values
    x = input_matrix.index.get_level_values(0).to_numpy()  # Row indices
    y = input_matrix.index.get_level_values(1).to_numpy()  # Column indices
    values = input_matrix.to_numpy()  # Values

    tensors = np.array([x, y, values]).T
    return tensors