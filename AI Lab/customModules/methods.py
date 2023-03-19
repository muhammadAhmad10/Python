#books={'Intro to CS':{'Book Name':'Intro to CS','Auther Name':'Ahmad','Book ID': '123','No of Copies':3}}
class Library:
    def __init__(self):
        self.books = {'Intro to CS': {'Book Name': 'Intro to CS', 'Author Name': 'Ahmad', 'Book ID': '123', 'No of Copies': 3}}

    def addBook(self):
        name = input("Enter the name of book: ")
        author = input("Enter the author of book: ")
        id = input("Enter the ISBN of book: ")
        copies = int(input('Enter the number of copies: '))
        self.books[name] = {'Book Name': name, 'Author Name': author, 'Book ID': id, 'No of Copies': copies}

    def removeBook(self):
        name = input("Enter the name of book you want to delete: ")
        del self.books[name]

    def searchBook(self):
        name = input("Enter the name of book you want to search: ")
        if self.books.get(name):
            print('Book found.')
            print(self.books[name])

    def updateBook(self):
        name = input("Enter the name of book you want to update: ")
        author = input("Enter the author of book: ")
        id = input("Enter the ISBN of book: ")
        self.books[name] = {'Book Name': name, 'Author Name': author, 'Book ID': id, 'No of Copies': self.books[name]['No of Copies']}

    def viewBooks(self):
        print(self.books)

    def lendBook(self):
        name = input("Enter the name of book you want to lend: ")
        print(self.books[name])
        if self.books.get(name):
            copy = self.books[name]['No of Copies']
            copy = copy - 1
            self.books[name]['No of Copies'] = copy
        print(self.books[name])

    def returnBook(self):
        name = input("Enter the name of book you want to return: ")
        print(self.books[name])
        if self.books.get(name):
            copy = self.books[name]['No of Copies']
            copy = copy + 1
            self.books[name]['No of Copies'] = copy
        print(self.books[name])


library = Library()













    # def addBook():
    #     name = input("Enter the name of book: ")
    #     auther = input("Enter the auther of book: ")
    #     id  = input("Enter the ISBN of book: ")
    #     copies = int(input('Enter the number of copies: '))
    #     books[name] = {'Book Name':name,'Auther Name':auther,'Book ID': id,'No of Copies':copies}
    #     print(books)

    # def removeBook():
    #     name = input("Enter the name of book you want to delete: ")
    #     del books[name]
    #     print(books)

    # def searchBook():
    #     name  = input("Enter the name of book you want to search: ")
    #     if(books[name]):
    #         print('Book found.')
    #     print(books[name])
    #     print(books)

    # def updateBook():
    #     name = input("Enter the name of book you want to update: ")
    #     auther = input("Enter the auther of book: ")
    #     id  = input("Enter the ISBN of book: ")
    #     books[name] = {'Book Name':name,'Auther Name':auther,'Book ID': id,'No of Copies':books[name]['No of Copies']}
    #     print(books)
    # def viewBooks():
    #     print(books)
    # def lendBook():
    #     name = input("Enter the name of book you want to lend: ")
    #     print(books[name])
    #     if(books[name]):
    #         copy = books[name]['No of Copies']
    #         copy = copy-1
    #         books[name]['No of Copies'] = copy
    #     print(books[name])
    #     print(books)

    # def returnBook():
    #     name = input("Enter the name of book you want to return: ")
    #     print(books[name])
    #     if(books[name]):
    #         copy = books[name]['No of Copies']
    #         copy = copy+1
    #         books[name]['No of Copies'] = copy
    #     print(books[name])
    #     print(books)
