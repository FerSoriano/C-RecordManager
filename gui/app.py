
from views.console_menu import run_console_app
from views.main_window import run_gui_app

from models.avl import AVLTree
from models.stack import ActionStack, ActionType

if __name__ == '__main__':
    print("Connecting with C...\n")

    def insert_node(tree: AVLTree, action: ActionStack, name: str, author: str):
        tree.insert(name, author)
        action.push(ActionType.ACTION_INSERT, tree.count_id, name, author)

    def load_test_books(tree: AVLTree, actions: ActionStack): 
        insert_node(tree, actions, "Dune", "Frank Herbert")
        insert_node(tree, actions, "1984", "George Orwell")
        insert_node(tree, actions, "Fahrenheit 451", "Ray Bradbury")
        insert_node(tree, actions, "Un Mundo Feliz", "Aldous Huxley")
        insert_node(tree, actions, "Fundación", "Isaac Asimov")

    tree = AVLTree()
    actions = ActionStack()

    load_test_books(tree, actions)

    # run_console_app(tree, actions)
    run_gui_app(tree, actions)
