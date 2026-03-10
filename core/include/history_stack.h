#ifndef HISTORY_STACK_H
#define HISTORY_STACK_H

typedef enum {
    ACTION_INSERT,
    ACTION_DELETE
} ActionType;


typedef struct StackNode {
    ActionType action;
    int id;
    char* name;
    char* author;
    StackNode* next;
} StackNode;

StackNode* push(StackNode* top, ActionType action, const int id, const char* name, const char* author);
StackNode* pop(StackNode** top);

void showStack(StackNode* top);
bool isEmpty(StackNode* top);

#endif