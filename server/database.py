from pymongo import MongoClient
import random
import json
import logging

logging.basicConfig(filename="newsServer.log", level=logging.INFO)

db = MongoClient("35.236.226.124", 27017, connect=False)['teenhacksli']
posts = db.posts


def addData(article_title, content, genre):
    post = {
        "Title: ":article_title,
        "Content: ":content,
        "Genre: ":genre
    }

    logging.info(post)
    posts.insert_one(post)


def getData():
    returnValue = []

    for document in posts.find({}):
        returnValue.append(document)

    return returnValue


def clearDatabase():
    posts.delete_many({})


if __name__ == "__main__":
    clearDatabase()
    addData("hi", "hello", "bye")
    print(getData())
