from gensim.models import KeyedVectors

class W2VLoader():
    def __init__(self, w2v_path=''):
        self.embed_model = KeyedVectors.load_word2vec_format(w2v_path, binary=False)
        self.pretrained_words = self.get_pretrained_words()
        self.vocab_size = len(self.pretrained_words)
        self.embedding_dim = self.get_embedding_dim()

    def get_pretrained_words(self):
        # Store pretrained vocab
        pretrained_words = list(self.embed_model.key_to_index.keys())
        return pretrained_words

    def get_embedding_dim(self):
        # Get dimensionality of embeddings
        word = self.pretrained_words[0]
        embedding_dim = self.embed_model.get_vector(word).shape[0]
        return embedding_dim