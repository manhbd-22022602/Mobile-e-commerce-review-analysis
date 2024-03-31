#data_loader.py
from vectorizer import tokenize_all_reviews, tokenize_reviews
from preprocess import text_preprocess, load_sentiment_dicts
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
    path_pos = 'sentiment_dicts/pos.txt'
    path_nag = 'sentiment_dicts/nag.txt'
    path_not = 'sentiment_dicts/not.txt'
    pos_list, nag_list, not_list = load_sentiment_dicts(path_pos, path_nag, path_not)

    data.loc[:, 'Comments'] = data['Comments'].apply(lambda x: text_preprocess(x, pos_list, nag_list, not_list))
    tokenized_reviews = tokenize_all_reviews(w2v.embed_model, w2v.embedding_dim, data['Comments'])

    return np.stack(pd.Series(tokenized_reviews)), data[['Pin', 'Service', 'General', 'Others', 'SPin', 'SSer', 'SGeneral', 'SOth']]