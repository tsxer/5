def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except KeyError as e :
            return f"Error: {e}. Try again."
        except IndexError as e :
            return f"Error: {e}. Try again."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        i = 1
        new_name = f"{name} ({i})"
        while new_name in contacts:
            i += 1
            new_name = f"{name} ({i})"
        contacts[new_name] = phone
        return f"Contact with a similar name exists. Added as '{new_name}'."
    else:
        contacts[name] = phone
        return "Contact added."

@input_error
def update_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts [name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def print_contact (args, contacts):
    name, *_ = args
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."
    
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
        elif command == "all":
            print(contacts)
        elif command == "change":
            print(update_contact(args, contacts))
        elif command == "phone":
            print(print_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

