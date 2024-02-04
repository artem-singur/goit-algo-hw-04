def parse_input(user_input):

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args

def add_contact(args, contacts):

    name, phone = args
    contacts[name] = phone

    return "Contact added."

def change_contact(args, contacts):

    name, phone = args

    if contacts.get(name) is None:
        return "No such contact exists."
    else:
        contacts[name] = phone
        return "Contact changed."

def get_contact(args, contacts):

    name = args[0]
    phone = contacts.get(name)
    if phone is None:
        return "No such contact exists."
    else:
        return phone

def all_contacts(contacts):

    if len(contacts) > 0:
        contacts_str = ""
        for name, phone in contacts.items():
            contacts_str = ("" if len(contacts_str) == 0 else contacts_str + "\n") + name + ": " + phone
        return contacts_str
    else:
        return "The list of contacts is empty."

def main():

    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
