import smtplib, ssl

host = "smtp.gmail.com"
port = 465

password = "kfxcxjsndcajaedy"
username = "qhawelamawele@gmail.com"
receiver = "qhawelamawele@gmail.com"

context = ssl.create_default_context()

message = """   Subject: Happy Father's Day
Hi
How are you?
Bye!"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)