__znacka__ = 'classify_equation'
__description__ = 'TODO: Add description here'


def classify_equation(equation):
    """
    Identifikuje, zda je rovnice lineární nebo nelineární.
    :param equation: Řetězec reprezentující rovnici.
    :return: Typ rovnice ('linear' nebo 'nonlinear').
    """
    if 'sin' in equation or 'cos' in equation or '**' in equation:
        return 'nonlinear'
    return 'linear'


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'