"""
    0176CS221015
    Aditya Kumar Srivastav
    LNCTE
    BATCH - 9
"""
username = []
password = {}
print("""WELCOME,
1. LOGIN
2. REGISTER
3. CHANGE PASSWORD
4. EXIT
""")
c = input("CHOOSE AN OPTION : ")
if c == "1":
    print("WELCOME TO THE LOGIN PAGE")
    user = input("ENTER YOUR USERNAME: ")
    if user in username:
        print(f"WELCOME {user}")
        pwd = input("ENTER YOUR PASSWORD: ")
        if username[user] == pwd:
            print("YOU HAVE LOGGED IN SUCCESSFULLY")
        else:
            print("YOU HAVE ENTERED WRONG PASSWORD")
    else:
        print("ENTER A VALID USERNAME")
elif c == "2":
    print("WELCOME TO THE REGISTRATION PAGE")
    user = input("CREATE NEW USERNAME : ")
    if user in username:
        print("THIS USERNAME ALREADY EXISTS")
    else:
        username.append(user)
        print("USERNAME CREATED")
        pwd = input("ENTER A PASSWORD: ")
        password[user] = pwd
        print("PASSWORD CREATED")
elif c == 3:
    user = ("ENTER YOUR USERNAME: ")
    if user in username:
        pwd = input("ENTER YOUR PASSWORD : ")
        if password[user] == pwd:
            n_pwd = input("ENTER NEW PASSWORD : ")
            if n_pwd != pwd:
                password[user] = n_pwd
                print("PASSWORD CHANGED")
            else:
                print("THIS PASSWORD IS SAME AS THE CURRENT PASSWORD")
        else:
            print("YOU HAVE ENTERED WRONG PASSWORD")
    else:
        print("ENTER A VALID USERNAME")
elif c == "4":
    exit()
else:
    print("ENTER A VALID CHOICE")
