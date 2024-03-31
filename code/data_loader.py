#data_loader.py
from vectorizer import tokenize_all_reviews, tokenize_reviews
from preprocess import text_preprocess
import pandas as pd
import numpy as np

def clean_n_tokenize_data(sent, w2v):
    sent = text_preprocess(sent)
    tokenized_sent = tokenize_reviews(w2v.embed_model, w2v.embedding_dim, sent)
    return tokenized_sent

def read_data_from_csv():
    train = pd.read_csv('/kaggle/input/absa-phone-vi/datasets/Train.csv')
    val = pd.read_csv('/kaggle/input/absa-phone-vi/datasets/Val.csv')
    test = pd.read_csv('/kaggle/input/absa-phone-vi/datasets/Test.csv')
    return train, val, test

def load_data(data, w2v):
    data.loc[:, 'Comments'] = data['Comments'].apply(lambda x: text_preprocess(x))
    tokenized_reviews = tokenize_all_reviews(w2v.embed_model, w2v.embedding_dim, data['Comments'])

    return np.stack(pd.Series(tokenized_reviews)), data[['Pin', 'Service', 'General', 'Others', 'SPin', 'SSer', 'SGeneral', 'SOth']]