name=''
mailto=''
mailcontent=''
def get_intent(data):
    global name
    global mailto
    global mailcontent
    m=data['message'].lower()
    ## If the intent is about name i.e the first input by the user.
    if data['key'] =="name":
        name=m
        return "next"
    ## If the user answered to the question ( enter the mail ID )
    elif data['key']=="Email-Id":
        mailto=m
        return "content"
    ## If the user added the content that is to be sent, then sendemail intent is called
    elif data['key']=="content" :
        mailcontent=m
        return "sendemail"
    ## If the user wants to search for a particular question
    elif data['key']=="Question":
        return "wikipedia"
    ## Search on wikipedia
    elif any(x in m for x in ["search" , "wikipedia"]):
        return "search"
    ## If the user wants to send email
    elif any(x in m for x in ["send","mail","inform","email"]):
        return "email"
    ## To know the current time
    elif any(x in m for x in ["time","currenttime"]):
        return "time"
    ## Thanking message
    elif any(x in m for x in ["Thank you","thankyou","thanks","thank you"]):
        return "thank"
    ## If the user wants to play a game
    elif any(x in m for x in ["game","play","hangman","playing","games"]):
        return "game"
    ## default page
    else :
        return "echo"

def handle(data):
    global name
    from flask import render_template
    intent=get_intent(data)
    ## Asking for what to search
    if intent == "search":
        return render_template('messages/mail.html',
        question={"key":"Question","text":"What do you want to search?"})
    ## To search the question on wikipedia
    elif intent =="wikipedia":
        from .wikipedia import getdata
        searchdata=getdata(data)
        return render_template('messages/wikiresult.html',
        searchdata=searchdata,
        question={"key":"task","text":""})
    ## Take the email ID as input
    elif intent == "email":
        return render_template('messages/mail.html',
        question={"key":"Email-Id","text":"Please enter the recipient Email ID"})
    ## Asking the user to enter the content to be sent
    elif intent == "content" :
        return render_template('messages/mail.html',
        question={"key":"content","text":"Please enter the content that you want to send to the recipient"})
    ## Activating sendemail function to send the mail to the particular person
    elif intent == "sendemail" :
        from .mail import sendmailto
        mailmsg = sendmailto(mailto,mailcontent)
        return render_template('messages/sendemail.html',
        mailmsg=mailmsg,
        question={"key":"task","text":""})
    ## Greeting the user
    elif intent == "next":
        return render_template('messages/greet.html',
        name=name,
        question={"key":"task","text":"Please let me know which task you would like to perform"})
    ## Activated to know the current time
    elif intent == "time" :
        from .time import gettime
        timemsg=gettime()
        return render_template('messages/sendtime.html',
        timemsg="The current time is "+timemsg,
        question={"key":"task","task":""})
    ## Thanking message
    elif intent=="thank":
        return render_template('messages/thank.html',
        question={'key':'','text':''})
    ## Game page
    elif intent == "game" :
        return render_template('gameinput.html',
        question={"key":"task","task":""})
    else:
        return render_template('messages/reply.html',
        question={'key':'','text':''})
        
