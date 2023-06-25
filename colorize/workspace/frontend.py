from flask import Flask, render_template
from movie import Movie
from database import Database
import os

class Frontend:
    def __init__(self):
        self.app = Flask(__name__)
        self.database = Database()
        
        @self.app.route("/")
        def index():
            movies = self.database.get_movies()
            return render_template("index.html", movies=movies)
        
        @self.app.route("/movie/<title>")
        def movie(title):
            movie = self.database.get_movie_by_title(title)
            return render_template("movie.html", movie=movie, colorized_movie_path=self.colorize_movie(movie))
        
        self.app.run()
        
    def display_movies(self, movies):
        # Code to display the movies on the front-end webpage
        
    def colorize_movie(self, movie):
        # Code to call the colorization algorithm to colorize the movie
        # Returns the file path of the colorized movie
        
