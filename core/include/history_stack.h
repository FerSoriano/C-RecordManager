#ifndef HISTORY_STACK_H
#define HISTORY_STACK_H

typedef void (*Callback)(const char* action, int id, const char* name, const char* author);

typedef enum {
    ACTION_INSERT,
    ACTION_DELETE
} ActionType;


typedef struct StackNode {
    ActionType action;
    int book_id;
    char* name;
    char* author;
    struct StackNode* next;
} StackNode;


StackNode* push(StackNode* s, ActionType action, const int id, const char* name, const char* author);
void pop(StackNode** s, Callback callback);
void peek(StackNode* s, Callback callback);
void showStack(StackNode* s, Callback callback);
StackNode* emptyStack(StackNode* s);

// helpers
static bool isEmpty(StackNode* s);
static const char* getAction(StackNode* s);


#endif


// Gran Salon 1
// SPX055