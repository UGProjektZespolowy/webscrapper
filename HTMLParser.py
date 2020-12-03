import re


def getListOfMFIUrls(htmlBase):
    result = htmlBase.find_all('div', class_='col-md-6')
    resultSet = list()
    for result_elem in result:
        resultSet.append(result_elem.find('a')['href'])
        if re.search('http.*', resultSet[len(resultSet) - 1]):
            resultSet.pop(len(resultSet) - 1)
    return resultSet


def getListOfUGUrls(htmlBase):
    result = htmlBase.find_all('div', class_='row mt-2 mb-5')
    resultSet = list()
    for result_elem in result:
        resultSet.append(result_elem.find('a')['href'])
    return resultSet


def getListOfInfUrls(htmlBase):
    result = htmlBase.find_all('div', class_='newsBox')
    resultSet = list()
    for result_elem in result:
        resultSet.append(result_elem.find('a')['href'])
    return resultSet
