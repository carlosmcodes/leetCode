#include "bTree.h"
#define INT_MAX  (2147483647)
#define INT_MIN  (-2147483647)
#include <ctype.h>
int main(){
    printf("Playground for Strings.\n---------------------\n");
    stringPlayground();
}
// char  *ss = "hellllo";
// ^^^^^^ THIS DOES NOT WORK ^^^^^^

/*
 * @funx: declutter main
 */
void stringPlayground(){
    int p[10]= {1,1,1,3,3,4,3,2,4,2};
    int p2[6]= {1, 3, 6, 4, 1, 2};
    // intersect(p,9,p2,4,p2);
    // char s[100] = "";
    // printstr(ab(s, 39), 100);
    // int d[11] = {1,3,2,1,2,1,5,3,3,4,2};
    // horizontalStrokes(d, 11);
    maxValue5(268);
}
int maxValue5(int N){
    int val = 0;
    int l = 1;
    int n = N;
    int sum = 0;
    int i = 0;
    // for(; N != 0; N/=10, l++)
    // // pr(l);
    for(; n != 0; n/=10, i++){
        val = 0 * 10 + n % 10;
        if ( i != 0)
            val = (10 * i) * val;
        // pr(val);
    }
    return 0;
}

int horizontalStrokes(int *A, int N){
  if (!A) return 0;
    int counter = 1;
    for(int i = 0, j = 1; j < N -1; j++, i++){
        if (A[i] > A[j])
            counter++;
        else if (A[i] < A[j])
            counter++;
    }


    if (counter > 1000000000) return -1;
    return counter;
}
char *ab(char *message, int K){
    if (!message) return "";
    int len = listSize(message);
    char res[len];
    char *resPtr = res;
    for (int i = 0; i < len; i++){
        if (i >= K){
            if (message[i] == ' '){
                return resPtr;
            }
            else
            {
                while(i <= len){
                res[i] = message[i];
                    i++;
                }
            }
            
        }
        res[i] = message[i];
    }
    return resPtr;
}

int smallestInt(int *A, int N){
    int smallest = 1;
    int temp = 0;
    int low = 0;
    qsort(A, N, sizeof(int), cmpfunc);
    for (int i = 0; i < N; i++){
        temp = A[i];
        low = A[i];
        low--;
        temp++;
        low = temp < smallest ? temp : low;
    }
    return smallest;
}

int firstUniqChar(char * s){

}
/*
 * @param: integer value to be reversed
 * @return: reversed integer value
 */
int reverse(int x){
    // long long is for overflow purposes
    long long val = 0;
    for(; x != 0; x/=10)
        val = val * 10 + x % 10;
	return (val > INT_MAX || val < INT_MIN) ? 0 : val;
}


/*
 * @param: string array
 * @param: size of array
 */
void reverseString(char* s, int sSize){
    char temp;
    for (int i = 0,j=sSize-1; i <= j; i++, j--){
        temp = s[j];
        s[j] = s[i];
        s[i] = temp;
    }
}
/*
 * @param: int array to be passed in
 * @param: size of array
 * @param: target x to hit
 * @param: return size of new array
 * incomplete
 * 
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    // [2, 7, 11, 15]
    // if: target - i = i+1
    int *newb = malloc((*returnSize) * sizeof(int));
    for (int i = 0; i < numsSize; i++){
        if (target - nums[i] == nums[i+1]){
            newb[i] = i;
            newb[i+1] = i+1;
        }
    }
    return newb;
}

/*
 * @param: int array
 * @param: size of array
 * fx: move all zeroes to the right. keep ordering the same
 */
void moveZeroes(int* nums, int numsSize){
    /*
     * 2 cases:
     * 1 starts at zero
     * 1 starts at non-zero 
     */
    for(int i = 0, j = 0; i < numsSize; i++) {
        if(nums[j]){
            j++;
        }
     else if (nums[i] != 0) {
        nums[j] = nums[i];
        nums[i] = 0;
        j++;
    }
}
}

/*
 * @param: array 
 * @param: size of array
 * @param: size of array to be returned
 * @return: array with newly added int 
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){
    int* size =  malloc((*returnSize) * sizeof(int));
    int ten = 1;
    for(int i = 0; i < digitsSize-1; i++) ten*=10;
    ++digits[(digitsSize -1)];
    int sum = 0;
    for(int i = 0; i < digitsSize; i++){
        size[i] = digits[i];
    }
    return size;
}

/*
 * @param: array #1
 * @param: size of array1
 * @param: array #2
 * @param: size of array2
 * @param: return size of new array
 * @return: intersection of two arrays => pointer to array
 */
int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    puts("intersect."), nl();
    qsort(nums1, nums1Size, sizeof(int), cmpfunc);
    printint(nums1, nums1Size);
    qsort(nums2, nums2Size, sizeof(int), cmpfunc);
    int i = 0, j = 0;
    *returnSize = 0;
    int max = nums1Size > nums2Size ? nums1Size : nums2Size;
    int *res =  malloc(max * sizeof(int));
    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] == nums2[j]) {
            // assign nums1[i] to res[returnsize], then  increment returnsize @ *x
            res[(*returnSize)++] = nums1[i];
            ++i;
            ++j;
        } 
        else if (nums1[i] < nums2[j]) 
            ++i;
        else 
            ++j;
    }
    return res;
}

/*
 * @param: element a to check 
 * @param: element b to check
 * @return: needed for qsort fx 
 * 
 * Return x meaning
 * <0 The element pointed by p1 goes before the element pointed by p2
 * 0  The element pointed by p1 is equivalent to the element pointed by p2
 * >0 The element pointed by p1 goes after the element pointed by p2
 */
int cmpfunc (const void * a, const void * b) {
// non-reverse order
   return ( *(int*)a - *(int*)b );

// reverse order
//    return ( *(int*)b - *(int*)a );
}

/*
 * @param: array of int's
 * @param: size of array
 * @return: number that does NOT appear twice
 */
int singleNumber(int* nums, int numsSize){
    int binaryFlip = 0;
    for (int i = 0; i< numsSize; i++)
    binaryFlip^=nums[i];
    return binaryFlip;
}

/*
 *
 * @param: array to search for
 * @param: size of array
 * @return: length of current array that does not have dup's
 */
int removeDuplicates(int* nums, int numsSize){
    if (numsSize == 0) return 0;
    int i = 0;
    for (int j = 1; j < numsSize; j++){
        if (nums[j] != nums[i]){
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}


/*
 * @param: int array to be searched
 * @param: size of array
 * @return: t/f statement
 */
bool containsDuplicate(int* nums, int numsSize){
    qsort(nums,numsSize, sizeof(int), cmpfunc);
    for (int i =0; i < numsSize-1; i++){
        if (nums[i] == nums[i+1]) return true;
    }
    return false;
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

void printint(int *s, int size){
    for (int i = 0; i < size; i++)
        printf("%d", s[i]);
    nl();
}

void printstr(char *s, int size){
    for (int i = 0; i < size; i++)
        printf("%c", s[i]);
    nl();
}