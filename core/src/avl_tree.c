
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/avl_tree.h"

Node* createNode(int id, char* name, char* author) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->id = id;
    node->name = strdup(name); // string duplicate
    node->author = strdup(author); // string duplicate
    node->height = 1;
    node->left = NULL;
    node->right = NULL;
    return node;
}

Node* insertNode(Node* root, Node* n) {
    if (root == NULL) {
        return n;
    }

    if (n->id < root->id) {
        root->left = insertNode(root->left, n);
    } else if (n->id > root->id) {
        root->right = insertNode(root->right, n);
    } else {
        return root;
    }

    setHeight(&root);

    int balanceFactor = getHeight(root->left) - getHeight(root->right);

    if (balanceFactor < -1) {
        Node* tmp = root->right;
        if (getHeight(tmp->left) - getHeight(tmp->right) > 0) {
            root->right = rightRotation(tmp); // double rotation
        }
        return leftRotation(root);
    }
    if (balanceFactor > 1){
        Node* tmp = root->left;
        if (getHeight(tmp->left) - getHeight(tmp->right) < 0) {
            root->left = leftRotation(tmp); // double rotation
        }
        return rightRotation(root);
    }


    return root;
}

static void setHeight(Node** n) {
    if (n == NULL) return;
    (*n)->height = max(getHeight((*n)->left), getHeight((*n)->right)) + 1;
}

int getHeight(Node* n) {
    if (n == NULL) return 0;
    return n->height;
}

static int max(int a, int b) {
    return (a > b) ? a : b;
}

static Node* leftRotation(Node* n) {
    Node* tmp = n->right;
    Node* tmp2 = tmp->left;

    tmp->left = n;
    n->right = tmp2;

    setHeight(&n);
    setHeight(&tmp);

    return tmp;
}

static Node* rightRotation(Node* n) {
    Node* tmp = n->left;
    Node* tmp2 = tmp->right;

    tmp->right = n;
    n->left = tmp2;

    setHeight(&n);
    setHeight(&tmp);

    return tmp;
}

void preorden(Node* root, Callback callback) {
    if (root == NULL) return;
    // printf("[id: %d] - %s by %s | H:[%d]\n", root->id, root->name, root->author, root->height);
    callback(root->id, root->name, root->author);
    preorden(root->left, callback);
    preorden(root->right, callback);
}

void inorden(Node* root, Callback callback) {
    if (root == NULL) return;
    inorden(root->left, callback);
    // printf("[id: %d] - %s by %s | H:[%d]\n", root->id, root->name, root->author, root->height);
    callback(root->id, root->name, root->author);
    inorden(root->right, callback);
}