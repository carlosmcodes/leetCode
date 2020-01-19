#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
/*
bst can have at most 2 children!!
        54
       / \
      51    99
     /  \   / \
    1   52 59  101
     \12   
*/
     
/* typedef w name @ bottom prevents from calling struct everytime
 bTree after struct is 'tagname', bTree in last line is type.
 => therefore youre calling typdef on a type. that type being bTree
 */

typedef struct bTree
{
    int val;
    struct bTree *left;
    struct bTree *right;
} bTree;

void btreePlayground();
void stringPlayground();
int listSize(char *s);
void printItems_inCharList(char *s);
void pr(int v);
void nl();
void preOrder(bTree *n);
void inOrder(bTree *n);
void postOrder(bTree *n);
bTree *insertNode(bTree *node, int value);
bTree *createNode(int val);
bool exists(bTree *root,int value);

