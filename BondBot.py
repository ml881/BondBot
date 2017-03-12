import json
from random import randint

LITERAL_QUOTE = "\""
QUOTES_PATH = "quotes.json"
MAX_QUOTE_LENGTH = 140

def buildQuote(quoteDict):
    quoteString = quoteDict["Quote"]
    filmString = "--" + quoteDict["Film"]

    returnString = LITERAL_QUOTE + quoteString + LITERAL_QUOTE + filmString

    if len(returnString) > MAX_QUOTE_LENGTH:
        filmStringSize = len(filmString)
        #plus two for the quote makes
        remainder = (filmStringSize + 2) - MAX_QUOTE_LENGTH
        trimmedQuoteString = quoteString[:-remainder]
        returnString = LITERAL_QUOTE + trimmedQuoteString + LITERAL_QUOTE + filmString

    print(len(returnString))
    return returnString

def loadQuotes():
    quotes=open(QUOTES_PATH).read()
    quotesDict = json.loads(quotes)
    return quotesDict

def selectQuote(quotesList):
    numOfQuotes = len(quotesList) -1
    i = randint(0,numOfQuotes)
    return buildQuote(quotesList[i])

########################
##########MAIN##########
#######################
print("Bond Bot")

quotesList = loadQuotes()

nextQuote = selectQuote(quotesList)

print(nextQuote)
