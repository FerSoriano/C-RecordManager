from bindings.avl_tree import get_root_height, inorden_data, preorden_data, search_book_by_id, delete_book_by_id


def getHeight(root):
    height = get_root_height(root)
    print(f"Tree height: {height}")


def inorden(root):
    print("\nPrinting inorden:")
    books = inorden_data(root)
    for book in books:
        print(f"ID: {book['id']} | Name: {book['name']} | Author: {book['author']}")


def preorden(root):
    print("\nPrinting preorden:")
    books = preorden_data(root)
    for book in books:
        print(f"ID: {book['id']} | Name: {book['name']} | Author: {book['author']}")


def search_book(root):
    while (True):
        book_id = input("\nSearch book by id or '*' to exit: ")
        if book_id == "*": break
        book = search_book_by_id(root, int(book_id))
        if book:
            print("Book found!")
            print(f"ID: {book['id']} | Name: {book['name']} | Author: {book['author']}")
        else:
            print("Book not found!")


def delete_book(root):
    while (True):
        book_id = input("\nDelete book by id or '*' to exit: ")
        if book_id == "*": break

        book = search_book_by_id(root, int(book_id))
        if book:
            root = delete_book_by_id(root, int(book_id))
            print(f"Book [{book['name']}] deleted")
        else:
            print("Book not found!")

    return root


def run_console_app(root):
    while (True):
        print("\n1) Height\n2) Inorden\n3) Preorden\n4) Search book\n5) Delete book\n6) Exit")
        option = int(input("Option: "))
        print("\n")

        if option == 6:
            break
        elif option == 1:
            getHeight(root)
        elif option == 2:
            inorden(root)
        elif option == 3:
            preorden(root)
        elif option == 4:
            search_book(root)
        elif option == 5:
            root = delete_book(root)
        else:
            print("Invalid option")
