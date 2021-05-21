## Function to print the current time
import datetime

def gettime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    return strTime