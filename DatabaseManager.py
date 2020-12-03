import pymongo
import HTMLResult


def updateMFIDatabase(data):
    client = pymongo.MongoClient(
        "mongodb+srv://ugAdmin:ugAdmin@htmldatabase.pjivs.mongodb.net/sample_airbnb?retryWrites"
        "=true&w=majority")
    database = client["scrapper_result"]
    collection = database["scrapperMFI_result"]
    query = {"News": str(data.text)}

    if not collection.find_one(query):
        preparedData = {"News": str(data.text), "Image": str(data.image), "Header": str(data.htmlHeader), "Title": str(data.title)}
        collection.insert_one(preparedData)


def updateUGDatabase(data):
    client = pymongo.MongoClient(
        "mongodb+srv://ugAdmin:ugAdmin@htmldatabase.pjivs.mongodb.net/sample_airbnb?retryWrites"
        "=true&w=majority")
    database = client["scrapper_result"]
    collection = database["scrapperUG_result"]
    query = {"News": str(data.text)}

    if not collection.find_one(query):
        preparedData = {"News": str(data.text), "Image": str(data.image), "Header": str(data.htmlHeader), "Title": str(data.title)}
        collection.insert_one(preparedData)


def updateInfDatabase(data):
    client = pymongo.MongoClient(
        "mongodb+srv://ugAdmin:ugAdmin@htmldatabase.pjivs.mongodb.net/sample_airbnb?retryWrites"
        "=true&w=majority")
    database = client["scrapper_result"]
    collection = database["scrapperInf_result"]
    query = {"News": str(data.text)}

    if not collection.find_one(query):
        preparedData = {"News": str(data.text), "Image": str(data.image), "Header": str(data.htmlHeader), "Title": str(data.title)}
        collection.insert_one(preparedData)


def removeAll():
    client = pymongo.MongoClient(
        "mongodb+srv://ugAdmin:ugAdmin@htmldatabase.pjivs.mongodb.net/sample_airbnb?retryWrites"
        "=true&w=majority")
    database = client["scrapper_result"]
    collection = database["scrapperInf_result"]
    collection.remove()
    collection = database["scrapperMFI_result"]
    collection.remove()
    collection = database["scrapperUG_result"]
    collection.remove()
