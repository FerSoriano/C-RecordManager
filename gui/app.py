
from views.console_menu import run_console_app
from views.main_window import run_gui_app

from models.avl import AVLTree
from models.stack import ActionStack, ActionType

if __name__ == '__main__':
    print("Connecting with C...\n")

    def insert_node(tree: AVLTree, action: ActionStack,book_id: int, name: str, author: str):
        tree.insert(book_id, name, author)
        action.push(ActionType.ACTION_INSERT, book_id, name, author)

    def load_test_books(tree: AVLTree, action: ActionStack): 
        insert_node(tree, action, 1, "Dune", "Frank Herbert")
        insert_node(tree, action, 2, "1984", "George Orwell")
        insert_node(tree, action, 3, "Fahrenheit 451", "Ray Bradbury")
        insert_node(tree, action, 4, "Un Mundo Feliz", "Aldous Huxley")
        insert_node(tree, action, 5, "Fundación", "Isaac Asimov")

    tree = AVLTree()
    actions = ActionStack()

    load_test_books(tree, actions)

    # run_console_app(tree, actions)
    run_gui_app(tree, actions)
