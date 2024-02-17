
class Library:
    def __init__(self, fileName):  #constructor
        self.fileName = fileName
        self.file = open(self.fileName, "a+")

    def __del__(self):       #destructor
        self.file.close()

    def listBooks(self):
        with open(self.fileName, "r", encoding="utf-8") as file:
            for row in file:
                print(row)

    def addBook(self):
        bookName = input("Name of the Book: ")
        author = input("Author of the Book: ")
        releaseDate = input("Release Date: ")
        numberOfPages = input("Number of Pages: ")

        with open(self.fileName, "a+", encoding="utf-8") as file:
            file.write(f"{bookName},{author},{releaseDate},{numberOfPages}\n")

    def removeBook(self):
        bookName = input("Name of the book to delete: ")
        with open(self.fileName, "r+", encoding="utf-8") as file:
            rows = file.readlines()
            file.seek(0)              #start position
            for row in rows:
                if bookName not in row:
                    file.write(row)   #rewriting the file
            file.truncate()           #remove attachments

def main(): #Due to an error, I added the main function.
    lib= Library("books.txt")  #A lib object is created from the Library class and a file name is provided.

    while True:
        print("***** MENU *****\n"
              "1) List Books\n"
              "2) Add Book\n"
              "3) Remove Book\n"
              "q) Exit\n")

        selection = input("Please select an operation from the menu: ")

        if selection == "1":
            print("Books are being listed......\n")
            lib.listBooks()

        elif selection == "2":
            lib.addBook()
            print("Book has been added....\n")

        elif selection == "3":
            lib.removeBook()
            print("The book has been deleted....\n")

        elif selection.lower() == "q":
            print("EXIT\n")
            break

        else:
            print("Wrong selection, please try again..")

if __name__ == "__main__": #Due to an error, I added the main function.
    main()










