import ctypes
from .lib_loader import c_lib

# Node* createNode(int id, char* name, char* author);
c_lib.createNode.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
c_lib.createNode.restype = ctypes.c_void_p
def createNode(id: int, name: str, author: str):
    name_bytes = name.encode('utf-8')
    author_bytes = author.encode('utf-8')
    return c_lib.createNode(id, name_bytes, author_bytes)

# Node* insertNode(Node* root, Node* n);
c_lib.insertNode.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
c_lib.insertNode.restype = ctypes.c_void_p
def insertNode(root, node):
    return c_lib.insertNode(root, node)

# typedef void (*Callback)(int id, const char* name, const char* author);
CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)

# void inorden(Node* root, Callback callback);
c_lib.inorden.argtypes = [ctypes.c_void_p, CALLBACK]
c_lib.inorden.restype = None
def inorden_data(root):
    books = []
    def get_books_data(id, name, author):
        books.append({
            "id": id,
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
    def get_books_data(id, name, author):
        books.append({
            "id": id,
            "name": name.decode('utf-8'),
            "author": author.decode('utf-8')
        })
    c_lib.preorden(root, CALLBACK(get_books_data))
    return books
    
# int getHeight(Node* n)
c_lib.getHeight.argtypes = [ctypes.c_void_p]
c_lib.getHeight.restype = ctypes.c_int
def getRootHeight(root):
    return c_lib.getHeight(root)
