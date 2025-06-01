class EmotionLearner:
    def __init__(self):
        self.known_patterns = {}
        
    def learn(self, input_data, label):
        """Uloží vstupní data jako vzor určité emoce."""
        if label not in self.known_patterns:
            self.known_patterns[label] = []
        self.known_patterns[label].append(input_data)
    
    def classify(self, input_data):
        """Vrací název nejbližší naučené emoce podle jednoduché podobnosti."""
        best_label = None
        best_score = float('-inf')
        for label, patterns in self.known_patterns.items():
            for pattern in patterns:
                score = self.similarity(input_data, pattern)
                if score > best_score:
                    best_score = score
                    best_label = label
        return best_label
    
    def similarity(self, a, b):
        """Základní podobnost, lze nahradit pokročilou funkcí (např. cosine similarity, DTW, ...)."""
        return -sum(abs(x - y) for x, y in zip(a, b))  # jednoduchá L1 vzdálenost

class ZecPatternLearner:
    def __init__(self):
        self.vocabulary = {}
    
    def learn_pattern(self, text, label):
        """Učí se jazykové vzorce podle zadaného labelu (např. význam, kategorie, nálada)."""
        words = text.split()
        for word in words:
            if word not in self.vocabulary:
                self.vocabulary[word] = {}
            if label not in self.vocabulary[word]:
                self.vocabulary[word][label] = 0
            self.vocabulary[word][label] += 1
    
    def predict_label(self, text):
        """Předpoví dominantní label pro daný text na základě naučených vzorců."""
        label_scores = {}
        words = text.split()
        for word in words:
            if word in self.vocabulary:
                for label, count in self.vocabulary[word].items():
                    label_scores[label] = label_scores.get(label, 0) + count
        if not label_scores:
            return None
        return max(label_scores, key=label_scores.get)

# Integrace do EVO
class EvoEmotionZec:
    def __init__(self):
        self.emotion_learner = EmotionLearner()
        self.zec_learner = ZecPatternLearner()
        self.plugins = []  # sem lze registrovat pomocné pluginy/funkce

    def add_plugin(self, plugin):
        self.plugins.append(plugin)

    def train_emotion(self, data, label):
        self.emotion_learner.learn(data, label)
    
    def train_zec(self, text, label):
        self.zec_learner.learn_pattern(text, label)

    def classify_emotion(self, data):
        return self.emotion_learner.classify(data)
    
    def predict_zec(self, text):
        return self.zec_learner.predict_label(text)