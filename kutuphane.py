import os

class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0) 
        books = self.file.read().splitlines()
        if not books:
            print("\nNo books were found in the library!\n")
        else:
            print("\n List of Books: \n")
            for book in books:
                book_info = book.split(",")
                print(f"Book Title: {book_info[0]}")
                print(f"Author: {book_info[1]}")
                print(f"Release Date: {book_info[2]}")
                print(f"Number of Pages: {book_info[3]}\n")


    def add_book(self):
        title = input("\nEnter book title: ")
        author = input("Enter book author: ")
        year = input("Enter first release year: ")
        pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{year},{pages}\n"
        self.file.write(book_info)
        print(f"\nThe book with named '{title}' has been added to the library.\n")

    def remove_book(self):
        book_title = input("\nEnter the book title to remove: ")
        with open('books.txt', 'r') as file:
            books = file.readlines()

        book_index = None
        for i, book in enumerate(books):
            if book.startswith(f"{book_title},"):
                 book_index = i
                 break
            
        if book_index is not None:
            del books[book_index]
            print(f"Book '{book_title}' has been removed from the library.")
        else:
            print(f"Book '{book_title}' not found in the library.")
            return
       
        with open('books.txt', 'w') as file:
            pass
 
        with open('books.txt', 'a') as file:
            for book in books:
                file.write(book)
        
        

lib = Library()

while True:
    print(" *** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
