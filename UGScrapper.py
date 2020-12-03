import HTMLParser
import requests
from bs4 import BeautifulSoup


def getUGData():
    response = requests.get('https://ug.edu.pl/news/pl/category/13/archiwum')
    htmlBase = BeautifulSoup(response.content, 'html.parser')
    listOfUGUrls = HTMLParser.getListOfUGUrls(htmlBase)

    resultSet = list()
    for url in listOfUGUrls:
        response = requests.get('https://ug.edu.pl' + url)
        htmlBase = BeautifulSoup(response.text, 'html.parser')
        resultSet.append(htmlBase)
