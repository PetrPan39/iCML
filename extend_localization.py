__znacka__ = 'extend_localization'
__description__ = 'TODO: Add description here'


from flask_babel import Babel, _

def extend_localization(app, locales):
    """
    Přidává lokalizační podporu aplikaci Flask.
    :param app: Flask aplikace.
    :param locales: Seznam podporovaných lokalizací.
    """
    app.config['BABEL_SUPPORTED_LOCALES'] = locales
    babel = Babel(app)
    return babel


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'

def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
