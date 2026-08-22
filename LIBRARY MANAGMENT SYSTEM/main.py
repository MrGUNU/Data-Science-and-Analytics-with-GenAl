import json
import random
import string
from pathlib import Path
from datetime import datetime

class Library:
    database = "library.json"
    data = {"books": [], "members": []}

    # Load existing data to Json

    if Path(database).exists():
        with open(database, "r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
    else:
        with open(database, "w") as f:
            json.dump(data,f,indent=4)

    
    def gen_id(Prefix = "B"):
        random_id = ""
        for i in range(5):
            random_id += random.choice(string.ascii_uppercase + string.digits)

        return Prefix + "-" + random_id

    @classmethod
    def save_data(cls):
        with open(cls.database, 'w') as f:
            json.dump(cls.data,f,indent=4, default=str)

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author of the book: ")
        copies = int(input("How many copies: "))


        book = {
            "id" : Library.gen_id(),
            "title" : title,
            "author" : author,
            "total_copies" : copies,
            "available_copies" : copies,
            "added_on" : datetime.now().strftime("%Y-%m-%d %H-%M-%S") 
        }

        Library.data['books'].append(book)
        Library.save_data()

    def list_books(self):
        if not Library.data['books']:
            print("Sorry no books found")
            return

        for b in Library.data['books']:
            print(f"{b['id']:12} {b['title'][:24]:25} {b['author'][:19]:20} {b['total_copies']}/{b['available_copies']:>3}")

        print()

    def add_members(self):
        name = input("Enter your name: ")
        email = input("Enter your mail id: ")

        members = {
            "id": Library.gen_id("M"),
            "name": name,
            "email": email,
            "borrowed": []
        }

        Library.data['members'].append(members)
        Library.save_data()
        print("Member added sucessfully")

    def list_members(self):
        if not Library.data['members']:
            print("There are no members")
        for m in Library.data['members']:
            print(f"{m['id']:12} {m['name'][:24]:25} {m['email'][:29]:30}")
            print("This guy has currently")
            print(f"{m['borrowed']}")
        print()

    def borrow(self):
        member_id = input("Enter the member ID: ").strip()
        members = [m for m in Library.data['members'] if m['id'] == member_id]
        if not members:
            print("No such ID exist")
            return
        members = members[0]

        book_id = input("Enter the book ID: ")
        books = [b for b in Library.data['books'] if b['id'] == book_id]

        if not books:
            print("Sorry no such id of book exist")
            return
        book = books[0]

        if book['available_copies'] <= 0:
            print("Sorry no books available")
            return

        borrow_entry = {
            "book_id": book['id'],
            "title": book['title'],
            "borrow_on": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        }

        members['borrowed'].append(borrow_entry)
        book['available_copies'] -= 1
        Library.save_data()


    def return_book(self):
        member_id = input("Enter the mermber ID : ").strip()
        members = [m for m in Library.data['members'] if m['id'] == member_id]
        if not members:
            print("no such Id exist")
            return 
        
        member = members[0]

        if not member['borrowed']:
            print("no borrowed books")
            return 
        
        print("borrowed books")
        for i, b in enumerate(member['borrowed'],start = 1):
            print(f"{i}. {b['title']} ({b['book_id']})")
        
        try:
            choice = int(input("enter number to return : - "))
            selected = member['borrowed'].pop(choice - 1)
        except Exception as err:
            print("invalid value ")
        
        books = [bk for bk in Library.data['books'] if bk['id'] == selected['book_id'] ]
        if books:
            books[0]['available_copies'] += 1
        
        Library.save_data()

obj = Library()

while True:
        
    print("="*50)
    print("Library Management System")
    print("="*50)
    print("1. Add Book")
    print("2. List Books")
    print("3. Add Members")
    print("4. List Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("0. Exit the Portal")
    print("-"*50)

    choice = input("What do you want to do: ")

    if choice == "1":
        obj.add_book()

    if choice == "2":
        obj.list_books()

    if choice == "3":
        obj.add_members()

    if choice == "4":
        obj.list_members()

    if choice == "5":
        obj.borrow()

    if choice == "6":
        obj.return_book()

    if choice == "0":
        exit(0)