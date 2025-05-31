# PLUGIN A4: Emotion Predictor
def register(master):
    logic = '''
def _core(self, task):
    if isinstance(task, (int, float)):
        if task > 70:
            return 'šťastná'
        elif task < 30:
            return 'smutná'
        else:
            return 'neutrální'
    return 'neznámá'
'''
    master.teamwork.add_specialist('emotion_predictor', logic)

def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
