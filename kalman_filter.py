__znacka__ = 'kalman_filter'
__description__ = 'TODO: Add description here'


import numpy as np

def kalman_filter(values, process_variance=1e-5, measurement_variance=1e-1):
    """
    Implementace Kalmanova filtru pro redukci šumu.
    :param values: Sekvence vstupních dat.
    :param process_variance: Variance procesu (modelu).
    :param measurement_variance: Variance měření (dat).
    :return: Vyfiltrovaná data.
    """
    n_iter = len(values)
    xhat = np.zeros(n_iter)
    P = np.zeros(n_iter)
    xhatminus = np.zeros(n_iter)
    Pminus = np.zeros(n_iter)
    K = np.zeros(n_iter)

    xhat[0] = values[0]
    P[0] = 1.0

    for k in range(1, n_iter):
        xhatminus[k] = xhat[k - 1]
        Pminus[k] = P[k - 1] + process_variance
        K[k] = Pminus[k] / (Pminus[k] + measurement_variance)
        xhat[k] = xhatminus[k] + K[k] * (values[k] - xhatminus[k])
        P[k] = (1 - K[k]) * Pminus[k]

    return xhat


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'