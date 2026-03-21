import platform
import customtkinter as ctk
from tkinter import ttk, messagebox

from views.insert_dialog import InsertBookDialog
from models.stack import ActionType

class LibraryApp(ctk.CTk):
    def __init__(self, avl_root, stack_root):
        super().__init__()
        if platform.system() == "Linux":
            ctk.set_widget_scaling(1.5)
            ctk.set_window_scaling(1.5)

        self.font_base = ctk.CTkFont(family="Roboto", size=14)
        self.font_title = ctk.CTkFont(family="Roboto", size=20, weight="bold")

        self.avl_root = avl_root
        self.stack_root = stack_root

        self.title("C-RecordManager: Library System")
        self.geometry("900x650")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Main Layout principal (Grid: 2 cols, 1 row)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._build_sidebar()
        self._build_main_frame()
        self._build_search_order_frame()
        self._build_grid_frame()

        self.refresh_table()
        self.refresh_history_table()
        

    def _build_sidebar(self):
        # TODO: Add Upload from file

        # Left pane - btns
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.sidebar_frame.grid_rowconfigure(5, weight=1) 

        self.lbl_logo = ctk.CTkLabel(self.sidebar_frame, text="Panel Admin", font=self.font_title)
        self.lbl_logo.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.btn_save = ctk.CTkButton(
            self.sidebar_frame, 
            text="Guardar",
            font=self.font_base, 
            command=self.save_to_csv,
            fg_color="#2ecc71", 
            hover_color="#27ae60"
        )
        self.btn_save.grid(row=1, column=0, padx=20, pady=10)

        self.btn_insert = ctk.CTkButton(
            self.sidebar_frame, 
            text="Insertar Libro",
            font=self.font_base, 
            command=self.open_insert_dialog
        )
        self.btn_insert.grid(row=2, column=0, padx=20, pady=10)
        
        self.btn_delete = ctk.CTkButton(
            self.sidebar_frame, 
            text="Eliminar Libro", 
            font=self.font_base, 
            command=self.delete_book
        )
        self.btn_delete.grid(row=3, column=0, padx=20, pady=10)

        self.btn_tree_height = ctk.CTkButton(
            self.sidebar_frame,
            text="Altura Árbol",
            font=self.font_base,
            command=self.show_tree_height
        )
        self.btn_tree_height.grid(row=4, column=0, padx=20, pady=10)

        self.btn_delete_tree = ctk.CTkButton(
            self.sidebar_frame, 
            text="Eliminar Árbol",
            font=self.font_base,
            command=self.delete_tree,
            fg_color="#dc143c", 
            hover_color="#b22222"
        )
        self.btn_delete_tree.grid(row=5, column=0, padx=20, pady=10)

        self.lbl_actions = ctk.CTkLabel(self.sidebar_frame, text="Historial Acciones", font=self.font_title)
        self.lbl_actions.grid(row=6, column=0, padx=20, pady=10)

        # Stack table
        self.history_frame = ctk.CTkFrame(self.sidebar_frame, fg_color="transparent")
        self.history_frame.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")
        self.history_frame.grid_columnconfigure(0, weight=1)
        self.history_frame.grid_rowconfigure(0, weight=1)

        cols_hist = ("action", "name")
        self.tree_history = ttk.Treeview(
            self.history_frame, 
            columns=cols_hist, 
            show="headings", 
            selectmode="none",
            height=5
        )
        self.tree_history.heading("action", text="Acción")
        self.tree_history.heading("name", text="Libro")
        
        self.tree_history.column("action", width=70, anchor="center")
        self.tree_history.column("name", width=100, anchor="w")
        self.tree_history.grid(row=0, column=0, sticky="news")

        # Scrollbar
        self.hist_scrollbar = ctk.CTkScrollbar(self.history_frame, command=self.tree_history.yview)
        self.hist_scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree_history.configure(yscrollcommand=self.hist_scrollbar.set)

        self.btn_undo = ctk.CTkButton(
            self.sidebar_frame, text="Deshacer Última Acción", fg_color="transparent", 
            border_width=2, text_color=("gray10", "#DCE4EE"), font=self.font_base, command=self.undo_last_action
        )
        self.btn_undo.grid(row=8, column=0, padx=20, pady=(10, 20))


    def _build_main_frame(self):
        # Right pane - dashboard        
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="news")
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        self.lbl_title = ctk.CTkLabel(self.main_frame, text="Catálogo de Libros", font=self.font_title)
        self.lbl_title.grid(row=0, column=0, pady=(20, 10))

    
    def _build_grid_frame(self):
        self.grid_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.grid_frame.grid(row=2, column=0, pady=10, sticky="news", padx=20)

        # Hacemos que la fila 2 del main_frame sea expansible
        self.main_frame.grid_rowconfigure(2, weight=1)
        self.grid_frame.grid_columnconfigure(0, weight=1)
        self.grid_frame.grid_rowconfigure(0, weight=1)

        # MODO OSCURO
        style = ttk.Style()
        style.theme_use("default")
        
        # Colores de las celdas
        style.configure("Treeview", 
                        background="#2b2b2b",
                        foreground="white",
                        rowheight=35,
                        fieldbackground="#2b2b2b",
                        borderwidth=0,
                        font=("Roboto", 12))
        
        # Color al seleccionar una fila (Azul CTk)
        style.map('Treeview', background=[('selected', '#1f538d')])
        
        # Colores de los encabezados
        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        font=("Roboto", 13, "bold"))
        style.map("Treeview.Heading", background=[('active', '#343638')]) # Hover

        # CREACIÓN DE LA TABLA
        columns = ("id", "name", "author")
        self.tree = ttk.Treeview(self.grid_frame, columns=columns, show="headings", selectmode="browse")

        # Configuramos los encabezados reales
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Título del Libro")
        self.tree.heading("author", text="Autor")

        # Ajustamos los anchos de las columnas
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("name", width=300, anchor="center")
        self.tree.column("author", width=200, anchor="center")

        self.tree.grid(row=0, column=0, sticky="news")

        self.scrollbar = ctk.CTkScrollbar(self.grid_frame, command=self.tree.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=self.scrollbar.set)


    def _build_search_order_frame(self):
        self.search_order_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.search_order_frame.grid(row=1, column=0, pady=10, sticky="ew", padx=20)

        self.lbl_search = ctk.CTkLabel(self.search_order_frame, text="ID del Libro:", font=self.font_base)
        self.lbl_search.grid(row=0, column=1)

        self.entry_search = ctk.CTkEntry(
            self.search_order_frame, 
            placeholder_text="Ej: 10", 
            width=70, 
            font=self.font_base
        )
        self.entry_search.grid(row=0, column=2)

        self.btn_search = ctk.CTkButton(
            self.search_order_frame, 
            text="Buscar", 
            font=self.font_base, 
            width=100,
            command=self.search_book_by_id
        )
        self.btn_search.grid(row=0, column=3)

        self.lbl_sort = ctk.CTkLabel(self.search_order_frame, text="Ordernar por:", font=self.font_base)
        self.lbl_sort.grid(row=0, column=4)

        self.combo_sort = ctk.CTkComboBox(
            self.search_order_frame, 
            values=["", "ID (inorden)", "Titulo", "Autor", "Preorden"],
            command=self.refresh_table
        )
        self.combo_sort.grid(row=0, column=5)


        for widget in self.search_order_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)


    def refresh_table(self, choice=None, books=None):        
        if books is None:
            books = self.order_table_by()
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        if books:
            for book in books:
                self.tree.insert("", "end", values=(book['book_id'], book['name'], book['author']))

    
    def refresh_history_table(self):
        for item in self.tree_history.get_children():
            self.tree_history.delete(item)
            
        actions = self.stack_root.get_all_actions()
        
        if actions:
            for action in actions:
                self.tree_history.insert("", "end", values=(action['action'], action['name']))

    
    def order_table_by(self) -> list | None:
        if self.entry_search.get() == "":
            books = self.avl_root.inorden()
            
            if not books:
                return None
            
            order_by = self.combo_sort.get().lower()

            if order_by == "autor":
                books.sort(key=lambda x: x['author'].lower())
            elif order_by == "titulo":
                books.sort(key=lambda x: x['name'].lower())
            elif order_by == "preorden":
                books = self.avl_root.preorden()
   
            return books
    

    def search_book_by_id(self):
        book_id_str = self.entry_search.get().strip()

        if not book_id_str:
            self.refresh_table()
            return
        
        try:
            book_id = int(book_id_str)
            book = self.avl_root.search(book_id)

            if book:
                self.refresh_table(books=[book])
            else:
                self.refresh_table(books=[])
                messagebox.showwarning("Libor no encontrado", f"El ID {book_id} no esta registrado")
        except ValueError:
            messagebox.showerror("Error ID", "ID invalido, intentalo otra vez")
            self.entry_search.delete(0, 'end')
            
    
    def open_insert_dialog(self):
        InsertBookDialog(self)

    
    def delete_book(self):
        selected_row = self.tree.selection()
        if not selected_row:
            messagebox.showwarning("Selecciona una fila", "Favor de seleccionar una fila primero")
            return

        row_data = self.tree.item(selected_row[0])['values']
        book_id = row_data[0]
        book_name = str(row_data[1])
        book_author = str(row_data[2])
        
        self.avl_root.delete(book_id)
        self.stack_root.push(
            ActionType.ACTION_DELETE,
            book_id,
            book_name,
            book_author
        )

        self.refresh_history_table()
        self.refresh_table()

        messagebox.showinfo("Libro Eliminado", f"Se elimino el libro {book_name}")


    def undo_last_action(self):
        if not self.stack_root.peek():
            messagebox.showinfo("Sin historial", "No hay historial de acciones")
            return
        

        confirm = messagebox.askyesno(
            "Confirmar Acción", 
            "¿Estás seguro de que deseas deshacer la última acción?"
        )
        
        if not confirm:
            return
        
        last_action = self.stack_root.pop()

        action = last_action['action'].lower()
        book_id = last_action['book_id']
        book_name = last_action['name']
        book_author = last_action['author']

        msg = ""
        if action  == 'insert':
            self.avl_root.delete(book_id)
            msg += "Se revirtió la inserción. Libro eliminado:\n\n"

        elif action == 'delete':
            self.avl_root.insert(book_id=book_id, book_name=book_name, book_author=book_author)
            msg += "Se revirtió la eliminación. Libro restaurado:\n\n"

        self.refresh_history_table()
        self.refresh_table()

        msg += f"- Libro: {book_name}\n- Autor: {book_author}"
        messagebox.showinfo("Rehacer Accion", message=msg)


    def show_tree_height(self):
        height = self.avl_root.height()
        messagebox.showinfo("Altura árbol", f"Altura del árbol: {height}")

    
    def delete_tree(self):
        if self.avl_root.height() == 0:
            messagebox.showwarning("Eliminar Árbol", "El árbol esta vacio.")
            return
        
        confirm = messagebox.askyesno(
            "Confirmar Acción", 
            "¿Estás seguro de que deseas ELIMINAR todo el ÁRBOL? Esta acción no se puede revertir."
        )
        
        if not confirm:
            return

        self.avl_root.delete_tree()
        messagebox.showinfo("Eliminar Árbol", "Se eliminó el árbol correctamente")
        self.refresh_table()

        self.empty_stack()
        self.refresh_history_table()
    

    def empty_stack(self):
        self.stack_root.empty_stack()

    
    def save_to_csv(self):
        if self.avl_root.save_to_csv() == 0:
            messagebox.showerror("Error", "Ocurrio un error al guardar el archivo")
            return
        messagebox.showinfo("Archivo guardado", "Archivo guardado correctamente.")
        

def run_gui_app(avl_root, stack_root):
    app = LibraryApp(avl_root, stack_root)
    app.mainloop()
