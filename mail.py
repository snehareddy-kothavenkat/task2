import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from_addr = 'testuser3792@gmail.com'
to_addr= 'kvsnehareddy772@gmail.com'
text = '''Hello Developer!!! Your web page has failed to execute ,exited with error code!'''

username = 'testuser3792@gmail.com'
password = 'reddy@02'

msg = MIMEMultipart()

msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "Failure to execute Web Page"
msg.attach(MIMEText(text, 'plain'))


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
