from data_preprocessing import DataPreprocessing
from machine_learning_model import MachineLearningModel
from visualization import Visualization

class Pipeline:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_preprocessing = DataPreprocessing(file_path)
        self.machine_learning_model = None
        self.visualization = None
        
    def run(self):
        # Load and preprocess the data
        self.data_preprocessing.load_data()
        self.data_preprocessing.clean_data()
        self.data_preprocessing.prepare_data()
        
        # Train and test the machine learning model
        self.machine_learning_model = MachineLearningModel(self.data_preprocessing.X, self.data_preprocessing.y)
        self.machine_learning_model.split_data()
        self.machine_learning_model.train_model()
        score = self.machine_learning_model.test_model()
        
        # Create visualizations of the data and the model's predictions
        self.visualization = Visualization(self.data_preprocessing.X, self.data_preprocessing.y, self.machine_learning_model.model)
        self.visualization.plot_data()
        self.visualization.plot_model()
        
        return score
