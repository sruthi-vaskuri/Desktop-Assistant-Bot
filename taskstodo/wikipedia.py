## Search in wikipedia and print the first statement taken from the wikipedia
import wikipedia

def getdata(data):
    query=data['message'].lower()
    try:
        ## searching the particular question in wikipedia
        results = wikipedia.summary(query, sentences=1)
    except Exception as e :
        ## If no result is found,then it executes exception block
        results = "No result found.Please try again"
    return results