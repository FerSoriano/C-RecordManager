from bindings.avl_tree import (
    create_node, 
    insert_node,
    get_root_height, 
    inorden_data, 
    preorden_data, 
    search_book_by_id, 
    delete_book_by_id
)


class AVLTree():
    def __init__(self) -> None:
        self.root = None

    
    def insert(self, book_id: int, name: str, author: str) -> None:
        node = create_node(book_id, name, author)
        self.root = insert_node(self.root, node)

    
    def height(self) -> int:
        return get_root_height(self.root)
    

    def inorden(self) -> list:
        return inorden_data(self.root)
    
    
    def preorden(self) -> list:
        return preorden_data(self.root)
    

    def search(self, book_id: int) -> dict:
        return search_book_by_id(self.root, book_id)
    

    def delete(self, book_id: int) -> None:
        self.root = delete_book_by_id(self.root, book_id)
