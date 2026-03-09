#ifndef ALV_TREE_H
#define AVL_TREE_H

typedef void (*Callback)(int id, const char* name, const char* author);

typedef struct Node{
    int id;
    char* name;
    char* author;
    int height;
    struct Node* left;
    struct Node* right;
} Node;


Node* createNode(int id, char* name, char* author);
Node* insertNode(Node* root, Node* n);

int getHeight(Node* n);

void inorden(Node* root, Callback callback);
void preorden(Node* root, Callback callback);

// helpers
static void setHeight(Node** n);
static int max(int a, int b);
static Node* leftRotation(Node* n);
static Node* rightRotation(Node* n);

#endif