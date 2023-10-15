#The data_loader.py module will be responsible for loading various types of data that the JarvisoBrain might need.
# For the sake of this implementation, I'll assume we're loading data from the SQLite database, but this can easily
# be extended to load from other sources in the future.

import sqlite3
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "..", "NeuralDatabase", "mainbrain.db")


class DataLoader:
    def __init__(self, database_path=DATABASE_PATH):
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

    def fetch_data(self, query, params=None):
        """
        Execute a query to fetch data from the database.

        Parameters:
            - query (str): SQL query to be executed.
            - params (tuple, optional): Values to be used in the SQL query for parameterized queries.

        Returns:
            - list: List of rows fetched from the database.
        """
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def insert_data(self, query, params):
        """
        Execute a query to insert data into the database.

        Parameters:
            - query (str): SQL query to be executed.
            - params (tuple): Values to be inserted into the database.
        """
        self.cursor.execute(query, params)
        self.connection.commit()

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()


if __name__ == "__main__":
    # Example usage:
    loader = DataLoader()

    # Fetching data example:
    rows = loader.fetch_data("SELECT * FROM some_table_name")
    for row in rows:
        print(row)

    # Inserting data example:
    insert_query = "INSERT INTO some_table_name (column1, column2) VALUES (?, ?)"
    example_value1 = "ExampleValue1"
    example_value2 = "ExampleValue2"
    loader.insert_data(insert_query, (example_value1, example_value2))

    loader.close()
