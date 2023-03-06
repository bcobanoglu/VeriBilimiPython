import csv
import os
import shutil

def init_records(file):
    with open(file, mode="w", newline="", encoding="utf-8") as f_w:
        w_n = csv.DictWriter(f_w, fieldnames=["ad", "tel"]) #key
        w_n.writeheader() #başlığı/key'ler yazar
        w_n.writerow({"ad":"Ali", "tel":4567})
        w_n.writerow({"ad":"Veli", "tel":7894})
        w_n.writerow({"ad":"Ayşe", "tel":9654})

def list_records(file):
    print("Telephone Numbers:")
    with open(file, mode="r") as f_r:
        r_n = csv.DictReader(f_r)
        for i in r_n:
            print(i["ad"],":", i["tel"])
        print()

def add_records(file):
    print("Add Name and Phone Number")
    with open(file, mode="a", newline="", encoding="utf-8") as f_a:
        w_n = csv.DictWriter(f_a, fieldnames=["ad", "tel"]) #key
        #w_n.writeheader() #başlığı/key'ler yazar
        ad = input("Name..: ").title()
        tel = int(input("Phone No.: "))
        w_n.writerow({"ad":ad, "tel":tel})

def find_records(file):
    with open(file, mode="r") as f_r:
        name = input("Searched Name..: ").title()
        r_n = csv.DictReader(f_r)
        for i in r_n:
            if i['ad']==name:
                print(i["ad"],":", i["tel"])
                break
        else:
            print(name, "was not found")


def del_records(file):
    print("Remove Name and Number")
    with open(file, 'r') as inp, open('phone_edit.csv', 'w') as out:
        #writer = csv.writer(out)
        writer = csv.DictWriter(out, fieldnames=["ad", "tel"]) #key
        writer.writeheader()
        ara = input("Deleted Name..: ").title()
        for row in csv.DictReader(inp):
            if row['ad'] != ara:
                writer.writerow(row)
    os.remove("phone.csv")
    os.rename("phone_edit.csv","phone.csv")


def update_records(file):
    fields = ["ad", "tel"]
    with open('phone.csv', 'r') as inp, open('phone_edit.csv', 'w') as out:
        reader = csv.DictReader(inp, fieldnames=fields)
        writer = csv.DictWriter(out, fieldnames=fields)
        writer.writeheader()
        ara = input("Updated Name..: ").title()
        for row in reader:
            if row['ad'] == str(ara):
                print('Updating..: ', row['ad'])
                name = input("New name..: ")
                tel = int(input("New Phone No..: "))
                row['ad'], row['tel'] = name, tel
            
            row = {'ad': row['ad'], 'tel': row['tel']}
            writer.writerow(row)

    shutil.move('phone_edit.csv', 'phone.csv')

def quit():
    print("The Programme Ended.")


def menu():
    print('1. List Record')
    print('2. Add Record')
    print('3. Delete Record')
    print('4. Find Record')
    print('5. Update Record')
    print('6. Quit')
    print()
    menu_choice = 0
    while menu_choice != 6:
        menu_choice = int(input("Choice (1-6)..: "))
        if menu_choice == 1:
            list_records(file)
    
        elif menu_choice == 2:
            add_records(file)
    
        elif menu_choice == 3:
            del_records(file)
    
        elif menu_choice == 4:
            find_records(file)
        
        elif menu_choice == 5:
            update_records(file)

        elif menu_choice==6:
            quit()

#main program
if __name__=="__main__":
    file = "phone.csv"
    init_records(file)
    menu()
