class EvoCore:
    def __init__(self, state_count=2):
        self.state_count = state_count  # Počet stavů (2 = binární, 24 = rozšířená logika)
        self.modules = []
        
    def register_module(self, module):
        """Registruje funkční modul do EVO."""
        self.modules.append(module)
    
    def process(self, data):
        """Hlavní metoda pro zpracování dat skrz všechny moduly."""
        for module in self.modules:
            data = module.process(data, self.state_count)
        return data

# Příklad modulu pro binární přenos
class BinaryTransferModule:
    def process(self, data, state_count):
        # Zde prozatím pouze binární operace, později můžeš přidat vícestavovou logiku
        return data

# Příklad použití
if __name__ == "__main__":
    evo = EvoCore(state_count=2)
    evo.register_module(BinaryTransferModule())
    vstup = [1,0,1,1,0,0,1,0]
    vystup = evo.process(vstup)
    print("Výstupní data EVO:", vystup)