import numpy as np
import networkx as nx

class LiveVectorLibrary:
    def __init__(self):
        self.graph = nx.Graph()
        self.token_vectors = {}
        self.quarantine = {}  # Dočasné úložiště neschválených vektorů
        self.min_similarity = 0.2  # Práh pro validaci (lze učitelně upravovat)

    def vectorize_text(self, text):
        words = text.lower().split()
        vectors = [np.random.rand(10) for _ in words]  # nahraď embedding modelem
        for word, vec in zip(words, vectors):
            self._safe_add_token(word, vec)
        return vectors

    def _safe_add_token(self, token, vector):
        # Validace – existuje už podobný vektor?
        for existing_token, existing_vector in self.token_vectors.items():
            similarity = self._cosine_similarity(vector, existing_vector)
            if similarity > self.min_similarity:
                self.add_token(token, vector)
                return
        # Pokud není dost podobný, do karantény
        self.quarantine[token] = vector

    def add_token(self, token, vector):
        if token not in self.token_vectors:
            self.token_vectors[token] = vector
            self.graph.add_node(token)
            self._barabasi_attach(token)
        else:
            self.token_vectors[token] = (self.token_vectors[token] + vector) / 2

    def _barabasi_attach(self, new_token):
        if self.graph.number_of_nodes() > 1:
            degrees = np.array([self.graph.degree(n) for n in self.graph.nodes()])
            probs = degrees / degrees.sum()
            chosen = np.random.choice(list(self.graph.nodes()), p=probs)
            self.graph.add_edge(new_token, chosen)

    def _cosine_similarity(self, v1, v2):
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-8)

    def quarantine_review(self):
        # Projde karanténu a ověří, zda už není bezpečné tokeny zařadit
        to_add = []
        for token, vector in self.quarantine.items():
            for existing_vector in self.token_vectors.values():
                if self._cosine_similarity(vector, existing_vector) > self.min_similarity:
                    to_add.append(token)
                    break
        for token in to_add:
            self.add_token(token, self.quarantine[token])
            del self.quarantine[token]