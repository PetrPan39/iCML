__znacka__ = 'team_module'
__description__ = 'TODO: Add description here'


import threading

def team_work(equations, methods):
    """
    Rozdělí úlohy mezi různé metody a agenty.
    :param equations: Seznam rovnic k řešení.
    :param methods: Seznam metod pro řešení rovnic.
    :return: Seznam výsledků od všech agentů.
    """
    results = []
    threads = []

    def worker(eq, method):
        result = method(eq)
        results.append(result)

    for equation, method in zip(equations, methods):
        thread = threading.Thread(target=worker, args=(equation, method))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'