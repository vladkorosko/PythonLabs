import MySQLdb


class MusicStoreDataBaseManager:
    def __init__(self):
        url = 'localhost'
        database = "MUSIC_STORE"
        self.db = MySQLdb.connect(url, "root", "11235813vlad", database)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def show_all_authors(self):
        query = "SELECT ID_AUTHOR, NAME FROM AUTHORS"
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            print("The authors are: ")
            for row in results:
                print("Author id:", row[0], "| Author name:", row[1])
        except Exception as e:
            print("Error while getting list of authors:", e)

    def show_all_albums(self):
        query = "SELECT ID_ALBUM, NAME, NUMBER_OF_SONGS, ID_AUTHOR FROM ALBUMS"
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            print("The albums are: ")
            for row in results:
                print("Album id:", row[0], "| Album name:", row[1],
                      "| Number of songs:", row[2], "| Author id:", row[3])
        except Exception as e:
            print("Error while getting list of albums:", e)

    def add_new_author(self, author_id: int, name: str):
        values = str(author_id) + ", '" + name + "'"

        query = "INSERT INTO AUTHORS (ID_AUTHOR, NAME) VALUES(" + values + ")"

        try:
            self.cursor.execute(query)
            self.db.commit()
            print("Author", name, "successfully added.")
            return True
        except Exception as e:
            print("Error while adding new author:", e)
            self.db.rollback()
            return False

    def add_new_album(self, album_id: int, name: str, number_of_songs: int, author_id: int):
        values = str(album_id) + ", " + str(author_id) + ", '" + name + "', " + str(number_of_songs)
        query = "INSERT INTO ALBUMS (ID_ALBUM, ID_AUTHOR, NAME, NUMBER_OF_SONGS) VALUES (" + values + ")"

        try:
            self.cursor.execute(query)
            self.db.commit()
            print("Album", name, "successfully added.")
            return True
        except Exception as e:
            print("Error while adding new album:", e)
            self.db.rollback()
            return False

    def change_author(self, author_id: int, name: str):
        query = "UPDATE AUTHORS SET NAME = '" + name + "' WHERE ID_AUTHOR = " + str(author_id)
        try:
            self.cursor.execute(query)
            self.db.commit()
            print("Author", name, "successfully updated.")
            return True
        except Exception as e:
            print("Error while updating author:", e)
            self.db.rollback()
            return False

    def change_album(self, album_id: int, name: str, number_of_songs: int, author_id: int):
        query = "UPDATE ALBUMS SET NAME = '" + name + "', NUMBER_OF_SONGS = " + str(number_of_songs) + \
                ", ID_AUTHOR = " + str(author_id) + " WHERE ID_ALBUM = " + str(album_id)
        try:
            self.cursor.execute(query)
            self.db.commit()
            print("Album", name, "successfully updated.")
            return True
        except Exception as e:
            print("Error while updating album:", e)
            self.db.rollback()
            return False

    def delete_author_by_id(self, author_id: int):
        query = "DELETE FROM AUTHORS WHERE ID_AUTHOR = " + str(author_id)

        try:
            self.cursor.execute(query)
            self.db.commit()
            print("Author with id", author_id, "successfully deleted")
            return True
        except Exception as e:
            print("Error while deleting author:", e)
            self.db.rollback()
            return False

    def delete_album_by_id(self, album_id: int):
        query = "DELETE FROM Albums WHERE ID_Album = " + str(album_id)

        try:
            self.cursor.execute(query)
            self.db.commit()
            print("Album with id", album_id, "successfully deleted")
            return True
        except Exception as e:
            print("Error while deleting album:", e)
            self.db.rollback()
            return False

    def find_author_by_condition(self, field_name, field_value, field_output):
        adding = False
        if field_name == "id":
            finding_by = "ID_AUTHOR"
        elif field_name == "name":
            finding_by = "NAME"
            adding = True
        else:
            raise Exception("Wrong name of field")

        if field_output == "*":
            select_field = "*"
        elif field_output == "id":
            select_field = "ID_AUTHOR"
        elif field_output == "name":
            select_field = "NAME"
        else:
            raise Exception("Wrong name of field")

        if adding:
            query = "SELECT " + select_field + " FROM AUTHORS WHERE " + \
                    finding_by + " = " + "'" + field_value + "'"
        else:
            query = "SELECT " + select_field + " FROM AUTHORS WHERE " + \
                    finding_by + " = " + str(field_value)

        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            print("The authors are: ")
            if field_output == "name":
                for row in results:
                    print("Author name:", row[0])
            elif field_output == "id":
                for row in results:
                    print("Author id:", row[0])
            else:
                for row in results:
                    print("Author id:", row[0], "| Author name:", row[1])
        except Exception as e:
            print("Error while getting list of authors:", e)

    def find_album_by_condition(self, field_name, field_value, field_output):
        adding = False
        if field_name == "album_id":
            finding_by = "ID_ALBUM"
        elif field_name == "name":
            finding_by = "NAME"
            adding = True
        elif field_name == "number_of_songs":
            finding_by = "NUMBER_OF_SONGS"
        elif field_name == "author_id":
            finding_by = "ID_AUTHOR"
        else:
            raise Exception("Wrong name of field")

        if field_output == "album_id":
            select_field = "ID_ALBUM"
        elif field_output == "name":
            select_field = "NAME"
        elif field_output == "number_of_songs":
            select_field = "NUMBER_OF_SONGS"
        elif field_output == "author_id":
            select_field = "ID_AUTHOR"
        elif field_output == "*":
            select_field = "*"
        else:
            raise Exception("Wrong name of field")

        if adding:
            query = "SELECT " + select_field + " FROM ALBUMS WHERE " + \
                    finding_by + " = " + "'" + field_value + "'"
        else:
            query = "SELECT " + select_field + " FROM ALBUMS WHERE " + \
                    finding_by + " = " + str(field_value)

        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            print("The albums are: ")
            if field_output == "album_id":
                for row in results:
                    print("Album id:", row[0])
            elif field_output == "name":
                for row in results:
                    print("Album name:", row[0])
            elif field_output == "number_of_songs":
                for row in results:
                    print("Number of songs:", row[0])
            elif field_output == "author_id":
                for row in results:
                    print("Author id:", row[0])
            else:
                for row in results:
                    print("Album id:", row[0], "| Album name:", row[1],
                          "| Number of songs:", row[2], "| Author id:", row[3])
        except Exception as e:
            print("Error while getting list of albums:", e)
