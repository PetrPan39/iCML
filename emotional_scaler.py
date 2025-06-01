import numpy as np

class EmotionalScaler:
    def __init__(self, emotion_model=None):
        self.emotion_model = emotion_model  # Možno napojit AI model pro lepší analýzu
        self.last_emotion_vector = None

    def is_static_scientific(self, input_data):
        """Detekuje, zda je vstup matematický, fyzikální, chemický nebo stacionární."""
        if isinstance(input_data, str):
            # Klíčová slova a jednoduchá heuristika
            keywords = [
                "rovnice", "vzorec", "konstanta", "tabulka", "chemický vzorec", "fyzikální zákon",
                "E=", "F=", "PV=nRT", "H2O", "NaCl", "CO2"
            ]
            if any(kw in input_data for kw in keywords):
                return True
            # Čistě číselný/statický vstup
            s = input_data.strip().replace(" ", "")
            if s.replace(".", "").replace("-", "").isdigit():
                return True
        # Můžeš přidat další typové kontroly, např. tabulka, numpy array, atd.
        return False

    def scale_emotion(self, input_data):
        """Zpracuje dynamický vstup, vrátí emocionální vektor a popis."""
        if self.is_static_scientific(input_data):
            return None, "Vstup je exaktní/stacionární – emoce neskalovány."
        # ---- EMOČNÍ ANALÝZA ----
        if self.emotion_model:
            # Pokud máš AI model, použij ho
            emotion_vector, labels = self.emotion_model(input_data)
        else:
            # Mock: náhodně generovaný emocionální vektor (nahraď skutečnou AI analýzou)
            # Dimenze: radost, smutek, strach, hněv, překvapení, neutrálnost, zvědavost, úleva
            emotion_vector = np.random.uniform(-1, 1, 8)
            labels = self.label_emotion(emotion_vector)
        self.last_emotion_vector = emotion_vector
        return emotion_vector, labels

    def label_emotion(self, vector):
        """Základní popis na základě nejsilnější složky vektoru."""
        dim_names = [
            "radost", "smutek", "strach", "hněv", "překvapení", "neutrálnost", "zvědavost", "úleva"
        ]
        idx = int(np.argmax(np.abs(vector)))
        sign = "pozitivní" if vector[idx] >= 0 else "negativní"
        return f"{sign} {dim_names[idx]} (škála ±1)"

# --- Příklad použití ---
if __name__ == "__main__":
    scaler = EmotionalScaler()
    vstupy = [
        "Dnes mám radost, protože svítí slunce!",
        "E = mc^2",
        "Ztratil jsem klíče a mám strach.",
        "PV = nRT",
        "Můj pes se bojí bouřky.",
        "Konstanta Plancka je 6.626e-34 Js",
        "Tvoje překvapení mě pobavilo."
    ]
    for v in vstupy:
        emo_vec, popis = scaler.scale_emotion(v)
        print(f"Vstup: {v}\nEmoce: {emo_vec}\nPopis: {popis}\n")