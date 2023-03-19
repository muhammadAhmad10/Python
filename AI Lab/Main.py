from customModules import methods
# print('1-Add book   2-Delete book  3-Update book \n4-Search book    5-View all books    6-Lend book  7-Return book')
# choice = int(input("Enter your choice: "))

while True:
    print('1-Add book   2-Delete book  3-Update book    4-Search book    \n5-View all books    6-Lend book  7-Return book')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        methods.library.addBook()
    elif choice == 2:
        methods.library.removeBook()
    elif choice == 3:
        methods.library.updateBook()
    elif choice == 4:
        methods.library.searchBook()
    elif choice == 5:
        methods.library.viewBooks()
    elif choice == 6:
        methods.library.lendBook()
    elif choice == 7:
        methods.library.returnBook()
    else:
        break