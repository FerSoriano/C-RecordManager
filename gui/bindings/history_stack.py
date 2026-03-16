import ctypes
from .lib_loader import c_lib
from enum import IntEnum


class ActionType(IntEnum):
    ACTION_INSERT = 0
    ACTION_DELETE = 1


# typedef void (*Callback)(const char* action, int id);
CALLBACK = ctypes.CFUNCTYPE (
    None, # return
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_char_p, 
    ctypes.c_char_p
)


# StackNode* push(StackNode* s, ActionType action, const int id, const char* name, const char* author);
c_lib.push.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
c_lib.push.restype = ctypes.c_void_p

def push_to_history(stack, action: ActionType, book_id: int, name: str, author: str):
    name_bytes = name.encode('utf-8')
    author_bytes = author.encode('utf-8')
    return c_lib.push(stack, action.value, book_id, name_bytes, author_bytes)


# void pop(StackNode** s, CallbackPop callback);
c_lib.pop.argtypes = [ctypes.POINTER(ctypes.c_void_p), CALLBACK]
c_lib.pop.restype = None

def pop_from_history(stack):
    book = {}
    def get_book(action, book_id, name, author):
        book["action"] = action.decode('utf-8') if action else None
        book["book_id"] = book_id
        book["name"] = name.decode('utf-8') if name else None
        book["author"] = author.decode('utf-8') if author else None
    
    stack_ptr = ctypes.c_void_p(stack)
    c_lib.pop(ctypes.byref(stack_ptr), CALLBACK(get_book))
    new_stack = stack_ptr.value
    
    return new_stack, book


# void peek(StackNode* s, Callback callback);
c_lib.peek.argtypes = [ctypes.c_void_p, CALLBACK]
c_lib.peek.restype = None

def peek_from_history(stack):
    book = {}
    def get_book(action, book_id, name, author):
        book["action"] = action.decode('utf-8') if action else None
        book["book_id"] = book_id
        book["name"] = name.decode('utf-8') if name else None
        book["author"] = author.decode('utf-8') if author else None
    c_lib.peek(stack, CALLBACK(get_book))
    return book


# void showStack(StackNode* s, Callback callback);
c_lib.showStack.argtypes = [ctypes.c_void_p, CALLBACK]
c_lib.showStack.restype = None

def show_history(stack):
    actions = []
    def get_history(action, book_id, name, author):
        actions.append({
            "action": action.decode('utf-8') if action else None,
            "book_id": book_id,
            "name": name.decode('utf-8') if name else None,
            "author": author.decode('utf-8') if author else None
        })
    c_lib.showStack(stack, CALLBACK(get_history))
    return actions


# StackNode* emptyStack(StackNode* s)
c_lib.emptyStack.argtypes = [ctypes.c_void_p]
c_lib.emptyStack.restype = ctypes.c_void_p

def empty_stack(stack):
    return c_lib.emptyStack(stack)
