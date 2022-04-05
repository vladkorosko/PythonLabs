from lab1.demo import demo
from lab2.classes.MusicStoreDatabaseManager import MusicStoreDataBaseManager


if __name__ == '__main__':
    m = MusicStoreDataBaseManager()
    m.find_album_by_condition('author_id', 105010, "name")
    #demo()
