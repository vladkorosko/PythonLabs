from entity.Album import Album


class Author:
    def __init__(self, author_id: int, name: str):
        self.author_id = author_id
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        self.albums.append(album)
        