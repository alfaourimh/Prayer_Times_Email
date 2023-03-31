import smtplib, ssl
from Web_info_test import fajr,sunrise,dhuhr,asr,maghrib,isha
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver

def send_mail():
    server = "smtp.gmail.com"
    port = 587
    password = "email_password"
    sender_address = "email_address"
    receiver_address = "receiver_email_address"
    
    msg = MIMEMultipart()
    msg['Subject'] = 'Your Day'
    msg['From'] = sender_address
    msg['To'] = receiver_address
    
    html ="""\
        <html>
        <body>
        <br>You have work from 8:00-5:00</br>
        <br>You have no class today</br>
        <br>Prayer Times are the following:</br>
        <table style = Border-Style: "Solid">
        <th>&#xFDFD;</th>
        <tr>
        <li>"""+(fajr)+"""</li>
        <li>"""+(sunrise)+"""</li>
        <li>"""+(dhuhr)+"""</li>
        <li>"""+(asr)+"""</li>
        <li>"""+(maghrib)+"""</li>
        <li>"""+(isha)+"""</li>
        </tr>
        </table>
        <br>You may want to improve this project or start a new one!</br>
        </body>
        </html>
        """ 
    msg.attach(MIMEText(html,'html'))
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(server, port) as smtpObj:
             smtpObj.ehlo()
             smtpObj.starttls()
             smtpObj.login(sender_address, password)
             smtpObj.sendmail(sender_address, receiver_address, msg.as_string())
    except Exception as e:
        print(e)
send_mail()
