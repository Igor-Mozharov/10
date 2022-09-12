from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, new_name):
        self.name = Name(new_name)
        self.phones = []

    def __repr__(self):
        return f'{self.phones}'

    def add_phone(self, new_phone):
        self.phones.append(Phone(new_phone))

    def change_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            self.phones.append(Phone(new_phone))
            self.phones.remove(old_phone)
        else:
            print('Cant find this phone number')

    def remove_phone(self, old_phone):
        if old_phone in self.phones:
            self.phones.remove(old_phone)
        else:
            print('cant find this phone number')


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name

    # def __repr__(self):
    #     return self.value


class Phone(Field):
    def __init__(self, phone):
        self.value = phone

    def __repr__(self):
        return self.value


addressbook = AddressBook()


def input_error(funk):
    def inner(text_input=None):
        try:
            if len(text_input.split()) > 3:
                print('to many parameters')
                return
            if len(text_input.split()) == 3:
                text_input.split()[1] == str(text_input.split()[1])
                text_input.split()[2] == int(text_input.split()[2])
            return funk(text_input)
        except (AttributeError, IndexError, ValueError, KeyError):
            print('Enter name or phone correctly')
    return inner


def hello(_=None):
    print('How can I help you?')


def show_all(_=None):
    print(addressbook.data)


@ input_error
def add(text_input: str):
    if text_input.split()[1] not in addressbook.data:
        adding = Record(text_input.split()[1])
        adding.add_phone(text_input.split()[2])
        addressbook.add_record(adding)
        print('Its done')
    else:
        print('This contact is exist')


@ input_error
def change(text_input: str):
    if text_input.split()[1] in addressbook.data:
        addressbook.data[text_input.split()[1]] = text_input.split()[2]
        print('it was changed')
    else:
        print('no contact')


@ input_error
def delete(text_input: str):
    if text_input.split()[1] in addressbook.data:
        addressbook.data.pop(text_input.split()[1])
        print('Done')


@ input_error
def phone(text_input: str):
    if text_input.split()[1] in addressbook.data:
        print(addressbook.data[text_input.split()[1]])
    else:
        print('This contact doesnt exist')


USER_INPUT = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'delete': delete
}


def main():
    while True:
        user_input = input('Enter something  ')
        user_input = user_input.lower()
        if user_input == '.':
            break
        if user_input == 'good bye' or user_input == 'close' or user_input == 'exit':
            print('Good bye!')
            break
        if user_input in USER_INPUT:
            USER_INPUT[user_input]()
        elif user_input.split()[0] in USER_INPUT:
            USER_INPUT[user_input.split()[0]](user_input)


main()
# user = Record('Igor')
# user2 = Record('Dima')
# user.add_phone('0500000000')
# user.add_phone('5555555555')
# user2.add_phone('777777777')
# user2.add_phone('55555555')

# adres = AddressBook()
# adres.add_record(user)
# adres.add_record(user2)
# adres.data['Dima'] = '0655555555'
