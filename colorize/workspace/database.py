import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("movies.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS movies (title TEXT, year INTEGER, file_path TEXT)")
        self.connection.commit()
        
    def add_movie(self, movie):
        # Code to add a movie to the database
        
    def get_movies(self):
        # Code to retrieve the list of movies from the database
        # Returns a list of Movie objects
        
