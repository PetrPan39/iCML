__znacka__ = 'plugin_generator'
__description__ = 'TODO: Add description here'

# PLUGIN D3: Plugin Evolution Generator
def register(master):
    logic = '''
def _core(self, task):
    if isinstance(task, dict) and 'name' in task and 'logic' in task:
        self.master.evo_code.create_plugin(task['name'], task['logic'])
        return f"Plugin {task['name']} vytvořen."
    return "Neplatný vstup"
'''
    master.teamwork.add_specialist('plugin_generator', logic)


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'