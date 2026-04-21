'''
Subject Section Number : 103
full name : مصطفى محمود عبد الرحمن حسونة
ID : 120258131
'''
#  Address Book System                  # 2026/02/05
contacts = []

while (True):
    print("menu:\n1 - Add New Contact\n2 - Search by Name\n3 - Search by number.\n4 - Delete contact by name.\n5 - Delete contact by number.\n6 - Show all contacts.\n7 - Exit")  
    try:
        choice = int(input("Please to enter your choice : "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if(choice == 7):
        print("the programe ended    :)")
        break
    elif choice not in range(1, 8):
        print("Invalid choice the choice must be between this range [1,7]")
    elif (choice == 1):                            # 2026/02/07
        name = input("enter the name : ")
        number = input("enter the number : ")
        number_exists = False
        for contact in contacts:
            if contact["number"] == number:
                number_exists = True
                break
        if number_exists:
            print("Error: This number already exists Process rejected.")
        else:
            print("'Note' allowed types: [family, personal, work, other]")
            input_type = input("Enter Type: ")
            if input_type in ['family','personal','work','other']:
                final_type = input_type
            else:
                final_type = "other"
                print("Warning: Type set to 'other' because input was not in the list.")
            new_contact = {"name" : name, "number" : number, "type" : final_type}
            contacts.append(new_contact)
            print("Contact added successfully    :)")
    elif not contacts:
        print("Address book is empty.")
    else :
        if choice == 2:                                         # 2026/02/09
            search_by_name = input("enter name to search : ")
            result_of_search = False

            for contact in contacts:
                if search_by_name in contact["name"]:
                    print("name : ",contact["name"]," | type : " , contact["type" ], " | number : " , contact["number"])
                    result_of_search = True

            if not result_of_search:
                print("No contact found with this name.")

        elif choice == 3:
            search_by_number = input("enter number to search : ")
            found_num = False
            for contact in contacts:
                if search_by_number == contact["number"]:
                    print("name : " , contact["name"] , " | number : " , contact["number"] , " | type : " , contact["type"] , )
                    found_num = True
            if not(found_num) : 
                print("No contact found with this number.")

        elif (choice == 4):
            name_to_delete = input("enter the name you want to delete : ")
            found = False
            new_contacts = []
            for contact in contacts:
                if contact["name"] == name_to_delete :
                    found = True
                else:
                    new_contacts.append(contact)
            if found: 
                deleted_count = len(contacts) - len(new_contacts) 
                contacts = new_contacts
                print(deleted_count, "contact/s deleted successfully.")
            else:
                print("No contact found with this name.")

        elif (choice == 5):
            number_to_delete = input("enter the number you want to delete : ")
            found = False
            new_contacts = []
            for contact in contacts :
                if number_to_delete == contact["number"]:
                    found = True
                    print("Contact deleted successfully.")
                else:
                    new_contacts.append(contact)
            if found :
                contacts = new_contacts
            else:
                print("no contact found with this number.")

        elif (choice == 6):
            print("------------------ All Contacts ------------------")
            print()
            if not contacts:
                print("Address book is empty.")
            else:
                for contact in contacts:
                    print("Name :" , contact['name'] , "| Number :" , contact['number'] , "| Type :" , contact['type'])
                    print("")
                 

                 # DONE 05:21 PM
                 # 2026/02/11 I am very happy to have accomplished this  2026/02/11
