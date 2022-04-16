from lab2.classes.MusicStoreDatabaseManager import MusicStoreDataBaseManager
from lab2.classes.MusicStoreDatabaseManager import print_authors
from lab2.classes.MusicStoreDatabaseManager import print_albums


def demo():
    try:
        m = MusicStoreDataBaseManager()
        print("Authors in database:")
        print()
        authors, field = m.show_all_authors()
        print_authors(authors, field)
        print("\n----------------------------------------------------------\n")

        print("Albums in database:")
        print()
        albums, field = m.show_all_albums()
        print_albums(albums, field)
        print("\n----------------------------------------------------------\n")

        print("Added new author 123456 'Sabatan'")
        m.add_new_author(123456, 'Sabatan')
        print()

        print("Added new album 121323 'Heros' with 10 songs to author 123456 'Sabatan'")
        m.add_new_album(121323, 'Heros', 10, 123456)
        print()

        print()
        authors, field = m.show_all_authors()
        print_authors(authors, field)
        print("\n----------------------------------------------------------\n")
        albums, field = m.show_all_albums()
        print_albums(albums, field)
        print("\n----------------------------------------------------------\n")

        print("Change name of author: 123456 'Sabatan' to 'Sabaton'")
        m.change_author(123456, "Sabaton")
        print("Change name of album: 121323 'Heros' to 'Heroes'")
        print("Change number of songs of album: 121323 'Heroes' from 10 to 15")
        m.change_album(121323, 'Heroes', 15, 123456)

        print()
        authors, field = m.show_all_authors()
        print_authors(authors, field)
        print("\n----------------------------------------------------------\n")
        albums, field = m.show_all_albums()
        print_albums(albums, field)
        print("\n----------------------------------------------------------\n")

        print("Add test album (999999 'Test deleting' 15) to author 123456 'Sabaton'\n")
        m.add_new_album(999999, 'Test deleting', 14, 123456)
        albums, field = m.find_album_by_condition("author_id", 123456, "*")
        print_albums(albums, field)

        print("\nFind all albums with number of songs is 15 and show only their names")
        albums, field = m.find_album_by_condition("number_of_songs", 15, "name")
        print_albums(albums, field)
        print("\nFind authors with name 'Sabaton'")
        authors, field = m.find_author_by_condition("name", "Sabaton", "*")
        print_authors(authors, field)
        print("\nFind all albums with author_id 102010 and show only album_id")
        albums, field = m.find_album_by_condition("author_id", 102010, "album_id")
        print_albums(albums, field)
        print("\n----------------------------------------------------------\n")

        print('\nDelete album with id 999999\n')
        m.delete_album_by_id(999999)
        albums, field = m.find_album_by_condition("author_id", 123456, "*")
        print_albums(albums, field)
        print("\n----------------------------------------------------------\n")

        print('\nDelete album with id 121323\n')
        m.delete_album_by_id(121323)
        albums, field = m.show_all_albums()
        print_albums(albums, field)
        print("\n----------------------------------------------------------\n")

        authors, field = m.show_all_authors()
        print_authors(authors, field)
        print("\nDelete author with id 123456\n")
        print()

        m.delete_author_by_id(123456)
        authors, field = m.show_all_authors()
        print_authors(authors, field)

        print("\n----------------------------------------------------------\n")
    except Exception as e:
        print(e)
