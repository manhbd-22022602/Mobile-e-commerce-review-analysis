from data_loader import load_data, read_data_from_csv
from vectorizer import W2VLoader
from training import SVCTuner
from model import SVCModel
import numpy as np
import pandas as pd
import joblib

if __name__ == "__main__":
    #load w2v model
    try:
        # Kiểm tra xem biến đã được lưu trong cache chưa
        w2v_300dims = joblib.load('w2v_300dims_cache.pkl')
        print("Đã load w2v_300dims từ cache.")
    except FileNotFoundError:
        # Nếu chưa có trong cache, thực hiện load và lưu vào cache
        w2v_300dims = W2VLoader(w2v_path='phow2v/word2vec_vi_words_300dims.txt')
        joblib.dump(w2v_300dims, 'w2v_300dims_cache.pkl')
        print("Đã load và lưu w2v_300dims vào cache.")

    tuning = input("Tuning and train model? (True/False): ")

    #load data
    train, val, test = read_data_from_csv()
    
    X_train, y_train = load_data(train, w2v_300dims)
    X_val, y_val = load_data(val, w2v_300dims)
    X_test, y_test = load_data(test, w2v_300dims)

    if tuning.lower() == 'true':
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

    #load pretrained model (skip tuning and evaluating due to long time to run)
    svm_Pin = joblib.load('pretrained_svm/bestModelPin')
    svm_Service = joblib.load('pretrained_svm/bestModelService')
    svm_General = joblib.load('pretrained_svm/bestModelGeneral')
    svm_Others = joblib.load('pretrained_svm/bestModelOthers')

    svm_SPin = joblib.load('pretrained_svm/bestModelSPin')
    svm_SSer = joblib.load('pretrained_svm/bestModelSSer')
    svm_SGeneral = joblib.load('pretrained_svm/bestModelSGeneral')
    svm_SOth = joblib.load('pretrained_svm/bestModelSOth')

    #predict
    acc_Pin = svm_Pin.calculate_accuracy_score(X_test, y_test)
    acc_Service = svm_Service.calculate_accuracy_score(X_test, y_test)
    acc_General = svm_General.calculate_accuracy_score(X_test, y_test)
    acc_Others = svm_Others.calculate_accuracy_score(X_test, y_test)
    acc_SPin = svm_SPin.calculate_accuracy_score(X_test, y_test)
    acc_SSer = svm_SSer.calculate_accuracy_score(X_test, y_test)
    acc_SGeneral = svm_SGeneral.calculate_accuracy_score(X_test, y_test)
    acc_SOth = svm_SOth.calculate_accuracy_score(X_test, y_test)

    print(f'Accuracy Pin: {acc_Pin}')
    print(f'Accuracy Service: {acc_Service}')
    print(f'Accuracy General: {acc_General}')
    print(f'Accuracy Others: {acc_Others}')
    print(f'Accuracy SPin: {acc_SPin}')
    print(f'Accuracy SSer: {acc_SSer}')
    print(f'Accuracy SGeneral: {acc_SGeneral}')
    print(f'Accuracy SOthers: {acc_SOth}')
    print(f'Mean accuracy: {np.mean([acc_Pin, acc_Service, acc_General, acc_Others, acc_SPin, acc_SSer, acc_SGeneral, acc_SOth])}')
