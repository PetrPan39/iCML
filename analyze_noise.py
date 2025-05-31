__znacka__ = 'analyze_noise'
__description__ = 'TODO: Add description here'


import numpy as np

def analyze_noise(data):
    """
    Analyzuje šum v datech.
    :param data: Sekvence dat.
    :return: Metriky šumu (např. průměrná odchylka, směrodatná odchylka).
    """
    mean_noise = np.mean(data - np.mean(data))
    std_noise = np.std(data)
    return {"mean_noise": mean_noise, "std_noise": std_noise}


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'