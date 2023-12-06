class Phonebook:
    def __init__(self, filename='book.txt'):
        self.filename = filename
        self.phonebook = self.read_phonebook()


    def read_phonebook(self):
        phonebook = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, phone_number = line.strip().split('; ')
                    phonebook[phone_number] = name
        except FileNotFoundError:
            pass
        return phonebook
    def save_phonebook(self):
        with open(self.FILENAME, 'w') as file:
            for phone_number, name in self.phonebook.items():
                file.write(f"{name}; {phone_number}\n")
        print("Phonebook saved.")

    def display_phonebook():
        phonebook = read_phonebook()
        for phone_number, name in phonebook.items():
            print(f"{name}: {phone_number}")

    def validate_number(phone_number):
        return len(phone_number) == 9 and phone_number.isdigit()

    def add_entry(name, phone_number):
        if not validate_number(phone_number):
            print("Invalid phone number.")
            return
        phonebook = read_phonebook()
        if phone_number in phonebook:
            print("Phone number already exists.")
            return
        phonebook[phone_number] = name
        save_phonebook(phonebook)
        print("Phone number added.")

    def remove_entry(phone_number):
        phonebook = read_phonebook()
        if phone_number in self.phonebook:
            del self.phonebook[phone_number]
            save_phonebook(phonebook)
            print("Phone number removed.")
        else:
            print("Phone number not found.")

    def modify_entry(self,old_phone_number, new_name, new_phone_number):
        self.phonebook = read_phonebook()
        if old_phone_number not in self.phonebook:
            print("Old phone number not found.")
            return False
        if not self.validate_number(new_phone_number):
            print("Invalid new phone number.")
            return False
        del self.phonebook[old_phone_number]
        self.phonebook[new_phone_number] = new_name
        self.save_phonebook()
        print("Phonebook entry modified.")
        return True    

book1 = Phonebook()
print(book1.read_phonebook())
book1.add_entry("Krzysztof","938912842")
book1.add_entry("Zbyszek", "346812832")
book1.display_phonebook()