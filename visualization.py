__znacka__ = 'visualization'
__description__ = 'TODO: Add description here'


import matplotlib.pyplot as plt

def visualize_results(data, title="Výsledky optimalizace"):
    """
    Vykreslí graf výsledků optimalizace.
    :param data: Data k vizualizaci (např. hodnoty MSE).
    :param title: Název grafu.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data, marker='o', linestyle='-', label='Chyba')
    plt.title(title)
    plt.xlabel('Iterace')
    plt.ylabel('Chyba (MSE)')
    plt.grid(True)
    plt.legend()
    plt.show()


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'