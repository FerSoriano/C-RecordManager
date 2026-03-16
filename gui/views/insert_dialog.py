import customtkinter as ctk
from tkinter import messagebox
from models.stack import ActionType

class InsertBookDialog(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.title("Insertar Nuevo Libro")
        self.geometry("400x300")
        self.resizable(False, False) # Evitamos que el usuario deforme la ventana
        
        self.transient(parent)
        self.grab_set()
        self.focus_set()

        self.font_base = ctk.CTkFont(family="Roboto", size=14)
        self.font_title = ctk.CTkFont(family="Roboto", size=20, weight="bold")

        self.parent = parent 

        self._build_ui()

    def _build_ui(self):
        self.lbl_title = ctk.CTkLabel(self, text="Datos del Libro", font=self.font_title)
        self.lbl_title.grid(row=0, column=0, columnspan=2, pady=(20, 20))

        # Book id
        self.lbl_id = ctk.CTkLabel(self, text="ID:", font=self.font_base)
        self.lbl_id.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.entry_id = ctk.CTkEntry(self, width=200, font=self.font_base, text_color="gray")
        self.entry_id.grid(row=1, column=1, padx=(0, 20), pady=10)
        self.entry_id.insert(0, str(self.get_new_book_id()))
        self.entry_id.configure(state="readonly")

        # Book name
        self.lbl_name = ctk.CTkLabel(self, text="Título:", font=self.font_base)
        self.lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.entry_name = ctk.CTkEntry(self, width=200, font=self.font_base)
        self.entry_name.grid(row=2, column=1, padx=(0, 20), pady=10)

        # Author
        self.lbl_author = ctk.CTkLabel(self, text="Autor:", font=self.font_base)
        self.lbl_author.grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.entry_author = ctk.CTkEntry(self, width=200, font=self.font_base)
        self.entry_author.grid(row=3, column=1, padx=(0, 20), pady=10)

        # btns
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.grid(row=4, column=0, columnspan=2, pady=(20, 0))


        self.btn_cancel = ctk.CTkButton(self.btn_frame, text="Cancelar", width=100, 
                                        fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),
                                        command=self.destroy)
        self.btn_cancel.grid(row=0, column=0, padx=10)


        self.btn_save = ctk.CTkButton(self.btn_frame, text="Guardar", width=100, 
                                      command=self.on_save_click)
        self.btn_save.grid(row=0, column=1, padx=10)


    def on_save_click(self):
        book_name = self.entry_name.get().strip()
        book_author = self.entry_author.get().strip()

        if not book_name or not book_author:
            messagebox.showwarning("Error de Validación", "El Título y el Autor no pueden estar vacíos.")
            return
        
        if self.bookExists(book_name, book_author):
            messagebox.showwarning("Libro Duplicado", f"El libro '{book_name}' ya está registrado en el catálogo.")
            return
        
        book_id = self.parent.avl_root.insert(book_name=book_name, book_author=book_author)
        self.parent.stack_root.push(
            ActionType.ACTION_INSERT,
            book_id,
            book_name,
            book_author
        )

        self.parent.refresh_history_table()
        self.parent.refresh_table()

        # messagebox.showinfo("Éxito", f"Se agregó '{book_name}' correctamente.")
        self.destroy()


    def get_new_book_id(self):
        return self.parent.avl_root.count_id + 1
    

    def bookExists(self, book_name: str, book_author: str) -> bool:
        books = self.parent.avl_root.inorden()
        if not books:
            return False
        for book in books:
            if book['name'].lower() == book_name.lower() and book['author'].lower() == book_author.lower():
                return True
        return False
