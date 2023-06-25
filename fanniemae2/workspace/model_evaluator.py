from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

class ModelEvaluator:
    def __init__(self):
        pass
    
    def evaluate_model(self, model, X_test, y_test):
        # Load the trained model from disk
        model = joblib.load('model.joblib')
        
        # Make predictions on the test data
        y_pred = model.predict(X_test)
        
        # Calculate evaluation metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        evaluation_metrics = {'accuracy': accuracy, 'precision': precision, 'recall': recall, 'f1': f1}
        
        return evaluation_metrics
