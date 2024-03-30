import optuna
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from model import SVCModel
import joblib

class SVCTuner:
    def __init__(self, X_train, y_train, X_test, y_test, attribute=None):
        self.X_train, self.y_train, self.X_test, self.y_test = X_train, y_train, X_test, y_test
        self.attribute = attribute
        self.best_params = None
        self.best_model = None

    def objective(self, trial):
        kernel = trial.suggest_categorical('kernel', ['linear', 'poly', 'rbf', 'sigmoid'])
        C = trial.suggest_loguniform('C', 1e-5, 100)
        gamma = trial.suggest_categorical('gamma', ['scale', 'auto'])
        
        svc_model = SVCModel(kernel=kernel, C=C, gamma=gamma, attribute=self.attribute)
        svc_model.fit(self.X_train, self.y_train)
        
        f1 = svc_model.calculate_f1_score(self.X_test, self.y_test)
        
        return f1

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

    def evaluate_best_model(self):
        if self.best_model is None:
            raise ValueError("No best model available. Please run tuning first.")
        
        base_model = SVCModel(attribute=self.attribute)
        base_f1 = base_model.calculate_f1_score(self.X_test, self.y_test)
        
        y_pred_best = self.best_model.predict(self.X_test)
        best_f1 = f1_score(self.y_test[self.attribute], y_pred_best)
        best_recall = recall_score(self.y_test[self.attribute], y_pred_best)
        best_precision = precision_score(self.y_test[self.attribute], y_pred_best)

        print("Base Model - F1 Score:", base_f1)
        print("Best Model - F1 Score:", best_f1)
        print("Best Model - recall Score:", best_recall)
        print("Best Model - precision Score:", best_precision)
        print("Best Hyperparameters:", self.best_params)


