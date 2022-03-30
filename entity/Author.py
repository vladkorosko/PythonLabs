from entity.Album import Album
from entity.Album import print_albums


class Author:
    def __init__(self, author_id: int, name: str):
        self.author_id = author_id
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        self.albums.append(album)


def print_author(author: Author) -> None:
    print("Author id: " + str(author.author_id) + "; Author name: " + author.name + "")
    print_albums(author.albums, '\t')

def print_authors(authors: [Author]) -> None:
    print("The authors are: ")
    print("\n-----------------------------------------------\n")
    for i in authors:
        print_author(i)