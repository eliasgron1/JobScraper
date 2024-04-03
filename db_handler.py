import mysql.connector
import credentials
import duunitori_scraper

class Database_Master:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host=credentials.HOST,
        user=credentials.USER,
        password=credentials.PASSWORD,
        database = credentials.DATABASE,
        auth_plugin='mysql_native_password'
        )
        self.mycursor = self.mydb.cursor()
        print(self.mydb)    # Check connection status

    def create_sql(self,listing_date,company_name,job_name,location,link):
        sql = "INSERT INTO listings (listing_date,company_name,job_name,location,link) VALUES (%s, %s, %s, %s, %s)"
        values = (listing_date, company_name, job_name, location, link)
        self.mycursor.execute(sql, values)

    def commit_sql(self):
        self.mydb.commit()

