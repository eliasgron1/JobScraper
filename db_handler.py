import mysql.connector
import credentials
import duunitori_scraper

class Database_Master:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host=credentials.HOST,
        user=credentials.USER,
        password=credentials.PASSWORD
        )

    def push_to_db(self,data):
        pass

