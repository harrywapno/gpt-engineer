from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class MachineLearningModel:
    def __init__(self, X, y):
        self.X = X
        self.y = y
    
    def train_test_split(self):
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        
        return X_train, X_test, y_train, y_test
    
    def train_model(self, X_train, y_train):
        # Train a linear regression model on the training data
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        return model
    
    def test_model(self, model, X_test, y_test):
        # Test the model on the testing data
        score = model.score(X_test, y_test)
        
        return score
