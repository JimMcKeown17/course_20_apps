import requests
import os
import smtplib, ssl
# from dotenv import load_dotenv
# load_dotenv()

topic = "apple"

api_key = os.getenv("NEWS")
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-06-27&" \
      "sortBy=publishedAt&" \
      "apiKey="+ api_key + "&" \
      "language=en"

request = requests.get(url)
content = request.json()
print(content)

body = ""
for article in content['articles'][0:20]:
    title = article['title'] if article['title'] else "No Title"
    description = article['description'] if article['description'] else "No Description"
    art_url = article['url'] if article['url'] else "No URL"

    body = "Subject: Today's news" + "\n" + body + title + "\n" + description + "\n" + art_url + "\n\n"
def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    password = os.getenv("PASSWORD")
    username = "qhawelamawele@gmail.com"
    receiver = "qhawelamawele@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

body = body.encode("utf-8")
send_email(body)