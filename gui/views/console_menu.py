
from models.avl import AVLTree
from models.stack import HistoryStack, ActionType


def insert_node(tree: AVLTree, book_id: int, name: str, author: str):
    tree.insert(book_id, name, author)


def get_height(tree: AVLTree):
    height = tree.height()
    print(f"Tree height: {height}")


def inorden(tree: AVLTree):
    print("\nPrinting inorden:")
    books = tree.inorden()
    for book in books:
        print(f"ID: {book['book_id']} | Name: {book['name']} | Author: {book['author']}")


def preorden(tree: AVLTree):
    print("\nPrinting preorden:")
    books = tree.preorden()
    for book in books:
        print(f"ID: {book['book_id']} | Name: {book['name']} | Author: {book['author']}")


def search_book(tree: AVLTree):
    while (True):
        book_id = input("\nSearch book by id or '*' to exit: ")
        if book_id == "*": break
        book = tree.search(int(book_id))
        if book:
            print("Book found!")
            print(f"ID: {book['book_id']} | Name: {book['name']} | Author: {book['author']}")
        else:
            print("Book not found!")


def delete_book(tree: AVLTree):
    while (True):
        book_id = input("\nDelete book by id or '*' to exit: ")
        if book_id == "*": break

        book = tree.search(int(book_id))
        if book:
            tree.delete(int(book_id))
            print(f"Book [{book['name']}] deleted")
        else:
            print("Book not found!")


def run_console_app():
    
    tree = AVLTree()
    historial = HistoryStack() #  TODO: create stack actions


    book_id = 0

    while (True):
        print("\n1) Insert\n2) Height\n3) Inorden\n4) Preorden\n5) Search book\n6) Delete book\n7) Exit")
        option = int(input("Option: "))
        print("\n")

        if option == 7:
            break
        elif option == 1:
            book_id += 1
            name = input("Book: ")
            author = input("Author: ")
            insert_node(tree, book_id, name, author)
        elif option == 2:
            get_height(tree)
        elif option == 3:
            inorden(tree)
        elif option == 4:
            preorden(tree)
        elif option == 5:
            search_book(tree)
        elif option == 6:
            delete_book(tree)
        else:
            print("Invalid option")
