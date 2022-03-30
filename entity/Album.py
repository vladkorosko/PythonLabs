class Album:
    def __init__(self, album_id: int, name: str, number_of_songs: int, author_id: int):
        self.album_id = album_id
        self.name = name
        self.number_of_songs = number_of_songs
        self.author_id = author_id


def print_album(album: Album, padding: str) -> None:
    print(padding + "Album id: " + str(album.album_id) + "; Album name: " + album.name +
          "; Number of songs: " + str(album.number_of_songs) + "; Album author: " + str(album.author_id))


def print_albums(list_of_albums: [Album], padding: str) -> None:
    print("The albums are: ")
    for i in list_of_albums:
        print_album(i, padding)
    print("\n-----------------------------------------------\n")