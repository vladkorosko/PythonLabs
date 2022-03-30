from lab1.myclasses.MusicStore import MusicStore
from entity.Author import Author
from entity.Album import Album


def print_album(album: Album, padding: str) -> None:
    print(padding + "Album id: " + str(album.album_id) + "; Album name: " + album.name +
          "; Number of songs: " + str(album.number_of_songs) + "; Album author: " + str(album.author_id))


def print_albums(list_of_albums: [Album], padding: str) -> None:
    print("The albums are: ")
    for i in list_of_albums:
        print_album(i, padding)
    print("\n-----------------------------------------------\n")


def print_author(author: Author) -> None:
    print("Author id: " + str(author.author_id) + "; Author name: " + author.name + "")


class Manager:
    def __init__(self, music_store: MusicStore, path_xml: str):
        self.music_store = music_store
        self.path_xml = path_xml

    def __add_album(self) -> None:
        continue_while = True
        first = True
        while continue_while:
            if not first:
                answer = input("Do you want to continue (y/n): ")
                if answer != 'y':
                    break
            else:
                first = False

            album_id = input("Enter new album's id: ")
            author_id = input("Enter author's id: ")
            name = input("Enter name of album: ")
            number_of_songs = input("Enter number of songs in album: ")
            if album_id.isnumeric() and author_id.isnumeric() and number_of_songs.isnumeric():
                try:
                    self.music_store.add_album(int(album_id), name, int(number_of_songs), int(author_id))
                    print("Successfully added")
                except Exception as e:

                    print(e)
            else:
                print("Albums ID, authors ID or number of songs is not a number")
            print("\n-----------------------------------------------\n")

    def __add_author(self) -> None:
        continue_while = True
        first = True
        while continue_while:
            if not first:
                answer = input("Do you want to continue (y/n): ")
                if answer != 'y':
                    break
            else:
                first = False

            author_id = input("Enter author's id: ")
            name = input("Enter name of author: ")
            if author_id.isnumeric():
                try:
                    self.music_store.add_author(int(author_id), name)
                    print("Successfully added")
                except Exception as e:

                    print(e)
            else:
                print("ID is not a number")
            print("\n-----------------------------------------------\n")

    def __delete_album(self) -> None:
        continue_while = True
        first = True
        while continue_while:
            if not first:
                answer = input("Do you want to continue (y/n): ")
                if answer != 'y':
                    break
            else:
                first = False

            album_id = input("Enter album's id: ")
            if album_id.isnumeric():
                try:
                    self.music_store.delete_album_by_id(int(album_id))
                    print("Successfully deleted")
                except Exception as e:
                    print(e)
            else:
                print("ID is not a number")
            print("\n-----------------------------------------------\n")

    def __delete_author(self) -> None:
        continue_while = True
        first = True
        while continue_while:
            if not first:
                answer = input("Do you want to continue (y/n): ")
                if answer != 'y':
                    break
            else:
                first = False

            author_id = input("Enter author's id: ")
            if author_id.isnumeric():
                try:
                    self.music_store.delete_author_by_id(int(author_id))
                    print("Successfully deleted")
                except Exception as e:

                    print(e)
            else:
                print("ID is not a number")
            print("\n-----------------------------------------------\n")

    def __get_size_albums(self) -> None:
        print("We have " + str(self.music_store.count_albums()) + " albums")
        print("\n-----------------------------------------------\n")

    def __get_size_authors(self):
        print("We have " + str(self.music_store.count_authors()) + " authors")
        print("\n-----------------------------------------------\n")

    def __show_albums(self):
        print_albums(self.music_store.get_all_albums(), "")

    def __show_authors(self):
        print("The authors are: ")
        print("\n-----------------------------------------------\n")
        for i in self.music_store.get_all_authors():
            print_author(i)
            print_albums(i.albums, "\t")

    def __clear(self):
        self.music_store.clear()

    def __clear_albums(self):
        self.music_store.clear_albums()

    def __rename_album(self):
        continue_while = True
        first = True
        while continue_while:
            if not first:
                answer = input("Do you want to continue (y/n): ")
                if answer != 'y':
                    break
            else:
                first = False

            album_id = input("Enter album's id: ")
            new_name = input("Enter new album`s name: ")
            if album_id.isnumeric():
                try:
                    self.music_store.change_album_name(int(album_id), new_name)
                    print("Successfully renamed")
                except Exception as e:

                    print(e)
            else:
                print("ID is not a number")
            print("\n-----------------------------------------------\n")

    def __rename_author(self):
        continue_while = True
        first = True
        while continue_while:
            if not first:
                answer = input("Do you want to continue (y/n): ")
                if answer != 'y':
                    break
            else:
                first = False

            author_id = input("Enter author's id: ")
            new_name = input("Enter new author`s name: ")
            if author_id.isnumeric():
                try:
                    self.music_store.change_author_name(int(author_id), new_name)
                    print("Successfully renamed")
                except Exception as e:

                    print(e)
            else:
                print("ID is not a number")
            print("\n-----------------------------------------------\n")

    def __change_number_of_songs(self):
        continue_while = True
        first = True
        while continue_while:
            if not first:
                answer = input("Do you want to continue (y/n): ")
                if answer != 'y':
                    break
            else:
                first = False

            album_id = input("Enter album's id: ")
            new_number_of_songs = input("Enter new album`s number of songs: ")
            if album_id.isnumeric() and new_number_of_songs.isnumeric():
                try:
                    self.music_store.change_number_of_songs(int(album_id), int(new_number_of_songs))
                    print("Successfully changed")
                except Exception as e:

                    print(e)
            else:
                print("ID or new number of songs are not a number")
            print("\n-----------------------------------------------\n")

    def __save_to_xml(self):
        number_of_authors, number_of_albums = self.music_store.save_to_xml(self.path_xml)
        print("\nSuccessfully saved", number_of_authors, "author(s) and", number_of_albums, "album(s)")
        print("\n-----------------------------------------------\n")

    def __load_from_xml(self):
        try:
            number_of_authors, number_of_albums = self.music_store.load_from_xml(self.path_xml)
            print("\nSuccessfully loaded", number_of_authors, "author(s) and", number_of_albums, "album(s)")
        except Exception as e:
            print(e)
        print("\n-----------------------------------------------\n")

    def __get_album(self):
        continue_while = True
        first = True
        while continue_while:
            if not first:
                answer = input("Do you want to continue (y/n): ")
                if answer != 'y':
                    break
            else:
                first = False

            album_id = input("Enter album's id: ")
            if album_id.isnumeric():
                try:
                    print_album(self.music_store.get_album_by_id(int(album_id)), "")
                except Exception as e:

                    print(e)
            else:
                print("ID is not a number")
            print("\n-----------------------------------------------\n")

    def __get_author(self):
        continue_while = True
        first = True
        while continue_while:
            if not first:
                answer = input("Do you want to continue (y/n): ")
                if answer != 'y':
                    break
            else:
                first = False

            author_id = input("Enter author's id: ")
            if author_id.isnumeric():
                try:
                    print_author(self.music_store.get_author_by_id(int(author_id)))
                except Exception as e:

                    print(e)
            else:
                print("ID is not a number")
            print("\n-----------------------------------------------\n")

    def __manage_albums(self):
        first = True
        continue_while = True
        while continue_while:
            if not first:
                print("Wrong command, try again")
            first = True

            print("Enter ADD to add new album")
            print("Enter RENAME to rename album")
            print("Enter CHANGE to change number of songs of album")
            print("Enter GET to get album by id")
            print("Enter INFO to get info about albums")
            print("Enter COUNT to get number of albums")
            print("Enter DEL to delete album")
            print("Enter CLEAR to clear albums")
            print("Enter BACK to switch on main menu")
            command = input("Enter your command: ")

            print("\n-----------------------------------------------\n")

            if command == 'a' or command == 'ADD':
                self.__add_album()
            elif command == 'r' or command == "RENAME":
                self.__rename_album()
            elif command == 'c' or command == "CHANGE":
                self.__change_number_of_songs()
            elif command == 'g' or command == 'GET':
                self.__get_album()
            elif command == 'd' or command == 'DEL':
                self.__delete_album()
            elif command == 'ct' or command == 'COUNT':
                self.__get_size_albums()
            elif command == 'i' or command == 'INFO':
                self.__show_albums()
            elif command == 'cl' or command == 'CLEAR':
                self.__clear_albums()
            elif command == 'b' or command == 'BACK':
                continue_while = False
            else:
                first = False

    def __manage_authors(self):
        first = True
        continue_while = True
        while continue_while:
            if not first:
                print("Wrong command, try again")
            first = True

            print("Enter ADD to add new author")
            print("Enter RENAME to rename author")
            print("Enter GET to get album by id")
            print("Enter INFO to get info about authors")
            print("Enter COUNT to get number of authors")
            print("Enter DEL to delete author")
            print("Enter CLEAR to clear authors")
            print("Enter BACK to switch on main menu")
            command = input("Enter your command: ")

            print("\n-----------------------------------------------\n")

            if command == 'a' or command == 'ADD':
                self.__add_author()
            elif command == 'r' or command == 'RENAME':
                self.__rename_author()
            elif command == 'g' or command == 'GET':
                self.__get_author()
            elif command == 'd' or command == 'DEL':
                self.__delete_author()
            elif command == 'ct' or command == 'COUNT':
                self.__get_size_authors()
            elif command == 'i' or command == 'INFO':
                self.__show_authors()
            elif command == 'cl' or command == 'CLEAR':
                self.__clear()
            elif command == 'b' or command == 'BACK':
                continue_while = False
            else:
                first = False

    def menu(self):
        first = True
        continue_while = True
        while continue_while:
            if not first:
                print("Wrong command, try again")
            first = True

            print("Enter ALBUM to work with albums")
            print("Enter AUTHOR to work with author")
            print("Enter LOAD to load data from file")
            print("Enter SAVE to save data to file")
            print("Enter CLEAR to clear music store")
            print("Enter EXIT to close app")

            command = input("Enter your command: ")

            print("\n-----------------------------------------------\n")

            if command == 'al' or command == 'ALBUM':
                self.__manage_albums()
            elif command == 'au' or command == 'AUTHOR':
                self.__manage_authors()
            elif command == 'l' or command == 'LOAD':
                self.__load_from_xml()
            elif command == 's' or command == 'SAVE':
                self.__save_to_xml()
            elif command == 'cl' or command == 'CLEAR':
                self.__clear()
            elif command == 'EXIT' or command == 'e':
                continue_while = False
            else:
                first = False
