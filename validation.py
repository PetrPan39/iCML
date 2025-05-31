__znacka__ = 'validation'
__description__ = 'TODO: Add description here'


import numpy as np

def validate_numerical_array(array, name="Array"):
    """
    Kontrola, zda je vstupní data pole čísel.
    :param array: Vstupní data k validaci.
    :param name: Název pole (pro výpis chybových hlášek).
    :return: True, pokud je validní, jinak vyvolá výjimku.
    """
    if not isinstance(array, np.ndarray):
        raise ValueError(f"{name} must be a numpy array.")
    if not np.issubdtype(array.dtype, np.number):
        raise ValueError(f"{name} must contain numerical values.")
    return True


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'