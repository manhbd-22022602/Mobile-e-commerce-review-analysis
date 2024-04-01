#vectorizer.py
import numpy as np
from gensim.models import KeyedVectors

def tokenize_all_reviews(embed_model, dims, reviews):
    # split each review into a list of words
    reviews_words = [review.split() for review in reviews]

    tokenized_reviews = []
    for review in reviews_words:
        mean_embedding = np.zeros(dims)
        num_words = 0
        for word in review:
            try:
                mean_embedding += embed_model[word]
                num_words += 1
            except:
                continue
        mean_embedding /= num_words
        tokenized_reviews.append(mean_embedding)

    return tokenized_reviews 

def tokenize_reviews(embed_model, dims, sent):
    words = sent.split()
    mean_embedding = np.zeros(dims)
    num_words = 0
    for word in words:
        try:
            mean_embedding += embed_model[word]
            num_words += 1
        except:
            continue
    mean_embedding /= num_words
    return mean_embedding

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
