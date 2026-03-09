from bindings.avl_tree import create_node, insert_node
from views.console_menu import run_console_app


if __name__ == '__main__':
    print("Connecting with C...\n")

    root = None

    root = insert_node(root, create_node(1, "Test", "Fer Soriano"))
    root = insert_node(root, create_node(2, "Test", "Fer Soriano"))
    root = insert_node(root, create_node(3, "Test", "Fer Soriano"))
    root = insert_node(root, create_node(4, "Test", "Fer Soriano"))
    root = insert_node(root, create_node(5, "Test", "Fer Soriano"))
    root = insert_node(root, create_node(6, "Test", "Fer Soriano"))
    root = insert_node(root, create_node(7, "Test", "Fer Soriano"))
    root = insert_node(root, create_node(8, "Test", "Fer Soriano"))

    print("Data inserted succesfully from C!")
    
    root = run_console_app(root)