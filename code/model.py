from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

class SVCModel():
    def __init__(self, kernel='rbf', C=1.0, gamma='scale', attribute=None):
        self.kernel = kernel
        self.C = C
        self.gamma = gamma
        self.svc = None
        self.attribute = attribute

    def fit(self, X, y):
        self.svc = SVC(kernel=self.kernel, C=self.C, gamma=self.gamma, probability=True)
        self.svc.fit(X, y[self.attribute])

    def predict(self, X):
        if self.svc is None:
            raise ValueError("SVC model has not been trained yet. Please call 'fit' first.")
        return self.svc.predict(X)

    def predict_proba(self, X):
        if self.svc is None:
            raise ValueError("SVC model has not been trained yet. Please call 'fit' first.")
        return self.svc.predict_proba(X)
    
    def calculate_accuracy_score(self, X, y, y_pred=None):
        if self.svc is None:
            raise ValueError("SVC model has not been trained yet. Please call 'fit' first.")
        
        if y_pred is not None:
            accuracy = accuracy_score(y[self.attribute], y_pred)
            return accuracy
        
        y_pred = self.predict(X)
        accuracy = accuracy_score(y[self.attribute], y_pred)
        return accuracy
    
    def calculate_f1_score(self, X, y, y_pred=None):
        if self.svc is None:
            raise ValueError("SVC model has not been trained yet. Please call 'fit' first.")

        if y_pred is not None:
            if y[self.attribute].nunique() < 3:
                f1 = f1_score(y[self.attribute], y_pred)
            else:
                f1 = f1_score(y[self.attribute], y_pred, average='micro')
            return f1

        y_pred = self.predict(X)
        if y[self.attribute].nunique() < 3:
            f1 = f1_score(y[self.attribute], y_pred)
        else:
            f1 = f1_score(y[self.attribute], y_pred, average='micro')
        return f1
    
    def calculate_precision_score(self, X, y, y_pred=None):
        if self.svc is None:
            raise ValueError("SVC model has not been trained yet. Please call 'fit' first.")
        
        if y_pred is not None:
            if y[self.attribute].nunique() < 3:
                precision = precision_score(y[self.attribute], y_pred)
            else:
                precision = precision_score(y[self.attribute], y_pred, average='micro')
            return precision
        
        y_pred = self.predict(X)
        if y[self.attribute].nunique() < 3:
            precision = precision_score(y[self.attribute], y_pred)
        else:
            precision = precision_score(y[self.attribute], y_pred, average='micro')
        return precision
    
    def calculate_recall_score(self, X, y, y_pred=None):
        if self.svc is None:
            raise ValueError("SVC model has not been trained yet. Please call 'fit' first.")
        
        if y_pred is not None:
            if y[self.attribute].nunique() < 3:
                recall = recall_score(y[self.attribute], y_pred)
            else:
                recall = recall_score(y[self.attribute], y_pred, average='micro')
            return recall
        
        y_pred = self.predict(X)
        if y[self.attribute].nunique() < 3:
            recall = recall_score(y[self.attribute], y_pred)
        else:
            recall = recall_score(y[self.attribute], y_pred, average='micro')
        return recall