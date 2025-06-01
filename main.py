from evo_core import EvoCore, BinaryTransferModule

if __name__ == "__main__":
    evo = EvoCore(state_count=2)
    evo.register_module(BinaryTransferModule())
    vstup = [1, 0, 1, 1, 0, 0, 1, 0]
    print("Vstupní data:", vstup)
    vystup = evo.process(vstup)
    print("Výstupní data EVO:", vystup)