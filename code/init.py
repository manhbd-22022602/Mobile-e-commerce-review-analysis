from data_loader import load_data, read_data_from_csv
from vectorizer import W2VLoader
from training import SVCTuner
import pandas as pd
import joblib

if __name__ == "__main__":
    #load w2v model
    w2v_300dims = W2VLoader(
        w2v_path='/kaggle/input/phow2v/word2vec_vi_words_300dims/word2vec_vi_words_300dims.txt'
    )

    #load data
    train, val, test = read_data_from_csv()
    
    X_train, y_train = load_data(train, w2v_300dims)
    X_val, y_val = load_data(val, w2v_300dims)
    X_test, y_test = load_data(test, w2v_300dims)

    #tuning
    svm_Pin = SVCTuner(X_train, y_train, X_val, y_val, attribute='Pin')
    svm_Pin.tune(n_trials=100)

    svm_Service = SVCTuner(X_train, y_train, X_val, y_val, attribute='Service')
    svm_Service.tune(n_trials=100)

    svm_General = SVCTuner(X_train, y_train, X_val, y_val, attribute='General')
    svm_General.tune(n_trials=100)  

    svm_Others = SVCTuner(X_train, y_train, X_val, y_val, attribute='Others')
    svm_Others.tune(n_trials=100)

    svm_SPin = SVCTuner(X_train, y_train, X_val, y_val, attribute='SPin')
    svm_SPin.tune(n_trials=100)

    svm_SSer = SVCTuner(X_train, y_train, X_val, y_val, attribute='SSer')
    svm_SSer.tune(n_trials=100)

    svm_SGeneral = SVCTuner(X_train, y_train, X_val, y_val, attribute='SGeneral')
    svm_SGeneral.tune(n_trials=100)

    svm_SOth = SVCTuner(X_train, y_train, X_val, y_val, attribute='SOth')
    svm_SOth.tune(n_trials=100)

    #load model
    svm_Pin = joblib.load('bestModelPin')
    svm_Service = joblib.load('bestModelService')
    svm_General = joblib.load('bestModelGeneral')
    svm_Others = joblib.load('bestModelOthers')

    svm_SPin = joblib.load('bestModelSPin')
    svm_SSer = joblib.load('bestModelSSer')
    svm_SGeneral = joblib.load('bestModelSGeneral')
    svm_SOth = joblib.load('bestModelSOth')

    #evaluate
    compare_table = {}
    compare_table['Pin'] = svm_Pin.evaluate_best_model()
    compare_table['Service'] = svm_Service.evaluate_best_model()
    compare_table['General'] = svm_General.evaluate_best_model()
    compare_table['Others'] = svm_Others.evaluate_best_model()

    compare_table['SPin'] = svm_SPin.evaluate_best_model()
    compare_table['SSer'] = svm_SSer.evaluate_best_model()
    compare_table['SGeneral'] = svm_SGeneral.evaluate_best_model()
    compare_table['SOthers'] = svm_SOth.evaluate_best_model()

    compare_df = pd.DataFrame(compare_table).T
    print(compare_df)