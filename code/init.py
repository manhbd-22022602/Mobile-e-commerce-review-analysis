from data_loader import load_data
from vectorizer import W2VLoader
from training import SVCTuner
import pandas as pd
import joblib

# read data from csv
def read_data_from_csv():
    train = pd.read_csv('/kaggle/input/absa-phone-vi/datasets/Train.csv')
    val = pd.read_csv('/kaggle/input/absa-phone-vi/datasets/Val.csv')
    test = pd.read_csv('/kaggle/input/absa-phone-vi/datasets/Test.csv')
    return train, val, test

# Filter sentences that do not contain aspects to classify sentiment
def filter_sentences_without_aspects(train, val, test, attribute):
    train_data = train[train[attribute] == 1]
    val_data = val[val[attribute] == 1]
    test_data = test[test[attribute] == 1]
    return train_data, val_data, test_data

# Tokenize data
def tokenize_data(train, val, test, Loader):
    X_train, y_train = load_data(train, Loader)
    X_val, y_val = load_data(val, Loader)
    X_test, y_test = load_data(test, Loader)
    return X_train, y_train, X_val, y_val, X_test, y_test

# Tuning hyperparameter
def tune_svm(X_train, y_train, X_val, y_val, attribute, n_trials=1000):
    svm = SVCTuner(X_train, y_train, X_val, y_val, attribute=attribute)
    svm.tune(n_trials=n_trials)
    return svm

def main():

    w2v_300dims = W2VLoader(
        w2v_path='/kaggle/input/phow2v/word2vec_vi_words_300dims/word2vec_vi_words_300dims.txt'
    )
    

    # Load data from file csv
    train, val, test = read_data_from_csv()


    # Filter sentences that do not contain aspects to classify sentiment
    train_SPin, val_SPin, test_SPin = filter_sentences_without_aspects(train=train, val=val, test=test, attribute='Pin')
    train_SSer, val_SSer, test_SSer = filter_sentences_without_aspects(train=train, val=val, test=test, attribute='Service')
    train_SGeneral, val_SGeneral, test_SGeneral = filter_sentences_without_aspects(train=train, val=val, test=test, attribute='General')
    train_SOth, val_SOth, test_SOth = filter_sentences_without_aspects(train=train, val=val, test=test, attribute='Others')


    # Tokenize data
    X_train, y_train, X_val, y_val, X_test, y_test = tokenize_data(train=train, val=val, test=test, Loader=w2v_300dims)
    X_train_SPin, y_train_SPin, X_val_SPin, y_val_SPin, X_test_SPin, y_test_SPin = tokenize_data(train=train_SPin, val=val_SPin, test=test_SPin, Loader=w2v_300dims)
    X_train_SSer, y_train_SSer, X_val_SSer, y_val_SSer, X_test_SSer, y_test_SSer = tokenize_data(train=train_SSer, val=val_SSer, test=test_SSer, Loader=w2v_300dims)
    X_train_SGeneral, y_train_SGeneral, X_val_SGeneral, y_val_SGeneral, X_test_SGeneral, y_test_SGeneral = tokenize_data(train=train_SGeneral, val=val_SGeneral, test=test_SGeneral, Loader=w2v_300dims)
    X_train_SOth, y_train_SOth, X_val_SOth, y_val_SOth, X_test_SOth, y_test_SOth = tokenize_data(train=train_SOth, val=val_SOth, test=test_SOth, Loader=w2v_300dims)


    # Tuning hyperparameter
    svm_Pin = tune_svm(X_train, y_train, X_val, y_val, attribute='Pin')
    svm_Service = tune_svm(X_train, y_train, X_val, y_val, attribute='Service')
    svm_General = tune_svm(X_train, y_train, X_val, y_val, attribute='General')
    svm_Others = tune_svm(X_train, y_train, X_val, y_val, attribute='Others')
    svm_SPin = tune_svm(X_train_SPin, y_train_SPin, X_val_SPin, y_val_SPin, attribute='SPin')
    svm_SSer = tune_svm(X_train_SSer, y_train_SSer, X_val_SSer, y_val_SSer, attribute='SSer')
    svm_SGeneral = tune_svm(X_train_SGeneral, y_train_SGeneral, X_val_SGeneral, y_val_SGeneral, attribute='SGeneral')
    svm_SOth = tune_svm(X_train_SOth, y_train_SOth, X_val_SOth, y_val_SOth, attribute='SOth')


    # Load model
    svm_Pin = joblib.load('bestModelPin')
    svm_Service = joblib.load('bestModelService')
    svm_General = joblib.load('bestModelGeneral')
    svm_Others = joblib.load('bestModelOthers')

    svm_SPin = joblib.load('bestModelSPin')
    svm_SSer = joblib.load('bestModelSSer')
    svm_SGeneral = joblib.load('bestModelSGeneral')
    svm_SOth = joblib.load('bestModelSOth')

if __name__ == "__main__":
    main()