def main():
    choice = "0"
    d = {}
    while choice != "E":
        choice = input("Choose an option:\n"
                       "1 - Login\n"
                       "2 - Register\n"
                       "E - Exit\n")
        print()
        match choice:
            case "2":
                print("[Register]")
                username = input("Username: ")
                password = input("Password: ")
                print("User successfully added!")
                d[username] = password
            case "1":
                print("[Login]")
                username = input("Username: ")
                password = input("Password: ")
                if (username not in d) or d[username] != password:
                    print("Incorrect username/password!")
                else:
                    print("Success!")
                    while choice != "E" and choice != "4":
                        choice = input("Choose an option\n"
                                       "3 - Change Password\n"
                                       "4 - Logout\n"
                                       "E - Exit\n")
                        match choice:
                            case "3":
                                print("[Change Password]")
                                password2 = input("Password: ")
                                d[username] = password2



if __name__ == "__main__":
    main()