import os
from bindings.avl_tree import (
    create_node, 
    insert_node,
    get_root_height, 
    inorden_data, 
    preorden_data, 
    search_book_by_id, 
    delete_book_by_id,
    delete_tree
)
from bindings.file_manager import save_tree_to_csv, load_tree_from_csv


class AVLTree():
    def __init__(self) -> None:
        self.root = None
        self.count_id = 0
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "..", "..", "data", "books.csv")
        self.filename = file_path
        self.load_from_csv(self.filename)

    
    def insert(self, book_name: str, book_author: str, book_id: int = None) -> int:
        if book_id is None:
            self.count_id += 1
            book_id = self.count_id
        else:
            if book_id > self.count_id:
                self.count_id = book_id
        
        node = create_node(book_id, book_name, book_author)
        self.root = insert_node(self.root, node)

        return book_id

    
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

    
    def delete_tree(self):
        self.root = delete_tree(self.root)


    def load_from_csv(self, filename: str):
        self.root = load_tree_from_csv(self.root, filename)
        
        books = self.inorden()
        if books:
            highest_id = max(book['book_id'] for book in books)
            self.count_id = highest_id

    
    def save_to_csv(self, filename: str) -> int:
        return save_tree_to_csv(self.root, filename)
