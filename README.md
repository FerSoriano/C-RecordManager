# C-RecordManager: Optimized Library System

A high-performance Library Management System featuring a hybrid architecture. This project implements advanced data structures in **C** for a robust and efficient backend, seamlessly integrated with a **Python** frontend using `ctypes`.

Developed as a Final Project for Data Structures and Algorithms (DSA).

## 🚀 Current Features

- **Backend (C):** Implementation of an AVL Tree for O(log n) search, insertion, and deletion of library records.
- **Frontend (Python):** Modular architecture handling user inputs and displaying data retrieved from the C backend via callbacks.
- **Memory Management:** Dynamic memory allocation with deep copies (`strdup`) and proper memory freeing to prevent leaks.
- **Integration:** Direct C-to-Python communication via shared libraries (`.so`).

## 📂 Project Structure

The project follows a strict Separation of Concerns (SoC) principle, dividing the core logic from the user interface:

    C-RecordManager/
    ├── core/                   # C Backend (Data Structures & Algorithms)
    │   ├── include/            # Header files (.h) defining structs and public APIs
    │   └── src/                # Source files (.c) containing the core logic
    ├── gui/                    # Python Frontend (UI & Integration)
    │   ├── bindings/           # ctypes wrappers and C-to-Python translations
    │   ├── views/              # Console menus (and future GUI components)
    │   └── app.py              # Main entry point for the Python application
    └── lib/                    # Compiled shared libraries (.so / .dll)

## 🛠️ Build and Run Instructions

To run this project locally, you need a C compiler (`gcc` or `clang`) and Python 3 installed on your system.

### 1. Compile the C Core

First, compile all the C source files into a single shared library. Open your terminal in the root directory of the project and run:

    gcc -shared -fPIC -o lib/libcore.so core/src/*.c

_(Note: Ensure the `lib/` directory exists before running this command)._

### 2. Run the Application

Once the `libcore.so` file is generated, you can start the Python application:

    python3 gui/app.py

## 🔜 Upcoming Features (WIP)

- **Action History (Undo):** Implementation of a Stack (LIFO) data structure in C to keep track of inserted and deleted records.
- **Graphical User Interface (GUI):** Migration from the current console view to a fully interactive GUI using `CustomTkinter`.
- **Data Persistence:** Reading and writing the AVL tree data to a local file for permanent storage.
