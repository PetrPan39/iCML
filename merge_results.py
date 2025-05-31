__znacka__ = 'merge_results'
__description__ = 'TODO: Add description here'


import numpy as np

def merge_results(results):
    """
    Kombinuje výsledky různých metod do jedné reprezentace.
    :param results: Seznam výsledků od různých metod.
    :return: Kombinovaný výsledek.
    """
    combined = np.mean([np.array(r) for r in results], axis=0)
    return combined.tolist()


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'