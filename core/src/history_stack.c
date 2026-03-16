
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "../include/history_stack.h"


StackNode* push(StackNode* s, ActionType action, const int book_id, const char* name, const char* author) {
    StackNode* top = (StackNode*)malloc(sizeof(StackNode));

    top->action = action;
    top->book_id = book_id;
    top->name = (name != NULL) ? strdup(name) : NULL;
    top->author = (author != NULL) ? strdup(author) : NULL;

    top->next = s;

    return top;
}


void pop(StackNode** s, Callback callback) {
    if (isEmpty(*s)) return;

    StackNode* tmp = *s;

    callback(getAction(tmp), tmp->book_id, tmp->name, tmp->author);

    *s = tmp->next;   

    free(tmp->name);
    free(tmp->author);
    free(tmp);
}


void peek(StackNode* s, Callback callback) {
    if (isEmpty(s)) return;
    callback(getAction(s), s->book_id, s->name, s->author);
}


void showStack(StackNode* s, Callback callback) {
    if (isEmpty(s)) return;
    callback(getAction(s), s->book_id, s->name, s->author);
    showStack(s->next, callback);
}


StackNode* emptyStack(StackNode* s) {
    if (isEmpty(s)) return NULL;
    emptyStack(s->next);
    free(s->name);
    free(s->author);
    free(s);
    return NULL;
}


// helpers
static bool isEmpty(StackNode* s) {
    return s == NULL;
}


static const char* getAction(StackNode* s) {
    if (isEmpty(s)) return NULL;
    return (s->action == ACTION_DELETE) ? "Delete" : "Insert";
}