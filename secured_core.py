class CML_A:
    def __init__(self):
        self.__private_param = 42   # dvojité podtržítko ochrání před přístupem
        self._kill_switch = False

    def step(self, x, y):
        if self._kill_switch:
            raise RuntimeError("Systém je v bezpečnostním režimu.")
        # ... vlastní logika evoluce a self-tuningu ...

    def _self_tune(self):
        # pouze interní self-tuning, žádná veřejná cesta
        pass

    def kill(self):
        self._kill_switch = True

    # ŽÁDNÝ veřejný setter nebo getter pro __private_param!