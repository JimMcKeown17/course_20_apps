import requests
import selectorlib
import smtplib
import ssl
import time
import sqlite3
import os

EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
print(EMAIL_PASSWORD)

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class Event:
    def scrape(self,url):
        response = requests.get(url)
        source = response.text
        return source

    def extract(self,source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)['tours']
        return value

class Email():
    def send(self, message):
        host = "smtp.gmail.com"
        port = 465

        username = "qhawelamawele@gmail.com"
        password = "hidden"

        receiver = "qhawelamawele@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)


class Database:
    def __init__(self, database_path):
        self.connection = sqlite3.Connection(database_path)

    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()
    def read(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        print(rows)
        return rows

if __name__ == "__main__":
    while True:
        event = Event()
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)
        if extracted != "No upcoming tours":
            database = Database(database_path='data.db')
            row = database.read(extracted)
            if not row:
                database.store(extracted)
                email = Email()
                email.send(message="Hey, new event was found")
        time.sleep(2)