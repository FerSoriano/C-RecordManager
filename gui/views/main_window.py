import platform
import customtkinter as ctk


class LibraryApp(ctk.CTk):
    def __init__(self, avl_root, stack_root):
        super().__init__()
        if platform.system() == "Linux":
            ctk.set_widget_scaling(1.5)
            ctk.set_window_scaling(1.5)

        self.avl_root = avl_root
        self.stack_root = stack_root

        self.title("C-RecordManager: Library System")
        self.geometry("900x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Main Layout principal (Grid: 2 cols, 1 row)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        font_base = ctk.CTkFont(family="Roboto", size=14)
        font_title = ctk.CTkFont(family="Roboto", size=20, weight="bold")


        # Left pane - btns
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Library Manager", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.btn_insert = ctk.CTkButton(self.sidebar_frame, text="Insertar Libro", font=font_base)
        self.btn_insert.grid(row=1, column=0, padx=20, pady=10)

        self.btn_search = ctk.CTkButton(self.sidebar_frame, text="Buscar Libro", font=font_base)
        self.btn_search.grid(row=2, column=0, padx=20, pady=10)
        
        self.btn_delete = ctk.CTkButton(self.sidebar_frame, text="Eliminar Libro", font=font_base)
        self.btn_delete.grid(row=3, column=0, padx=20, pady=10)

        self.btn_undo = ctk.CTkButton(self.sidebar_frame, text="Deshacer (Undo)", fg_color="transparent", 
                                      border_width=2, text_color=("gray10", "#DCE4EE"), font=font_base)
        self.btn_undo.grid(row=4, column=0, padx=20, pady=10)

        # Right pane - dashboard
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # todo: add treeview
        self.title_label = ctk.CTkLabel(self.main_frame, text="Catálogo de Libros (AVL)", 
                                        font=font_title)
                                        # font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=20)


def run_gui_app(avl_root, stack_root):
    app = LibraryApp(avl_root, stack_root)
    app.mainloop()
