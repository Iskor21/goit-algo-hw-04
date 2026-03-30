def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts, filename="contacts.txt"):
    name, phone = args
    contacts[name] = phone
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{name},{phone}\n")
    return ["Contact added."]

def change_contact(args, contacts, filename="contacts.txt"):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        with open(filename, "w", encoding="utf-8") as f:
            for n, p in contacts.items():
                f.write(f"{n},{p}\n")
        return ["Contact changed."]
    else:
        return ["Contact does not exist."]

def load_contacts(filename="contacts.txt"):
    contacts = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts

def phone_contact(args, contacts):
    if not args:
        return [f"{n}: {p}" for n, p in contacts.items()]
    else:
        name = args[0]
        if name in contacts:
            return [f"{name}: {contacts[name]}"]
        else:
            return [f"Contact {name} does not exist."]

def all_contacts(contacts):
    return [f"{n}: {p}" for n, p in contacts.items()]

def main():
    contacts = load_contacts()
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
            for r in add_contact(args, contacts):
                print(r)
        elif command == "change":
            for r in change_contact(args, contacts):
                print(r)
        elif command == "phone":
            for r in phone_contact(args, contacts):
                print(r)
        elif command == "all":
            for r in all_contacts(contacts):
                print(r)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()