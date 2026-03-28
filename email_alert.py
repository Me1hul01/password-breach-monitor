import smtplib
import sys
from email.message import EmailMessage
from string import Template
from pathlib import Path
from datetime import datetime
from checker import main


args = sys.argv[1:]
Result = main(args)




now = datetime.now()
current_time = now.strftime("%m/%d/%Y %I:%M:%S %p")

if Result:
    html = Template(Path("Alert.html").read_text())
    email = EmailMessage()
    email['From'] = 'example1@gmail.com'
    email['To'] = 'example2@gmail.com'
    email['Subject'] = 'Breach Alert'



    html_content = html.substitute(
    alert=Result,
    present_time=current_time
)
    email.set_content(html_content, subtype="html")





    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
     smtp.ehlo()
     smtp.starttls()
     smtp.login('example1@gmail.com', "Email_Pass")
     smtp.send_message(email)
     smtp.quit()


    print("Email sent")
else:
    print("Email not sent")