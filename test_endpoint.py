__znacka__ = 'test_endpoint'
__description__ = 'TODO: Add description here'


import httpx

def test_endpoint(url, data):
    """
    Testuje API endpoint.
    :param url: URL endpointu.
    :param data: Data pro POST request.
    :return: Odpověď API.
    """
    response = httpx.post(url, json=data)
    return response.status_code, response.json()


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'