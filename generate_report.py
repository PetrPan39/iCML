__znacka__ = 'generate_report'
__description__ = 'TODO: Add description here'


import json

def generate_report(data, file_path="report.json"):
    """
    Generuje report z dat ve formátu JSON.
    :param data: Data k zahrnutí do reportu.
    :param file_path: Cesta k uložení reportu.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    return f"Report uložen na {file_path}"


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'