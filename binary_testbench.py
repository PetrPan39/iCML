import random

def generate_binary_sequence(length):
    """Vygeneruje náhodný binární řetězec o dané délce."""
    return [random.choice([0, 1]) for _ in range(length)]

def transmit_with_noise(sequence, error_rate=0.0):
    """
    Simuluje přenos binárního řetězce s možností výskytu chyb (šumu).
    error_rate: pravděpodobnost chyby na jednom bitu (0.0 - 1.0)
    """
    noisy_sequence = []
    for bit in sequence:
        if random.random() < error_rate:
            # Chyba: invertuj bit
            noisy_sequence.append(1 - bit)
        else:
            noisy_sequence.append(bit)
    return noisy_sequence

def compare_sequences(seq1, seq2):
    """Porovná dva binární řetězce a vrátí počet rozdílů (chyb)."""
    return sum(b1 != b2 for b1, b2 in zip(seq1, seq2))

def print_sequences(seq1, seq2):
    """Vytiskne oba řetězce a zvýrazní rozdíly."""
    out = []
    for b1, b2 in zip(seq1, seq2):
        if b1 == b2:
            out.append(str(b1))
        else:
            out.append(f"[{b1}->{b2}]")
    print('Výsledek porovnání:', ' '.join(out))

if __name__ == "__main__":
    length = 32
    error_rate = 0.05  # 5% šum
    original = generate_binary_sequence(length)
    received = transmit_with_noise(original, error_rate)
    print("Původní řetězec: ", original)
    print("Přijatý  řetězec: ", received)
    errors = compare_sequences(original, received)
    print(f"Počet chyb: {errors} / {length}")
    print_sequences(original, received)