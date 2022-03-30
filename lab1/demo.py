from lab1.myclasses.Manager import Manager
from lab1.myclasses.MusicStore import MusicStore


def demo():
    store = MusicStore()
    manager = Manager(store, "lab1/resources/sample.xml")
    manager.menu()
