import ctypes
from .lib_loader import c_lib


# int saveTreeToCSV(Node* root, const char* filename);
c_lib.saveTreeToCSV.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
c_lib.saveTreeToCSV.restype = ctypes.c_int

def save_tree_to_csv(root, filename) -> int:
    """
    Exports the current AVL tree records to a CSV file.

    This function interfaces with the C backend's saveTreeToCSV implementation.
    It passes the root pointer of the tree and the target filename to perform 
    the file operation.

    Args:
        root (ctypes.c_void_p): A pointer to the root node of the AVL tree.
        filename (str): The destination file path for the CSV output.

    Returns:
        int: 1 if the save operation succeeded, 0 if it failed.
    """
    return c_lib.saveTreeToCSV(root, filename.encode('utf-8'))


# Node* loadTreeFromCSV(Node* root, const char* filename);
c_lib.loadTreeFromCSV.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
c_lib.loadTreeFromCSV.restype = ctypes.c_void_p

def load_tree_from_csv(root, filename):
    """
    Loads record data from a CSV file into the AVL tree.

    This function calls the C backend's loadTreeFromCSV. It parses the 
    specified file and inserts each record into the existing AVL structure.

    Args:
        root (ctypes.c_void_p): A pointer to the current root node of the AVL tree.
    filename (str): The path to the CSV file containing the data.

    Returns:
        ctypes.c_void_p: A pointer to the new root of the AVL tree after loading.
    """
    return c_lib.loadTreeFromCSV(root, filename.encode('utf-8'))