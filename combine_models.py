__znacka__ = 'combine_models'
__description__ = 'TODO: Add description here'


from sklearn.base import clone

def combine_models(models, weights):
    """
    Kombinuje výsledky více modelů podle zadaných vah.
    :param models: Seznam modelů (např. LinearRegression, RANSAC).
    :param weights: Váhy jednotlivých modelů.
    :return: Kombinovaný model nebo jeho predikce.
    """
    if len(models) != len(weights):
        raise ValueError("Počet modelů musí odpovídat počtu vah.")

    combined_model = clone(models[0])
    combined_model.coef_ = sum(model.coef_ * weight for model, weight in zip(models, weights))
    return combined_model


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'