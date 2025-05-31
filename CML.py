from core.CML_A import CML as CML_A
from core.CML_B import CML_B
from core.CML_C import CML_C

class CML:
    def __init__(self, plugins_path="plugins"):
        self.plugin_manager = CML_B(plugins_path)                 # načti všechny pluginy
        self.premier = CML_A(n=10)                               # hlavní evoluční třída
        self.speaker = CML_C(self, self.plugin_manager)           # komunikátor s přístupem k pluginům

    def predikuj_a_optim(self, text, vektor, target=None):
        if target is not None:
            output = self.premier.learn(vektor, target)
        else:
            output = self.premier.predict(vektor)
        return output

    def testuj_evoluci(self, sentences, n_iter=10):
        history = []
        for i, text in enumerate(sentences):
            vektor = self.speaker.vektorizuj(text)
            target = [sum(vektor)] * len(vektor)
            output = self.premier.learn(vektor, target)
            history.append({
                "step": i,
                "input": text,
                "vector": vektor,
                "target": target,
                "output": output.tolist() if hasattr(output, "tolist") else output
            })
        return history

    def vyhodnoceni(self):
        best_score = getattr(self.premier, "_best_score", None)
        steps = getattr(self.premier, "_evolution_level", None)
        return {"best_score": best_score, "evolution_steps": steps}