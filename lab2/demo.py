from lab2.classes.MusicStoreDatabaseManager import MusicStoreDataBaseManager


def demo():
    m = MusicStoreDataBaseManager()
    print("Authors in database:")
    print()
    m.show_all_authors()
    print("\n----------------------------------------------------------\n")

    print("Albums in database:")
    print()
    m.show_all_albums()
    print("\n----------------------------------------------------------\n")

    print("Added new author 123456 'Sabatan'")
    m.add_new_author(123456, 'Sabatan')
    print()

    print("Added new album 121323 'Heros' with 10 songs to author 123456 'Sabatan'")
    m.add_new_album(121323, 'Heros', 10, 123456)
    print()

    print()
    m.show_all_authors()
    print("\n----------------------------------------------------------\n")
    m.show_all_authors()
    print("\n----------------------------------------------------------\n")

    print("Change name of author: 123456 'Sabatan' to 'Sabaton'")
    m.change_author(123456, "Sabaton")
    print("Change name of album: 121323 'Heros' to 'Heroes'")
    print("Change number of songs of album: 121323 'Heroes' from 10 to 15")
    m.change_album(121323, 'Heroes', 15, 123456)

    print()
    m.show_all_authors()
    print("\n----------------------------------------------------------\n")
    m.show_all_albums()
    print("\n----------------------------------------------------------\n")

    print("Add test album (999999 'Test deleting' 15) to author 123456 'Sabaton'\n")
    m.add_new_album(999999, 'Test deleting', 14, 123456)
    m.find_album_by_condition("author_id", 123456, "*")

    print("\nFind all albums with number of songs is 15 and show only their names")
    m.find_album_by_condition("number_of_songs", 15, "name")
    print("\nFind authors with name 'Sabaton'")
    m.find_author_by_condition("name", "Sabaton", "*")
    print("\nFind all albums with author_id 102010 and show only album_id")
    m.find_album_by_condition("author_id", 102010, "album_id")
    print("\n----------------------------------------------------------\n")

    print('\nDelete album with id 999999\n')
    m.delete_album_by_id(999999)
    m.find_album_by_condition("author_id", 123456, "*")
    print("\n----------------------------------------------------------\n")

    print('\nDelete album with id 121323\n')
    m.delete_album_by_id(121323)
    m.show_all_albums()
    print("\n----------------------------------------------------------\n")

    m.show_all_authors()
    print("\nDelete author with id 123456\n")
    print()

    m.delete_author_by_id(123456)
    m.show_all_authors()
    print("\n----------------------------------------------------------\n")
