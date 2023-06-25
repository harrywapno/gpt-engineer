import matplotlib.pyplot as plt

class Visualization:
    def __init__(self, X_test, y_test, model):
        self.X_test = X_test
        self.y_test = y_test
        self.model = model
    
    def create_scatter_plot(self):
        # Create a scatter plot of the predicted vs actual values
        y_pred = self.model.predict(self.X_test)
        plt.scatter(self.y_test, y_pred)
        plt.xlabel('Actual Values')
        plt.ylabel('Predicted Values')
        plt.title('Predicted vs Actual Values')
        plt.show()
