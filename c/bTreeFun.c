#include "bTree.h"

int main(){
    puts("main.");
    btreePlayground();
   
}

char *serialize(bTree *root){
    char s[500];
    char *str = &s;
    if (!root)
        str = "#";
    else{
        
    }
    
}

bTree *deserialize(char *s){

}

/*
 * @param: root of tree
 * @return: node of min val
 */
int minVal(bTree *root){
    bTree *tempPtr = root;
    while (tempPtr->left) 
        tempPtr = tempPtr->left;
    return tempPtr->val;
}

/*
 * @param: root of tree
 * @return: node of max val
 */
int maxVal(bTree *root){
    bTree *temp = root;
    while (temp->right)
        temp = temp->right;
    return temp->val;
}

/*
 * @param: head of tree 
 * @return: number of nodes in tree ( not including root!!)
 */
int nodeCount(bTree *root){
    if (!root) return 0;
    return nodeCount(root->right) + nodeCount(root->left) + 1;
}

/*
 * @param: root node of tree
 * @return: size of depth
 */
int maxDepth(bTree *root){
    if (!root) return 0;
        int maxL = maxDepth(root->left);
        int maxR = maxDepth(root->right);
    return max(maxL, maxR)+1;
        
}

/*
 * @param: two int values
 * @return: max of the two values
 */
int max(int a, int b){
    return (a >= b) ? a : b;
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
            // printf("i: %d | %d\n",i, rando);
            insertNode(root, rando);
        } 
    }
    // puts("preorder:");
    // preOrder(root);
    // nl();
    // puts("inorder:");
    // inOrder(root);
    // nl();
    // puts("postorder:");
    // postOrder(root);
    // nl();
    // printf("maxdepth: ");
    // pr(maxDepth(root));
    // pr(nodeCount(root));
    // pr(minVal(root));
    // pr(maxVal(root));    
}

/*
 * @param: checks if value is in tree
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