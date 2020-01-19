#include "bTree.h"

int main(){
    puts("main.");
}

/*
 * @funx: declutter main
 */
void btreePlayground(){
    bTree *root = NULL;
    root = insertNode(root,46);
    int i;
    for (i = 0; i< 23; i++) {
        int rando = rand() % 128;
        if (!exists(root,rando)){
            printf("%d\n", rando);
            insertNode(root, rando);
        } 
    }
    puts("preorder:");
    preOrder(root);
    nl();
    puts("inorder:");
    inOrder(root);
    nl();
    puts("postorder:");
    postOrder(root);
    nl();
}

/*
 * @funx: declutter main
 */
void stringPlayground(){
    char *v = "balogne";
    printItems_inCharList(v);
    printf("size of v is: %d", listSize(v));
    nl();
}

/*
 * @param: char pointer to be checked
 * @return: size of char array using recursion
 */
int listSize(char *s){
    if(*s == '\0') return *s;
    return listSize(++s) + 1; 
}

/*
 * @param: char pointer to be printed
 */
void printItems_inCharList(char *s){
    char *char_ptr;
    for (char_ptr = s; *char_ptr != '\0'; char_ptr++)
        printf("%c", *char_ptr);
    nl();
}

/*
 * @param: value to be checked in tree
 * @return: t/f 
 */
bool exists(bTree *root,int value){
    if (!root) return false;
    else {
        if (root->val == value)
        return true;
        return (value > root->val) ? exists(root->right, value) : exists(root->left, value);
    }
}

/*
 * @param: value to be printed. has to be int
*/
void pr(int v){
    printf("%d ", v);
}

/*
 * lazy i am, admit i will 
*/
void nl() {puts("");}

/*
 * @param: value to be created
 * @return: a pointer to the new node
*/
bTree *createNode(int val){
    bTree *newBoo = (bTree*)malloc(sizeof(bTree));
    newBoo->val = val;
    newBoo->left = NULL;
    newBoo->right = NULL;
    return newBoo;
}
/*
 * n, l, r
 * @param: root of tree
*/
void preOrder(bTree *n){
    if (!n) return;
    else {
        pr(n->val);
        preOrder(n->left);
        preOrder(n->right);
    }
}
/*
 * l, n , r
 * @param: root of tree
*/
void inOrder(bTree *n){
    if (!n) return;
    else
    {
        inOrder(n->left);
        pr(n->val);
        inOrder(n->right);
    }
}
/*
 * l, r, n
 * @param: root of tree
*/
void postOrder(bTree *n){
    if (!n) return;
    else
    {
        postOrder(n->left);
        postOrder(n->right);
        pr(n->val);
    }
}

/*
 * @param: pointer of tree(usually root), value to be inserted
 * @return: pointer to root tree with value included
 */
bTree *insertNode(bTree *node, int value){
    if(!node) return createNode(value);
    if(value > node->val)
        node->right = insertNode(node->right, value);
    else
        node->left = insertNode(node->left, value);
    return node;
}