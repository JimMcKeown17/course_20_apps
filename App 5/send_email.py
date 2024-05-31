import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "qhawelamawele@gmail.com"
    password = "otohevxctnchtxkc"

    receiver = "qhawelamawele@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email("Hey, does this work?")