class Library:
    def __init__(self, Library_name, listofbooks, originalbooks):
        self.Libraryname = Library_name
        self.books = listofbooks
        self.original = originalbooks

    def displaybooks(self):
        print("\nBooks currently available in library")
        for books in self.books:
            print(f" - {books}")

    def lendbook(self):
        name = input("Enter your name - ")
        book = input("Enter book name you want to borrow - ")
        if book in self.books:
            print(
                f"You have been issued {book}. Please keep it safe and return it within 30 days")
            self.books.remove(book)
            dict.update({book: name})
            return True
        elif book in self.original:
            print(
                f"Sorry {name}, This book has already been issued to {dict.get(book)}. Please wait until the book is available")
            return True
        else:
            print("Sorry, this book is not available in our library")

    def returnbook(self):
        name = input("Enter your name - ")
        book = input("Enter book name you want to return - ")
        self.books.append(book)
        dict.pop(book)
        print("Thanks for returning book. have a nice day")

    def addbook(self):
        book = input("Enter book name you want to donate - ")
        self.books.append(book)
        print("Thanks for donating a book. have a nice day")


if __name__ == '__main__':

    harshlibrary = Library("Harsh's Library", ["Algorithms", "Django", "Clrs", "Python Notes"], [
                           "Algorithms", "Django", "Clrs", "Python Notes"])
    dict = {}
    while True:
        print('''\n====== Welcome to Central Library ======
        please select an option
        1. desplay list of books
        2. borrow book
        3. return book
        4. donate a book to library
        5. exit
        ''')
        a = input("Enter your choise - ")

        if int(a) == 1:
            harshlibrary.displaybooks()

        elif int(a) == 2:
            harshlibrary.lendbook()

        elif int(a) == 3:
            harshlibrary.returnbook()

        elif int(a) == 4:
            harshlibrary.addbook()

        elif int(a) == 5:
            print("\nThanks for visiting Central library")
            exit()
        else:
            print("Invalid choise")
