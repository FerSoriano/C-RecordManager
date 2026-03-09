from bindings.avl_tree import *

root = None

root = insertNode(root, createNode(1, "Test 1", "Fer Soriano"))
root = insertNode(root, createNode(2, "Test 2", "Fer Soriano"))
root = insertNode(root, createNode(3, "Test 3", "Fer Soriano"))

print("Connecting with C...\n")
print("Printing inorden:")
books = inorden_data(root)
for book in books:
    print(f"ID: {book["id"]} | Name: {book["name"]} | Author: {book["author"]}")


print("\nPrinting preorden:")
books = preorden_data(root)
for book in books:
    print(f"ID: {book["id"]} | Name: {book["name"]} | Author: {book["author"]}")
