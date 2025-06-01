class WordCell:
    def __init__(self, word, vector, emotion=None):
        self.word = word
        self.vector = vector
        self.emotion = emotion
        self.edges = {}  # klíč: směr/typ spojení, hodnota: sad sousedních buněk

    def add_edge(self, direction, other_word_cell):
        if direction not in self.edges:
            self.edges[direction] = set()
        self.edges[direction].add(other_word_cell)

    def archive_usage(self, context, sentence):
        # Archivuje, v jakém směru a v jaké větě/slovní vazbě bylo slovo použito
        pass

# Archivace větného spojení:
class PhraseCell:
    def __init__(self, phrase, words):
        self.phrase = phrase
        self.words = words  # seznam WordCell
        self.edges = {}     # směr: další možné fráze, kontexty