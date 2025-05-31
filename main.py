from core.CML import CML

def main():
    cml = CML()
    # Ukázkový text pro evoluci
    sentences = [
        "První testovací věta.",
        "Druhá testovací věta.",
        "Třetí věta."
    ]
    print("Testuji evoluci (optimalizaci):")
    evoluce_history = cml.testuj_evoluci(sentences, n_iter=10)
    for krok in evoluce_history:
        print(f"Krok {krok['step']}: vstup: {krok['input']} | výstup: {krok['output']}")

    print("\nVyhodnocení optimalizace:")
    vysledek = cml.vyhodnoceni()
    print(vysledek)

if __name__ == "__main__":
    main()