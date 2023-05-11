from dotenv import load_dotenv
import os

import mysql.connector

load_dotenv()

class DBAccess():

    def connection(self):
        mydb = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_DATABASE")
        )
        return mydb

    def create(self):
        mydb = self.connection()
        cursor = mydb.cursor()
        cursor.execute("CREATE TABLE Movies (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), imdb_id VARCHAR(255), uri VARCHAR(255), year VARCHAR(255))")
        mydb.close()
        return mydb
    
    def save(self, val):
        mydb = self.connection()
        cursor = mydb.cursor()
        
        sql = "INSERT INTO Movies (title, imdb_id, uri, year) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, val)
        
        mydb.commit()
        mydb.close()
        return mydb
