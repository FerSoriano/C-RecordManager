
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../include/file_manager.h"


void writeNodeCSVPreorden(Node* root, FILE* file) {
    if (root == NULL) return;
    fprintf(file, "%d,%s,%s\n", root->id, root->name, root->author);
    writeNodeCSVPreorden(root->left, file);
    writeNodeCSVPreorden(root->right, file);
}


int saveTreeToCSV(Node* root, const char* filename) {
    if (root == NULL) return 0;

    FILE* file = fopen(filename, "w");
    if (file == NULL) return 0; // file error

    fprintf(file, "ID,Name,Author\n");

    writeNodeCSVPreorden(root, file);
    
    fclose(file);
    return 1;
}


Node* loadTreeFromCSV(Node* root, const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) return NULL;


    char buffer[1024];

    // skip headers
    fgets(buffer, sizeof(buffer), file);

    while(fgets(buffer, sizeof(buffer), file) != NULL) {
        char* str_id = strtok(buffer, ",");
        if (str_id == NULL) continue;
        int book_id = atoi(str_id);

        char* book_name = strtok(NULL, ",");
        char* book_author = strtok(NULL, "\n");

        if (book_name != NULL && book_author != NULL) {
            Node* node = createNode(book_id, book_name, book_author);
            root = insertNode(root, node);
        }
    }

    return root;
}
