##  Function to send email to particular person 
import smtplib

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    ## Automatic login by the server
    server.login('sruthisrinivas0@gmail.com', 'Vaskuri@s981')
    server.sendmail('sruthisrinivas0@gmail.com', to, content)
    server.close()

def sendmailto(mailto,mailcontent):
    try:
        ## sending mail to the given mail ID along with the content
        emailid=mailto   
        sendEmail(emailid,mailcontent)
        mailmsg = "Email Sent"
    except Exception as e:
        print(e)
        mailmsg = "Sorry my friend ! I am not able to send this email"
    return mailmsg
