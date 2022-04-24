import xmlrpc.client

from lab2.classes.MusicStoreDatabaseManager import parse_albums, parse_authors
from lab4.config import HOST, PORT


class ClientRCP:
    def __init__(self):
        self.server_proxy = xmlrpc.client.ServerProxy('http://' + HOST + ':' + PORT.__str__())

    def get_all_authors(self) -> str:
        try:
            authors, field = self.server_proxy.get_all_authors()
            return parse_authors(authors, field)
        except Exception as e:
            return "Error while getting authors: " + str(e)

    def get_all_albums(self) -> str:
        try:
            albums, field = self.server_proxy.get_all_albums()
            return parse_albums(albums, field)
        except Exception as e:
            return "Error while getting albums: " + str(e)

    def get_all_albums_of_author_by_id(self, author_id: int) -> str:
        try:
            albums, field = self.server_proxy.find_album_by_condition("author_id", author_id, "*")
            return parse_albums(albums, field)
        except Exception as e:
            return "Error while getting albums of author: " + str(e)

    def add_new_author(self, author_id: int, name: str) -> str:
        if self.server_proxy.add_new_author(author_id, name):
            return "Successfully added author " + name
        else:
            return "Error while adding author"

    def add_new_album(self, album_id: int, name: str, number_of_songs: int, author_id: int) -> str:
        if self.server_proxy.add_new_album(album_id, name, number_of_songs, author_id):
            return "Successfully added album " + name
        else:
            return "Error while adding album"

    def delete_author_by_id(self, author_id: int) -> str:
        if self.server_proxy.delete_author_by_id(author_id):
            return "Successfully deleted author with id " + str(author_id)
        else:
            return "Error while deleting author"

    def delete_album_by_id(self, album_id: int) -> str:
        if self.server_proxy.delete_album_by_id(album_id):
            return "Successfully deleted album with id " + str(album_id)
        else:
            return "Error while deleting album"

    def change_author_by_id(self, author_id: int, name: str) -> str:
        if self.server_proxy.change_author(author_id, name):
            return "Author with id " + str(author_id) + " successfully updated"
        else:
            return "Error while changing author"

    def count_author_albums_by_id(self, author_id):
        try:
            albums, _ = self.server_proxy.find_album_by_condition("author_id", author_id, "name")
            return "Author with id " + str(author_id) + " has " + str(len(albums)) + " albums"
        except Exception as exception:
            return "Error while getting author's albums: " + str(exception)
