from lab1.myclasses.Manager import Manager
from lab1.myclasses.MusicStore import MusicStore

from entity.Author import print_authors
from entity.Author import print_author
from entity.Album import print_albums
from entity.Album import print_album


def interactive():
    store = MusicStore()
    manager = Manager(store, "lab1/resources/sample.xml")
    manager.menu()

def demo():
    store = MusicStore()
    path_xml = "lab1/resources/sample.xml"


    print("Start of program:")
    print()
    print_authors(store.get_all_authors())
    print("\n----------------------------------------------------------\n")


    print("Added new author 123456 'Sabatan'")
    store.add_author(123456, 'Sabatan')

    print("Added new album 121323 'Heros' with 10 songs to author 123456 'Sabatan'")
    store.add_album(121323, 'Heros', 10, 123456)

    print()
    print_authors(store.get_all_authors())
    print("\n----------------------------------------------------------\n")


    print("Change name of author: 123456 'Sabatan' to 'Sabaton'")
    store.change_author_name(123456, "Sabaton")

    print("Change name of album: 121323 'Heros' to 'Heroes'")
    store.change_album_name(121323, "Heroes")

    print("Change number of songs of album: 121323 'Heroes' from 10 to 11")
    store.change_number_of_songs(121323, 11)

    print()
    print_authors(store.get_all_authors())
    print("\n----------------------------------------------------------\n")


    print("Load authors and albums from xml file: 'sample.xml'\n")
    number_of_authors, number_of_albums = store.load_from_xml(path_xml)
    print("\nSuccessfully loaded", number_of_authors, "author(s) and", number_of_albums, "album(s)")

    print()
    print_authors(store.get_all_authors())
    print("\n----------------------------------------------------------\n")


    print("Number of authors is:", store.count_authors())
    print("Number of albums is:", store.count_albums())
    print()
    print_albums(store.get_all_albums(), '')

    print("Author with id: 101010\n")
    print_author(store.get_author_by_id(101010))
    print("\nAuthor with index: 2\n")
    print_author(store.get_author_by_index(2))

    print("\nAlbum with id: 101010\n")
    print_album(store.get_album_by_id(101010), '')
    print("\nAlbum with index: 4\n")
    print_album(store.get_album_by_index(2), '')
    print("\n----------------------------------------------------------\n")


    print("Save changes to 'sample.xml'")
    number_of_authors, number_of_albums = store.save_to_xml(path_xml)
    print("\nSuccessfully saved", number_of_authors, "author(s) and", number_of_albums, "album(s)")
    print("\n----------------------------------------------------------\n")


    print("Add test album (999999 'Test deleting' 14) to author 123456 'Sabaton'\n")
    store.add_album(999999, 'Test deleting', 14, 123456)
    print_author(store.get_author_by_id(123456))

    print('\nDelete album with id 999999\n')
    store.delete_album_by_id(999999)
    print_author(store.get_author_by_id(123456))
    print("\n----------------------------------------------------------\n")


    print_authors(store.get_all_authors())
    print("\nDelete author with id 123456\n")

    print()
    store.delete_author_by_id(123456)
    print_authors(store.get_all_authors())
    print("\n----------------------------------------------------------\n")

    print("Save changes to 'sample.xml'")
    number_of_authors, number_of_albums = store.save_to_xml(path_xml)
    print("\nSuccessfully saved", number_of_authors, "author(s) and", number_of_albums, "album(s)")
    print("\n----------------------------------------------------------\n")
