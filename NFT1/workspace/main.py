from fractal_generator import FractalGenerator
from gui import GUI
from neural_net import NeuralNet
from database import Database

def main():
    # Initialize classes
    fractal_generator = FractalGenerator()
    gui = GUI()
    neural_net = NeuralNet()
    database = Database()

    # Generate fractal art
    fractal_art = fractal_generator.generate()

    # Display fractal art in GUI
    gui.display(fractal_art)

    # Store fractal art in database
    database.store(fractal_art)

    # Train neural net using fractal art
    neural_net.train(fractal_art)

if __name__ == "__main__":
    main()
