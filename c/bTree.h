#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
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

void nl(){puts("");};
/*
 * @param: value to print, has to be int
 */
void pr(int v){printf("%d\n", v);};
// ------------STRINGS--------------- //
void stringPlayground();
int listSize(char *s);
void printItems_inCharList(char *s);
int removeDuplicates(int* nums, int numsSize);
bool containsDuplicate(int* nums, int numsSize);
int cmpfunc (const void * a, const void * b);
int singleNumber(int* nums, int numsSize);
int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize);
void printint(int *s, int size);
int* plusOne(int* digits, int digitsSize, int* returnSize);
void moveZeroes(int* nums, int numsSize);
int* twoSum(int* nums, int numsSize, int target, int* returnSize);
void reverseString(char* s, int sSize);
void printstr(char *s, int size);
int reverse(int x);
int firstUniqChar(char * s);
int smallestInt(int *A, int N);
char *ab(char *message, int K);
int horizontalStrokes(int *A, int N);
int maxValue5(int N);
// -------------BINARY TREE--------------- //
void btreePlayground();
void preOrder(bTree *n);
void inOrder(bTree *n);
void postOrder(bTree *n);
bTree *insertNode(bTree *node, int value);
bTree *createNode(int val);
bool exists(bTree *root,int value);
int maxDepth(bTree *root);
int max(int a, int b);
int nodeCount(bTree *root);
int maxVal(bTree *root);
int minVal(bTree *root);
bTree *deserialize(char *s);
char *serialize(bTree *root);

