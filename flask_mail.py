# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


def sendmail(MailID,res):
    # Open the plain text file whose name is in textfile for reading.
    msg = EmailMessage()
    msg.set_content(res)
    
    fromid = "rasachatbot595@gmail.com"
    #toid = "@gmail.com"
    msg['Subject'] = 'Top rated restaurants'
    msg['From'] = fromid
    msg['To'] = MailID
    
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(fromid,"Rasachat@595")
    s.send_message(msg)
    s.quit()