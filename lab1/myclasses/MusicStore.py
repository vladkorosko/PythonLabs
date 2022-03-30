from xml.dom.minidom import parse
from xml.dom.minidom import Document

from lxml import etree
from lxml.etree import XMLSyntaxError

from entity.Album import Album
from entity.Author import Author


class MusicStore:
    def __init__(self):
        self.__albums = []
        self.__authors = []

    def id_in_albums(self, album_id: int) -> bool:
        for album in self.__albums:
            if album.album_id == album_id:
                return True
        return False

    def id_in_authors(self, author_id: int) -> bool:
        for author in self.__authors:
            if author.author_id == author_id:
                return True
        return False

    def get_album_by_id(self, album_id: int) -> Album:
        for album in self.__albums:
            if album.album_id == album_id:
                return album
        raise Exception("Music store has no album with id: " + str(album_id))

    def get_album_by_index(self, index: int) -> Album:
        if index < len(self.__albums):
            return self.__albums[index]
        raise Exception("List index out of range")

    def get_author_by_id(self, author_id: int) -> Author:
        for author in self.__authors:
            if author.author_id == author_id:
                return author
        raise Exception("Music store has no author with id: " + str(author_id))

    def get_author_by_index(self, index: int) -> Author:
        if index < len(self.__authors):
            return self.__authors[index]
        raise Exception("List index out of range")

    def count_albums(self) -> int:
        return len(self.__albums)

    def count_authors(self) -> int:
        return len(self.__authors)

    def add_album(self, album_id: int, name: str, number_of_songs: int, author_id: int) -> None:
        album = Album(album_id, name, number_of_songs, author_id)
        if self.id_in_albums(album_id):
            raise Exception("Album with id " + str(album_id) + " exists in list")
        if self.id_in_authors(author_id):
            self.__albums.append(album)
            for i in range(len(self.__authors)):
                if self.__authors[i].author_id == author_id:
                    self.__authors[i].add_album(album)
        else:
            raise Exception("Author with id " + str(author_id) + " does not exists in list")

    def add_author(self, author_id: int, name: str) -> None:
        if self.id_in_authors(author_id):
            raise Exception("Author with id " + str(author_id) + " exists in list")
        self.__authors.append(Author(author_id, name))

    def delete_author_by_id(self, author_id: int) -> None:
        try:
            author = self.get_author_by_id(author_id)
            for album in author.albums:
                self.__albums.remove(album)
            self.__authors.remove(author)
        except Exception as e:
            raise e

    def delete_album_by_id(self, author_id: int) -> None:
        try:
            album = self.get_album_by_id(author_id)
            author_id = album.author_id
            for author in self.__authors:
                if author_id == author.author_id:
                    author.albums.remove(album)
                    break
            self.__albums.remove(album)
        except Exception as e:
            raise e

    def get_all_albums(self) -> [Album]:
        return self.__albums

    def get_all_authors(self) -> [Author]:
        return self.__authors

    def clear(self) -> None:
        self.__albums.clear()
        self.__authors.clear()

    def clear_albums(self) -> None:
        self.__albums.clear()
        for author in self.__authors:
            author.albums.clear()

    def change_album_name(self, album_id: int, new_name: str) -> None:
        if self.id_in_albums(album_id):
            author_id = self.__authors[0].author_id
            for album in self.__albums:
                if album.album_id == album_id:
                    album.name = new_name
                    author_id = album.author_id
            for author in self.__authors:
                if author.author_id == author_id:
                    for album in author.albums:
                        if album.album_id == album_id:
                            album.name = new_name
        else:
            raise Exception("Album with id " + str(album_id) + " doesn't exists in list")

    def change_number_of_songs(self, album_id: int, new_number_of_songs: int) -> None:
        if self.id_in_albums(album_id):
            author_id = self.__authors[0].author_id
            for album in self.__albums:
                if album.album_id == album_id:
                    album.number_of_songs = new_number_of_songs
                    author_id = album.author_id
            for author in self.__authors:
                if author.author_id == author_id:
                    for album in author.albums:
                        if album.album_id == album_id:
                            album.number_of_songs = new_number_of_songs
        else:
            raise Exception("Album with id " + str(album_id) + " doesn't exists in list")

    def change_author_name(self, author_id: int, new_name: str) -> None:
        if self.id_in_authors(author_id):
            for author in self.__authors:
                if author.author_id == author_id:
                    author.name = new_name
        else:
            raise Exception("Author with id " + str(author_id) + " doesn't exists in list")

    @staticmethod
    def __validate_xml(path_xml: str) -> bool:
        parser = etree.XMLParser(dtd_validation=True)
        try:
            etree.parse(path_xml, parser)
            print("Validation success")
            return True
        except XMLSyntaxError as e:
            print(e)
            return False

    def load_from_xml(self, path_xml: str) -> (int, int):
        if MusicStore.__validate_xml(path_xml):
            number_of_authors = 0
            number_of_albums = 0
            with parse(path_xml) as dom_tree:
                collection = dom_tree.documentElement
                authors = collection.getElementsByTagName("author")
                for author in authors:
                    author_id = author.getAttribute("author_id")
                    author_name = author.getAttribute("name")
                    try:
                        self.add_author(int(author_id), author_name)
                        number_of_authors += 1
                    except Exception as e:
                        print(e)

                    albums = author.getElementsByTagName("album")
                    for album in albums:
                        album_id = album.getAttribute("album_id")
                        album_name = album.getAttribute("name")
                        number_of_songs = album.getAttribute("number_of_songs")

                        try:
                            self.add_album(int(album_id), album_name, int(number_of_songs), int(author_id))
                            number_of_albums += 1
                        except Exception as e:
                            print(e)
            return number_of_authors, number_of_albums
        else:
            raise Exception("Validation failed")

    def save_to_xml(self, path_xml: str) -> (int, int):
        root = Document()

        xml_file = root.createElement('music_store')
        root.appendChild(xml_file)

        number_of_authors = 0
        number_of_albums = 0
        for author in self.get_all_authors():
            new_author_to_save = root.createElement("author")
            new_author_to_save.setAttribute("author_id", str(author.author_id))
            new_author_to_save.setAttribute("name", str(author.name))
            number_of_authors += 1

            for album in author.albums:
                new_album_to_save = root.createElement("album")
                new_album_to_save.setAttribute("album_id", str(album.album_id))
                new_album_to_save.setAttribute("name", str(album.name))
                new_album_to_save.setAttribute("number_of_songs", str(album.number_of_songs))
                new_author_to_save.appendChild(new_album_to_save)
                number_of_albums += 1

            xml_file.appendChild(new_author_to_save)

        element = etree.fromstring(root.toxml())
        etree.indent(element, space="\t")
        xml_str = etree.tostring(element, doctype='<!DOCTYPE music_store SYSTEM "sample.dtd">', encoding='UTF-8',
                                 pretty_print=True, xml_declaration=True)
        with open(path_xml, "wb") as f:
            f.write(xml_str)
        return number_of_authors, number_of_albums