
from views.console_menu import run_console_app
from views.main_window import run_gui_app

from models.avl import AVLTree
from models.stack import ActionStack

if __name__ == '__main__':
    print("Connecting with C...\n")

    tree = AVLTree()
    actions = ActionStack()

    # run_console_app(tree, actions)
    run_gui_app(tree, actions)
