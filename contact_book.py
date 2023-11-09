
while True:
    print("\nType in the Numbers (1 or 2 or 3) for the Task you want to Perform: ")
    choice = input("1. Add \n2. Search \n3. Exit :__")
    if choice == "1":
        with open("contact.txt", "a") as c:
            name = input("Name: ")
            phone_no = input("Phone Number: ")
            user_email = input("Enter email: ")
            user_address = input("Enter Address: ")

            c.writelines(("\n", name, ":", phone_no, "\n", user_email,":\n", user_address))

    elif choice == "2":
        with open("contact.txt", "r") as c:
            search = input("Search item: ")
            for i in c:
                if search in i:
                    print(i,name,phone_no,user_email,user_address)

    else:
        print("\n Thank you for using the app")
        break


