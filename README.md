# C-RecordManager: Optimized Library System

A high-performance, fully interactive Library Management System featuring a hybrid architecture. This project implements advanced data structures in **_C_** for a robust and memory-efficient backend, seamlessly integrated with a modern **_Python_** Graphical User Interface (GUI) using `ctypes`.

Developed as a Final Project for Data Structures and Algorithms (DSA) 2026.

## 🚀 Current Features

- **Backend (C):**
  - **AVL Tree:** O(log n) search, insertion, and deletion of library records. Auto-balancing architecture.
  - **Data Persistence (CSV):** Low-level file I/O operations using `<stdio.h>` and `strtok` to serialize (via Pre-order traversal) and deserialize the AVL tree to/from a local `.csv` file.
  - **History Stack (LIFO):** Custom stack implementation to track user actions for a robust "Undo" feature.
  - **Memory Safety:** Deep memory management using `strdup` and recursive post-order tree/stack destruction to prevent memory leaks and dangling pointers.
- **Frontend (Python):**
  - **Modern GUI:** Fully interactive Dark Mode interface built with `CustomTkinter`, featuring semantic color coding for safe and destructive actions.
  - **Modular OOP Architecture:** Clean separation between UI Views, Python Models, and C Bindings.
  - **Real-time Sync:** Data grids and visual history stacks that react instantly to C backend operations via callbacks and shared libraries.

## 📂 Project Structure

The project follows a strict Separation of Concerns (SoC) principle, dividing the core C logic from the Python UI components and the database state:

    C-RecordManager/
    ├── core/                   # C Backend (Data Structures & Algorithms)
    │   ├── include/            # Header files (.h): avl_tree, history_stack, file_manager
    │   └── src/                # Source files (.c): avl_tree, history_stack, file_manager
    ├── data/                   # Local database storage (books.csv)
    ├── gui/                    # Python Frontend (UI & Integration)
    │   ├── bindings/           # ctypes wrappers and C-to-Python translations
    │   ├── models/             # Python OOP abstractions (avl.py, stack.py)
    │   ├── views/              # CustomTkinter GUI components & dialogs
    │   └── app.py              # Main entry point for the Python application
    ├── lib/                    # Compiled shared libraries (.so / .dll)
    ├── Makefile                # Automated build instructions
    └── requirements.txt        # Python dependencies (CustomTkinter)

## 🛠️ Build and Run Instructions

To run this project locally, you need a C compiler (`gcc` or `clang`) and Python 3 installed on your system.

### 1. Clone the Repository

Start by cloning this repository to your local machine and navigating into the project folder:

    git clone https://github.com/FerSoriano/C-RecordManager.git
    cd C-RecordManager

### 2. Set Up a Virtual Environment (Recommended)

It is highly recommended to use a Python virtual environment to manage dependencies and avoid conflicts:

    python3 -m venv .venv

Activate the virtual environment:

- **macOS / Linux:** `source .venv/bin/activate`
- **Windows:** `.venv\Scripts\activate`

### 3. Install Dependencies

With your virtual environment activated, install the required Python libraries for the graphical interface:

    pip install -r requirements.txt

### 4. Compile the C Core

Compile all the C source files into a single shared library. You can use the provided Makefile:

    make compile-c

_Alternatively, you can compile manually by running:_ `gcc -shared -fPIC -o lib/libcore.so core/src/*.c`

_(**Note**: Ensure the `lib/` directory exists before running this command)._

### 5. Run the Application

Once the `libcore.so` file is generated inside the `lib/` directory, start the Python application:

    python3 gui/app.py
