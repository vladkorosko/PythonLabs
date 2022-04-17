from lab3.classes.client import client_request


def demo():
    print("Authors in database:")
    print()
    print(client_request("get_all_authors"))
    print("\n----------------------------------------------------------\n")

    print("Albums in database:")
    print()
    print(client_request("get_all_albums"))
    print("\n----------------------------------------------------------\n")

    print("Added new author 123456 'Sabatan'")
    print()
    print(client_request("add_new_author#123456#Sabatan"))
    print()

    print("Added new album 121323 'Heroes' with 10 songs to author 123456 'Sabatan'")
    print()
    print(client_request("add_new_album#121323#Heroes#10#123456"))
    print()

    print()
    print(client_request("get_all_authors"))
    print("\n----------------------------------------------------------\n")
    print(client_request("get_all_albums"))
    print("\n----------------------------------------------------------\n")

    print("Change name of author: 123456 'Sabatan' to 'Sabaton'")
    print()
    print(client_request("change_author_by_id#123456#Sabaton"))

    print()
    print(client_request("get_all_authors"))
    print("\n----------------------------------------------------------\n")

    print("Add test album (999999 'Test deleting' 15) to author 123456 'Sabaton'\n")
    print(client_request("add_new_album#999999#Test deleting#15#123456"))
    print()
    print(client_request("get_all_albums_of_author_by_id#123456"))

    print("\nCount number of albums of author with author_id 102010")
    print()
    print(client_request("count_albums_author_by_id#102010"))
    print("\n----------------------------------------------------------\n")

    print('\nDelete album with id 999999\n')
    print(client_request("delete_album_by_id#999999"))
    print()
    print(client_request("get_all_albums"))
    print("\n----------------------------------------------------------\n")

    print('\nDelete album with id 121323\n')
    print(client_request("delete_album_by_id#121323"))
    print()
    print(client_request("get_all_albums"))
    print("\n----------------------------------------------------------\n")

    print(client_request("get_all_authors"))
    print("\nDelete author with id 123456\n")
    print(client_request("delete_author_by_id#123456"))
    print()
    print(client_request("get_all_authors"))
    print("\n----------------------------------------------------------\n")
