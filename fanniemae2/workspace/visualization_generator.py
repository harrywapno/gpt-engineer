import matplotlib.pyplot as plt
import joblib

class VisualizationGenerator:
    def __init__(self):
        pass
    
    def generate_visualizations(self, X_test, y_test, model):
        # Load the trained model from disk
        model = joblib.load('model.joblib')
        
        # Make predictions on the test data
        y_pred = model.predict(X_test)
        
        # Generate a confusion matrix
        fig, ax = plt.subplots()
        ax.imshow(confusion_matrix(y_test, y_pred), cmap='Blues')
        ax.set_xlabel('Predicted labels')
        ax.set_ylabel('True labels')
        ax.set_xticklabels(['', 'No Default', 'Default'])
        ax.set_yticklabels(['', 'No Default', 'Default'])
        ax.set_title('Confusion Matrix')
        plt.savefig('confusion_matrix.pdf')
        
        # Generate a ROC curve
        fig, ax = plt.subplots()
        fpr, tpr, _ = roc_curve(y_test, y_pred)
        ax.plot(fpr, tpr)
        ax.plot([0, 1], [0, 1], linestyle='--')
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('ROC Curve')
        plt.savefig('roc_curve.pdf')
