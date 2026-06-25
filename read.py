import csv
PATH = 'C:/Users/Mahur/Desktop/contact/contact.csv'
with open(PATH, "r") as My_dict:
    cs = csv.reader(My_dict)
    this_item = list(cs) 
name = input("Enter name: ")
for i in this_item:
    if i[0] == name:
        print(i) 