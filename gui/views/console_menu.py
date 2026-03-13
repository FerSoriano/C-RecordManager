
from models.avl import AVLTree
from models.stack import ActionStack, ActionType


def insert_node(tree: AVLTree, action: ActionStack,book_id: int, name: str, author: str):
    tree.insert(book_id, name, author)
    action.push(ActionType.ACTION_INSERT, book_id, name, author)


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


def delete_book(tree: AVLTree, action: ActionStack):
    while (True):
        book_id = input("\nDelete book by id or '*' to exit: ")
        if book_id == "*": break

        book = tree.search(int(book_id))
        if book:
            action.push(ActionType.ACTION_DELETE, book['book_id'], book['name'], book['author'])
            tree.delete(int(book_id))
            print(f"Book [{book['name']}] deleted")
        else:
            print("Book not found!")


def show_history_actions(actions: ActionStack):
    for action in actions.get_all_actions():
        print(action)


def undo_last_action(actions: ActionStack, tree: AVLTree) -> bool:
    last_action = actions.peek()
    if not last_action:
        print("No action found!")
        return False
    
    print(f"\nLast action: {last_action['action']} | Book: {last_action['name']}")
    
    response = input("Do you want to undo the action? (y/n): ")
    if response.lower() == 'y':
        book_undo = actions.pop()

        if book_undo is not None:
            if last_action['action'] == 'Delete':
                tree.insert(
                    book_undo['book_id'],
                    book_undo['name'],
                    book_undo['author'],
                )
            else:
                tree.delete(book_undo['book_id'])
            return True
        
    return False


def load_test_books(tree: AVLTree, action: ActionStack): 
    insert_node(tree, action, 1, "Dune", "Frank Herbert")
    insert_node(tree, action, 2, "1984", "George Orwell")
    insert_node(tree, action, 3, "Fahrenheit 451", "Ray Bradbury")
    insert_node(tree, action, 4, "Un Mundo Feliz", "Aldous Huxley")
    insert_node(tree, action, 5, "Fundación", "Isaac Asimov")


def run_console_app():
    
    tree = AVLTree()
    actions = ActionStack()


    load_test_books(tree, actions)
    book_id = 5

    while (True):
        print("\n1) Insert\n2) Height\n3) Inorden\n4) Preorden\n5) Search book\n6) Delete book\n-1) Exit")
        print("\n0) Historial de acciones\n")
        option = int(input("Option: "))
        print("\n")

        if option == -1:
            break
        elif option == 0:
            show_history_actions(actions)
            if undo_last_action(actions, tree):
                print("Undo action!\n")
        elif option == 1:
            book_id += 1
            name = input("Book: ")
            author = input("Author: ")
            insert_node(tree, actions, book_id, name, author)
        elif option == 2:
            get_height(tree)
        elif option == 3:
            inorden(tree)
        elif option == 4:
            preorden(tree)
        elif option == 5:
            search_book(tree)
        elif option == 6:
            delete_book(tree, actions)
        else:
            print("Invalid option")
