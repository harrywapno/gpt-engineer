from movie import Movie
from colorizer import Colorizer
from database import Database
from frontend import Frontend

# Create instances of the necessary classes
colorizer = Colorizer()
database = Database()
frontend = Frontend()

# Train the colorizer on the existing colorized movies
colorizer.train_on_colorized_movies()

# Convert color movies to black and white and add them to the training set
colorizer.add_black_and_white_movies_to_training_set()

# Train the colorizer on the expanded training set
colorizer.train_on_expanded_training_set()

# Retrieve the list of movies from the database
movies = database.get_movies()

# Display the movies on the front-end webpage
frontend.display_movies(movies)
