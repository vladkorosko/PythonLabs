from lab2.classes.MusicStoreDatabaseManager import MusicStoreDataBaseManager
from lab2.classes.MusicStoreDatabaseManager import parse_albums
from lab2.classes.MusicStoreDatabaseManager import parse_authors

import os

def process(data: str) -> str:
    manager = MusicStoreDataBaseManager()
    split = data.split("#")
    if split[0] == "add_new_author":
        if manager.add_new_author(int(split[1]), split[2]):
            return "Successfully added author " + split[2]
        else:
            return "Error while adding author"
    if split[0] == "add_new_album":
        if manager.add_new_album(int(split[1]), split[2], int(split[3]), int(split[4])):
            return "Successfully added album " + split[2]
        else:
            return "Error while adding album"

    if split[0] == "delete_author_by_id":
        if manager.delete_author_by_id(int(split[1])):
            return "Successfully deleted author with id " + split[1]
        else:
            return "Error while deleting author"
    if split[0] == "delete_album_by_id":
        if manager.delete_album_by_id(int(split[1])):
            return "Successfully deleted album with id " + split[1]
        else:
            return "Error while deleting album"

    if split[0] == "change_author_by_id":
        if manager.change_author(int(split[1]), split[2]):
            return "Author with id " + split[1] + " successfully updated"
        else:
            return "Error while changing author"

    if split[0] == "count_albums_author_by_id":
        try:
            albums, _ = manager.find_album_by_condition("author_id", split[1], "name")
            return "Author with id " + split[1] + " has " + str(len(albums)) + " albums"
        except Exception as exception:
            return "Error while getting author's albums: " + str(exception)

    if split[0] == "get_all_authors":
        authors, field = manager.get_all_authors()
        return parse_authors(authors, field)
    if split[0] == "get_all_albums":
        albums, field = manager.get_all_albums()
        return parse_albums(albums, field)
    if split[0] == "get_all_albums_of_author_by_id":
        albums, field = manager.find_album_by_condition("author_id", split[1], "*")
        return parse_albums(albums, field)

response = ""

with open("requests.txt", "r") as requests:
    while True:
        line = requests.readline()
        if not line:
            break
        response += line
        response += "\n"
        request = line[:-1]
        result = process(request)
        if result:
            response += result
            response += "\n########################################################\n"

os.remove("requests.txt")

with open("responses.txt", "a+") as responses:
    responses.write(response)
    responses.write("\n")
