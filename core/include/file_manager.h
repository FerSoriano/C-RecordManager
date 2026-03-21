#ifndef FILE_MANAGER
#define FILE_MANAGER

#include "avl_tree.h"

int saveTreeToCSV(Node* root, const char* filename);
Node* loadTreeFromCSV(Node* root, const char* filename);

#endif