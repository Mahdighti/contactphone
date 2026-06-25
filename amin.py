from modole import Phone
import csv
PATH = 'C:/Users/Mahur/Desktop/contact/contact.csv'
Phones = []
while True:
    def Add_contact():
        try:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            save = Phone(name, phone, email)
            Phones.append(save) 
        except Exception as a:
            print(f"Erorr {a} ")
    def Search():
        Name = input("enter name for search")
        for item in Phones:
            if Name == item.name:
                print(item.search())
    print("1.Add contact\n2.search contact\n3.Delete contact\n4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        Add_contact()
    elif ch == 2:
        Search()
    elif ch == 3:
        strn = input("Enter name: ")
        for x in Phones:
            if x == strn:
                Phones.remove(x) 
    elif ch == 4:
        with open(PATH, "a", newline='', encoding='utf8') as my_doct:
            cs = csv.writer(my_doct)
            cs.writerow(['name','phone','email'])
            for object in Phones:
                cs.writerows([[
                    object.name,
                    object.phone,
                    object.email
                ]])
        break