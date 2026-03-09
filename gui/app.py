from bindings.avl_tree import *

print("Connecting with C...\n")

root = None

root = insertNode(root, createNode(1, "Test", "Fer Soriano"))
root = insertNode(root, createNode(2, "Test", "Fer Soriano"))
root = insertNode(root, createNode(3, "Test", "Fer Soriano"))
root = insertNode(root, createNode(4, "Test", "Fer Soriano"))
root = insertNode(root, createNode(5, "Test", "Fer Soriano"))
root = insertNode(root, createNode(6, "Test", "Fer Soriano"))
root = insertNode(root, createNode(7, "Test", "Fer Soriano"))
root = insertNode(root, createNode(8, "Test", "Fer Soriano"))


height = getRootHeight(root)
print(f"Tree height: {height}")


print("\nPrinting inorden:")
books = inorden_data(root)
for book in books:
    print(f"ID: {book["id"]} | Name: {book["name"]} | Author: {book["author"]}")


print("\nPrinting preorden:")
books = preorden_data(root)
for book in books:
    print(f"ID: {book["id"]} | Name: {book["name"]} | Author: {book["author"]}")
