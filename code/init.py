from data_loader import load_data, read_data_from_csv
from vectorizer import W2VLoader
from training import SVCTuner
import pandas as pd
import joblib

if __name__ == "__main__":
    w2v_300dims = W2VLoader(
        w2v_path='/kaggle/input/phow2v/word2vec_vi_words_300dims/word2vec_vi_words_300dims.txt'
    )
    train, val, test = read_data_from_csv()

    X_train, y_train = load_data(train, w2v_300dims)
    X_val, y_val = load_data(val, w2v_300dims)
    X_test, y_test = load_data(test, w2v_300dims)

    #tuning
    svm_Pin = SVCTuner(X_train, y_train, X_val, y_val, attribute='Pin')
    svm_Pin.tune(n_trials=1000)

    svm_Service = SVCTuner(X_train, y_train, X_val, y_val, attribute='Service')
    svm_Service.tune(n_trials=1000)

    svm_General = SVCTuner(X_train, y_train, X_val, y_val, attribute='General')
    svm_General.tune(n_trials=1000)  

    svm_Others = SVCTuner(X_train, y_train, X_val, y_val, attribute='Others')
    svm_Others.tune(n_trials=1000)

    svm_SPin = SVCTuner(X_train, y_train, X_val, y_val, attribute='SPin')
    svm_SPin.tune(n_trials=1000)

    svm_SSer = SVCTuner(X_train, y_train, X_val, y_val, attribute='SSer')
    svm_SSer.tune(n_trials=1000)

    svm_SGeneral = SVCTuner(X_train, y_train, X_val, y_val, attribute='SGeneral')
    svm_SGeneral.tune(n_trials=1000)

    svm_SOth = SVCTuner(X_train, y_train, X_val, y_val, attribute='SOth')
    svm_SOth.tune(n_trials=1000)

    #load model
    svm_Pin = joblib.load('bestModelPin')
    svm_Service = joblib.load('bestModelService')
    svm_General = joblib.load('bestModelGeneral')
    svm_Others = joblib.load('bestModelOthers')

    svm_SPin = joblib.load('bestModelSPin')
    svm_SSer = joblib.load('bestModelSSer')
    svm_SGeneral = joblib.load('bestModelSGeneral')
    svm_SOth = joblib.load('bestModelSOth')

    