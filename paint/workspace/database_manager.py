import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect("image_database.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates a table for storing image data.
        """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS images
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            path TEXT NOT NULL,
                            difficulty INTEGER NOT NULL)''')
        self.conn.commit()

    def insert_image(self, name, path, difficulty):
        """
        Inserts image data into the database.
        """
        self.cursor.execute("INSERT INTO images (name, path, difficulty) VALUES (?, ?, ?)", (name, path, difficulty))
        self.conn.commit()

    def get_images(self):
        """
        Retrieves all image data from the database.
        """
        self.cursor.execute("SELECT * FROM images")
        return self.cursor.fetchall()
