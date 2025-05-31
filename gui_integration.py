__znacka__ = 'gui_integration'
__description__ = 'TODO: Add description here'


import tkinter as tk
import requests

def submit_to_api(api_url, data):
    """
    Odesílá data na API a vrací odpověď.
    :param api_url: URL endpointu API.
    :param data: Data k odeslání.
    :return: Odpověď API.
    """
    response = requests.post(api_url, json=data)
    return response.json()


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'