from pymongo import MongoClient


def retrieve_game(id):
    client = MongoClient()
    db = client.database
    games = db.games
    games.find_one({id: id})
    return
