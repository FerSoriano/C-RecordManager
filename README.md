# C-RecordManager: Optimized Library System

A high-performance, fully interactive Library Management System featuring a hybrid architecture. This project implements advanced data structures in **_C_** for a robust and memory-efficient backend, seamlessly integrated with a modern **_Python_** Graphical User Interface (GUI) using `ctypes`.

Developed as a Final Project for Data Structures and Algorithms (DSA) 2026.

## 🚀 Current Features

- **Backend (C):**
  - **AVL Tree:** O(log n) search, insertion, and deletion of library records. Auto-balancing architecture.
  - **History Stack (LIFO):** Custom stack implementation to track user actions for a robust "Undo" feature.
  - **Memory Safety:** Deep memory management using `strdup`, recursive post-order tree/stack destruction to prevent memory leaks and dangling pointers.
- **Frontend (Python):**
  - **Modern GUI:** Fully interactive Dark Mode interface built with `CustomTkinter`.
  - **Modular OOP Architecture:** Clean separation between UI Views, Python Models, and C Bindings.
  - **Real-time Sync:** Data grids and visual history stacks that react instantly to C backend operations via callbacks and shared libraries.

## 📂 Project Structure

The project follows a strict Separation of Concerns (SoC) principle, dividing the core C logic from the Python UI components:

    C-RecordManager/
    ├── core/                   # C Backend (Data Structures & Algorithms)
    │   ├── include/            # Header files (.h): avl_tree, history_stack
    │   └── src/                # Source files (.c): avl_tree, history_stack
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

### 1. Install Dependencies

Install the required Python libraries for the graphical interface:

    pip install -r requirements.txt

### 2. Compile the C Core

Compile all the C source files into a single shared library. You can use the provided Makefile:

    make compile-c

_Alternatively, you can compile manually by running:_ `gcc -shared -fPIC -o lib/libcore.so core/src/_.c`

_(**Note**: Ensure the `lib/` directory exists before running this command)._

### 3. Run the Application

Once the `libcore.so` file is generated inside the `lib/` directory, start the Python application:

    python3 gui/app.py

## 🔜 Upcoming Features (WIP)

- **Data Persistence:** Reading and writing the AVL tree data to a local `.json` or `.txt` file for permanent storage across sessions.
