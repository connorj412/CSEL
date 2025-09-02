def main():
    print("[Mailing List]")
    emails = []
    choice = 0
    while choice != 4:
        choice = int(input("1 - Add email\n"
                           "2 - Delete email\n"
                           "3 - List all emails\n"
                           "4 - Quit\n"
                           "Make your selection: "))
        match choice:
            case 1:
                new_email = input("Enter the email to be added: ")
                emails.append(new_email)
                print("Email added to mailing list.")
            case 2:
                delete_email = input("Enter the email to be removed: ")
                if delete_email in emails:
                    emails.remove(delete_email)
                    print(f"{delete_email} has been removed from the mailing list.")
                else:
                    print(f"No such email in mailing list: {delete_email}")
            case 3:
                for x in emails:
                    print(x)
    print("Shutting down...")
if __name__ == "__main__":
    main()