import HTMLParser
import requests
import DatabaseManager
import HTMLResult
from bs4 import BeautifulSoup


def getMFIData():
    response = requests.get('https://mfi.ug.edu.pl/wydzial_mfi/aktualnosci')
    htmlBase = BeautifulSoup(response.content, 'html.parser')
    listOfMFIUrls = HTMLParser.getListOfMFIUrls(htmlBase)

    resultSet = list()
    for url in listOfMFIUrls:
        subresult = HTMLResult.Result()
        response = requests.get('https://mfi.ug.edu.pl' + url)

        htmlBase = BeautifulSoup(response.content, 'html.parser')
        for element in htmlBase.find('head').contents:
            subresult.htmlHeader = subresult.htmlHeader + str(element)
        for element in htmlBase.find('div', class_='field field-name-body').contents:
            subresult.text = subresult.text + str(element)
        subresult.title = htmlBase.find('div', class_='field field-name-title').find('h1').contents[0]
        subset = htmlBase.find_all('div',
                                   class_='field field--name-field-zdjecie field--type-image field--label-hidden field__item')
        for result_elem in subset:
            subresult.image = result_elem.find('img')['src']

        resultSet.append(subresult)
    for subresult in resultSet:
        DatabaseManager.updateMFIDatabase(subresult)


def getUGData():
    response = requests.get('https://ug.edu.pl/news/pl/category/13/archiwum')
    htmlBase = BeautifulSoup(response.content, 'html.parser')
    listOfUGUrls = HTMLParser.getListOfUGUrls(htmlBase)

    resultSet = list()
    for url in listOfUGUrls:
        subresult = HTMLResult.Result()
        response = requests.get('https://ug.edu.pl' + url)
        htmlBase = BeautifulSoup(response.content, 'html.parser')

        for element in htmlBase.find('head').contents:
            subresult.htmlHeader = subresult.htmlHeader + str(element)
        for element in htmlBase.find('div', class_='clearfix text-formatted field field--name-field-tekst field--type-text-long field--label-hidden field__item').contents:
            subresult.text = subresult.text + str(element)
        subresult.title = htmlBase.find('h3', class_='title').find('span').contents[0]
        subset = htmlBase.find_all('div', class_='field field--name-field-zdjecie field--type-image field--label-hidden field__item')
        for result_elem in subset:
            subresult.image = result_elem.find('img')['src']

        resultSet.append(subresult)
    for sub in resultSet:
        DatabaseManager.updateUGDatabase(sub)


def getInfData():
    response = requests.get('https://inf.ug.edu.pl/studinfo')
    htmlBase = BeautifulSoup(response.content, 'html.parser')
    listOfInfUrls = HTMLParser.getListOfInfUrls(htmlBase)

    resultSet = list()
    for url in listOfInfUrls:
        subresult = HTMLResult.Result()
        response = requests.get('https://inf.ug.edu.pl/' + url)
        htmlBase = BeautifulSoup(response.content, 'html.parser')
        for element in htmlBase.find('head').contents:
            subresult.htmlHeader = subresult.htmlHeader + str(element)
        for element in htmlBase.find('div', class_='artBody').contents:
            subresult.text = subresult.text + str(element)
        subresult.title = htmlBase.find('div', class_='artTitle').contents[0]
        subresult.image = htmlBase.find('div', class_='artThumb').find('img')['src']

        resultSet.append(subresult)
    for subresult in resultSet:
        DatabaseManager.updateInfDatabase(subresult)
