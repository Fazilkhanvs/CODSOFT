contact = {"fazil":12345}

def display_contact():
     
     print("Name\t\tphone")
     for key in contact:
          print("{}\t\t{}".format(key,contact.get(key)))
     


while True:
    choice = int(input('''                   
    1. Add new contact
    2. Searcg contact
    3. Display contact
    4. Edit contact
    5. Delete contact
    6. Exit
    Enter your choice:'''))
    
    if choice == 1:
        name = input("Enter the name:")
        phone = input("Enter the phone number")
        contact[name] = phone

    elif choice == 2:
        search_name = input("Enter the name:")
        if search_name in  contact:
            print( search_name,"phone number is",contact[search_name])

        else:
            print("the name you have entered is not found")

    elif choice == 3:
            display_contact()
    elif choice == 4:
            edit_contact = input("Enter the name that you want updete the details:")
            if edit_contact in contact:
                 new_number = input("Enter the new mobile number:")

                 contact[edit_contact] = new_number
                 print("contact updated")
                 display_contact()
            else:
                 print("The name you have entered is not found")

    elif choice == 5:
            del_contact= input("enter the name to be deleted:")

            if del_contact in contact:
                 confirm = input("Are you sure that you want to delete this conntact(y/s):")

                 if confirm == "y" or confirm == "Y":
                      
                    contact.pop(del_contact)
                    display_contact()
                 else:
                    print("The name you have entered is not found")

                      

    
    else:
        break

    