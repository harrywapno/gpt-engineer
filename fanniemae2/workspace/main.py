from data_processor import DataProcessor
from model_trainer import ModelTrainer
from model_evaluator import ModelEvaluator
from visualization_generator import VisualizationGenerator

# Read and preprocess the data
data_processor = DataProcessor()
X_train, y_train, X_test, y_test = data_processor.read_and_preprocess_data()

# Train the model
model_trainer = ModelTrainer()
model = model_trainer.train_model(X_train, y_train)

# Evaluate the model
model_evaluator = ModelEvaluator()
evaluation_metrics = model_evaluator.evaluate_model(model, X_test, y_test)

# Generate visualizations
visualization_generator = VisualizationGenerator()
visualization_generator.generate_visualizations(X_test, y_test, model)
