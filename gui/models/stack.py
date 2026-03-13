from bindings.history_stack import (
    ActionType,
    push_to_history,
    pop_from_history,
    peek_from_history,
    show_history
)


class ActionStack:
    def __init__(self) -> None:
        self.root = None


    def push(self, action: ActionType, book_id: int, name: str, author: str) -> None:
        self.root = push_to_history(self.root, action, book_id, name, author)


    def pop(self) -> dict | None:
        if self.root == None:
            return None
        self.root, book_data = pop_from_history(self.root)
        return book_data


    def peek(self) -> dict | None:
        if self.root == None:
            return None
        return peek_from_history(self.root)


    def get_all_actions(self) -> list:
        return show_history(self.root)
 
        
    def is_empty(self) -> bool:
        return self.root is None