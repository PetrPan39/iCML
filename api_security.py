__znacka__ = 'api_security'
__description__ = 'TODO: Add description here'


from flask_jwt_extended import JWTManager

def setup_jwt(app, secret_key):
    """
    Nastaví zabezpečení API pomocí JWT.
    :param app: Flask aplikace.
    :param secret_key: Tajný klíč pro JWT.
    """
    app.config['JWT_SECRET_KEY'] = secret_key
    jwt = JWTManager(app)
    return jwt


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'

def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
