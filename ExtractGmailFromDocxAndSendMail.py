'''Python script to extract gmail id from given all short listed resume files given in .docx format in a folder
and send a mail to those mail id saying that resume is short listed for next round interview'''

import os
import re
import docx2txt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


Allgmail = []
mail_content = '''Hi, 

we are pleased to inform you that your resume is short listed for next round interview.
this is system generated mail so please don't replay anything.

kindly contact to mobile number : 7795378925

Thanks and Regards,
xyz recruiter.'''

sender_address = 'xyz123@gmail.com'
sender_pass = 'password'

path = 'C:\\Users\\che53832\\Desktop\\allresme2'
files = os.listdir(path)

for f in files:

    filePath = os.path.join(path, f)
    txt = docx2txt.process(filePath)

    email = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")
    match1 = email.finditer(txt)

    for x in match1:
        g = x.group(0)
        Allgmail.append(g)


for gmail in Allgmail:
    receiver_address = gmail
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = gmail
    message['Subject'] = 'xyz company recruiter'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent successfully to ',gmail)

print("All mail sent successfully")



