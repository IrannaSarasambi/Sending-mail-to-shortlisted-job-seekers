'''Python script to extract gmail id from given all short listed resume files given in .Pdf format in a folder
and send a mail to those mail id saying that resume is short listed for next round interview'''

import PyPDF2
import re
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

Allgmail = []
mail_content = '''Hi, 

we are pleased to inform you that your resume is short listed for next round interview.
this is system generated mail so please don't replay anything.

kindly contact to mobile number : 7795378925(Irgaa)

Thanks and Regards,
xyz recruiter.'''

sender_address = 'abcd123@gmail.com'
sender_pass = 'password'



path = 'C:\\Users\\che53832\\Desktop\\allpdf'
files = os.listdir(path)


for pdf in files:

    filePath = os.path.join(path, pdf)
    pdfread = PyPDF2.PdfFileReader(filePath)
    page = pdfread.getPage(0)
    pageinfo = page.extractText()

    email = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")
    match1 = email.finditer(pageinfo)

    for x in match1:
        g = x.group(0)
        Allgmail.append(g)



for gmail in Allgmail:
    receiver_address = 'irannass@gmail.com'
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
