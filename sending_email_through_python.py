import smtplib
from email.mime.text import MIMEText
content=input("Enter the text to be mailed:")
msg=MIMEText(content)
fromaddr=input("Sender email id:")
toaddr=input("Receiver email id:")
pw=input("Login password of sender:")
msg['From']=fromaddr
msg['To']=toaddr
msg['subject']="Test mail from Isha using python"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,pw)
server.send_message(msg)
server.quit()
print("Mail is sent")