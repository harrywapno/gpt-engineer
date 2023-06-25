from sklearn.ensemble import RandomForestClassifier
import joblib

class ModelTrainer:
    def __init__(self):
        pass
    
    def train_model(self, X_train, y_train):
        # Train a random forest classifier on the training data
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Save the trained model to disk
        joblib.dump(model, 'model.joblib')
        
        return model
