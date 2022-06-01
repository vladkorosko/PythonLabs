class Contact:
    def __init__(self, Id, name, surname):
        self.Id = Id
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return str(self.Id) + " " + self.name + " " + self.surname


class Telephone(Contact):
    def __init__(self, Id, name, surname, number):
        super().__init__(Id, name, surname)
        self.number = number

    def __str__(self) -> str:
        return str(self.Id) + " " + self.name + " " + self.surname + " " + self.number


class Email(Contact):
    def __init__(self, Id, name, surname, mail):
        super().__init__(Id, name, surname)
        self.mail = mail

    def __str__(self) -> str:
        return str(self.Id) + " " + self.name + " " + self.surname + " " + self.mail


class UnionContacts(Contact):
    def __init__(self, Id, name, surname, contacts_data):
        super().__init__(Id, name, surname)
        self.contacts_data = contacts_data

    def __str__(self) -> str:
        return str(self.Id) + " " + self.name + " " + self.surname + " " + self.contacts_data


def merge(phone, email):
    if phone.name == email.name and phone.surname == email.surname:
        return UnionContacts(phone.Id, phone.name, phone.surname, [phone.number, email.mail])


class ContactList:
    def __init__(self, contacts):
        self.contacts = contacts

    def sort_by_name(self):
        self.contacts.sort(key=lambda x: x.name)

    def sort_by_surname(self):
        self.contacts.sort(key=lambda x: x.surname)

    def get_contacts(self):
        return self.contacts

    def __str__(self) -> str:
        line = ""
        for i in self.contacts:
            line += str(i)
            line += "\n"
        return line


def print_result(result):
    print('[')
    for e in result:
        print('\t' + e.__str__())
    print(']')


if __name__ == '__main__':
    contacts_list = [Email(120203, "Vlad", "Korosko", "vlad.korosko1@gamil.com"),
                     Telephone(891232, "Petro", "Cossack", "+380123456789"),
                     Email(120203, "Amogus", "Impostor", "among.us@gamil.com"),
                     Telephone(891232, "Pedro", "De-France", "+310123246789"),
                     Telephone(891232, "Python", "3", "+380127893456"),
                     Telephone(891232, "C", "++", "+380128934567"),
                     Email(120203, "Java", "Skript", "java.skript@gamil.com"),
                     Email(120203, "Petro", "Cossack", "petro.cossack@gamil.com")]
    l = ContactList(contacts_list)
    print_result(l.contacts)
    l.sort_by_name()
    print_result(l.contacts)
    l.sort_by_surname()
    print_result(l.contacts)
