import ctypes
from .lib_loader import c_lib


# Node* createNode(int id, char* name, char* author);
c_lib.createNode.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
c_lib.createNode.restype = ctypes.c_void_p

def create_node(book_id: int, name: str, author: str):
    name_bytes = name.encode('utf-8')
    author_bytes = author.encode('utf-8')
    return c_lib.createNode(book_id, name_bytes, author_bytes)


# Node* insertNode(Node* root, Node* n);
c_lib.insertNode.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
c_lib.insertNode.restype = ctypes.c_void_p

def insert_node(root, node):
    return c_lib.insertNode(root, node)


# typedef void (*Callback)(int id, const char* name, const char* author);
CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)


# void inorden(Node* root, Callback callback);
c_lib.inorden.argtypes = [ctypes.c_void_p, CALLBACK]
c_lib.inorden.restype = None

def inorden_data(root):
    books = []
    def get_books_data(book_id, name, author):
        books.append({
            "book_id": book_id,
            "name": name.decode('utf-8'),
            "author": author.decode('utf-8')
        })
    c_lib.inorden(root, CALLBACK(get_books_data))
    return books


# void preorden(Node* root, Callback callback);
c_lib.preorden.argtypes = [ctypes.c_void_p, CALLBACK]
c_lib.preorden.restype = None

def preorden_data(root):
    books = []
    def get_books_data(book_id, name, author):
        books.append({
            "book_id": book_id,
            "name": name.decode('utf-8'),
            "author": author.decode('utf-8')
        })
    c_lib.preorden(root, CALLBACK(get_books_data))
    return books


# int getHeight(Node* n)
c_lib.getHeight.argtypes = [ctypes.c_void_p]
c_lib.getHeight.restype = ctypes.c_int

def get_root_height(root):
    return c_lib.getHeight(root)


# void searchNodeById(Node* root, int id, Callback callback)
c_lib.searchNodeById.argtypes = [ctypes.c_void_p, ctypes.c_int, CALLBACK]
c_lib.searchNodeById.restype = None

def search_book_by_id(root, book_id):
    book = {}
    def get_book_data(book_id, name, author):
        book["book_id"] = book_id
        book["name"] = name.decode('utf-8')
        book["author"] = author.decode('utf-8')
    c_lib.searchNodeById(root, book_id, CALLBACK(get_book_data))
    return book


# Node* deleteNode(Node* root, int id);
c_lib.deleteNode.argtypes = [ctypes.c_void_p, ctypes.c_int]
c_lib.deleteNode.restype = ctypes.c_void_p

def delete_book_by_id(root, book_id):
    return c_lib.deleteNode(root, book_id)
