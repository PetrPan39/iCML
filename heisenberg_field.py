__znacka__ = 'heisenberg_field'
__description__ = 'TODO: Add description here'


import numpy as np

def heisenberg_uncertainty(position_uncertainty, momentum_uncertainty):
    """
    Kontroluje splnění Heisenbergova principu neurčitosti.
    :param position_uncertainty: Nejistota polohy (v metrech).
    :param momentum_uncertainty: Nejistota hybnosti (v kg*m/s).
    :return: True, pokud splňuje Heisenbergův princip, jinak False.
    """
    PLANCK_CONSTANT = 6.62607015e-34  # Planckova konstanta (m^2 kg / s)
    return position_uncertainty * momentum_uncertainty >= PLANCK_CONSTANT / (4 * np.pi)


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'