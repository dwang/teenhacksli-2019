from pymongo import MongoClient
import random
import json
import logging

logging.basicConfig(filename="newsServer.log", level=logging.INFO)

db = MongoClient("127.0.0.1", 5000, connect=False)['hacktcnj']
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
