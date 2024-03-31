import optuna
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.model_selection import train_test_split
import joblib
import optuna.visualization
from model import SVCModel

class SVCTuner:
    def __init__(self, X_train, y_train, X_val, y_val, attribute=None):
        self.X_train, self.y_train, self.X_val, self.y_val = X_train, y_train, X_val, y_val
        self.attribute = attribute
        self.best_params = None
        self.best_model = None

    def objective(self, trial):
        kernel = trial.suggest_categorical('kernel', ['linear', 'poly', 'rbf', 'sigmoid'])
        C = trial.suggest_float('C', 1e-5, 100)
        gamma = trial.suggest_categorical('gamma', ['scale', 'auto'])
        
        svc_model = SVCModel(kernel=kernel, C=C, gamma=gamma, attribute=self.attribute)
        svc_model.fit(self.X_train, self.y_train)
        
        acc = svc_model.calculate_accuracy_score(self.X_val, self.y_val)
        
        return acc

    def tune(self, n_trials=100):
        study = optuna.create_study(direction='maximize')
        study.optimize(self.objective, n_trials=n_trials)
        
        self.best_params = study.best_params
        self.best_model = SVCModel(kernel=self.best_params['kernel'], 
                                   C=self.best_params['C'], 
                                   gamma=self.best_params['gamma'], 
                                   attribute=self.attribute)
        
        self.best_model.fit(self.X_train, self.y_train)
        joblib.dump(self.best_model, 'bestModel'+self.attribute)
        
        return optuna.visualization.plot_optimization_history(study)
    
    def evaluate_best_model(self, X_test, y_test):
        self.X_test = X_test
        self.y_test = y_test
        if self.best_model is None:
            raise ValueError("No best model available. Please run tuning first.")
        
        base_model = SVCModel(attribute=self.attribute)
        base_model.fit(self.X_train, self.y_train)
        y_pred_base = base_model.predict(self.X_test)
        base_acc = base_model.calculate_accuracy_score(self.X_test, self.y_test, y_pred=y_pred_base)
        base_f1 = base_model.calculate_f1_score(self.X_test, self.y_test, y_pred=y_pred_base)
        base_precision = base_model.calculate_precision_score(self.X_test, self.y_test, y_pred=y_pred_base)
        base_recall = base_model.calculate_recall_score(self.X_test, self.y_test, y_pred=y_pred_base)
        
        y_pred_best = self.best_model.predict(self.X_test)
        best_acc = self.best_model.calculate_accuracy_score(self.X_test, self.y_test, y_pred=y_pred_best)
        best_f1 = self.best_model.calculate_f1_score(self.X_test, self.y_test, y_pred=y_pred_best)
        best_recall = self.best_model.calculate_recall_score(self.X_test, self.y_test, y_pred=y_pred_best)
        best_precision = self.best_model.calculate_precision_score(self.X_test, self.y_test, y_pred=y_pred_best)

        return {'Base':{'Accuracy': base_acc,
                        'Precision': base_precision,
                        'Recall': base_recall,
                        'F1': base_f1},
                'Best':{'Accuracy': best_acc,
                        'Precision': best_precision,
                        'Recall': best_recall,
                        'F1': best_f1}}