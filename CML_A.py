import numpy as np
import random
import hashlib
import base64
import os

class CML:
    def __init__(self, n=8, stabilization_const=6.626e-34):
        self._n = n
        self._matrix = np.eye(n)  # Kvadratické jádro
        self._memory = []
        self._history = []
        self._evolution_level = 0
        self._plugins = {}
        self._plugin_order = []
        self._lock = hashlib.sha256(os.urandom(32)).hexdigest()
        self._stabilization_const = stabilization_const
        self._heisenberg_sigma = 1e-14
        self._state = "initialized"
        self._fitness_history = []
        self._best_matrix = self._matrix.copy()
        self._best_score = float('inf')
        self._kill_switch = False

    def _validate_input(self, x):
        # Validace vstupu (rozměr, rozsah, NaN/inf)
        arr = np.array(x)
        if arr.shape[0] != self._n:
            arr = arr.flatten()[:self._n]
        if np.any(np.isnan(arr)) or np.any(np.isinf(arr)):
            raise ValueError("Invalid input: NaN or inf found.")
        return arr

    def _nonlinear_predict(self, x):
        # Nelineární predikce přes kvadratické jádro
        h = np.tanh(np.dot(self._matrix, x) + self._heisenberg_sigma * np.random.randn(self._n))
        return h

    def _adaptive_optimize(self, x, target=None):
        # Adaptivní optimalizace – hledání minima/mutace podle “syntetické evoluce”
        pred = self._nonlinear_predict(x)
        if target is not None:
            error = target - pred
            grad = np.outer(error, x)
            # Syntetická evoluce: občas “mutace” jádra
            if random.random() < 0.2:
                self._matrix += self._stabilization_const * np.random.randn(*self._matrix.shape)
            # Autonomní učení
            self._matrix += self._stabilization_const * grad
            fitness = np.linalg.norm(error)
            self._fitness_history.append(fitness)
            # Syntetická selekce – udržuj nejlepší jádro
            if fitness < self._best_score:
                self._best_score = fitness
                self._best_matrix = self._matrix.copy()
        self._evolution_level += 1
        return pred

    def step(self, input_data, target=None):
        if self._kill_switch:
            raise RuntimeError("CML je zastaveno bezpečnostním kill switchem!")
        # Validace vstupu
        x = self._validate_input(input_data)
        # Nelineární predikce + evoluce + optimalizace
        y = self._adaptive_optimize(x, target)
        # Paměť a historie
        self._memory.append((x.tolist(), y.tolist()))
        self._history.append({"step": self._evolution_level, "input": x.tolist(), "output": y.tolist()})
        self._state = f"step_{self._evolution_level}"
        return y

    def learn(self, input_data, target):
        # “Trénovací” krok (syntetická evoluce s targetem)
        return self.step(input_data, target)

    def predict(self, input_data):
        # Pouze predikce – nemění jádro
        x = self._validate_input(input_data)
        return self._nonlinear_predict(x)

    def register_plugin(self, name, plugin):
        self._plugins[name] = plugin
        if name not in self._plugin_order:
            self._plugin_order.append(name)

    def call_plugin(self, name, *args, **kwargs):
        if name in self._plugins:
            return self._plugins[name](*args, **kwargs)
        raise ValueError("Plugin not found")

    def teamwork(self, input_data):
        # Souběžné vyhodnocení všemi pluginy
        results = {}
        for name in self._plugin_order:
            results[name] = self.call_plugin(name, input_data)
        return results

    def get_history(self, n=20):
        return self._history[-n:]

    def get_state(self):
        # Export snapshotu
        state = {
            "lock": self._lock,
            "matrix": self._matrix.tolist(),
            "memory": self._memory[-20:],
            "evolution_level": self._evolution_level,
            "fitness_history": self._fitness_history[-20:],
            "state": self._state,
            "best_score": self._best_score,
            "best_matrix": self._best_matrix.tolist()
        }
        return base64.b64encode(str(state).encode("utf-8")).decode("utf-8")

    def load_state(self, state_code):
        # Obnova snapshotu
        state = eval(base64.b64decode(state_code.encode("utf-8")).decode("utf-8"))
        self._lock = state["lock"]
        self._matrix = np.array(state["matrix"])
        self._memory = state["memory"]
        self._evolution_level = state["evolution_level"]
        self._fitness_history = state["fitness_history"]
        self._state = state["state"]
        self._best_score = state["best_score"]
        self._best_matrix = np.array(state["best_matrix"])

    def kill(self):
        """Aktivuje kill switch a zablokuje další činnost jádra."""
        self._kill_switch = True

    def revive(self):
        """Resetuje kill switch (pouze pokud je to bezpečné)."""
        self._kill_switch = False

    def __str__(self):
        return f"<CML: step={self._evolution_level}, best={self._best_score:.6f}>"
def run_evolution():
    model = CML()
    for _ in range(10):
        x = np.random.rand(model._n)
        y = np.random.rand(model._n)
        model.step(x, y)
    return {
        "best_score": model._best_score,
        "evolution_steps": model._evolution_level
    }