#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <map>
#include <set>
#include <cmath>
#include "listNode.cpp"
using namespace std;
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2);

class linkedList{
    public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode preHead(0), *p = &preHead;
    int extra = 0;
    while (l1 || l2 || extra) {
        if (l1) {
        extra += l1->val;
        l1 = l1->next;
        }
        if (l2) extra += l2->val, l2 = l2->next;
        p->next = new ListNode(extra % 10);
        extra /= 10;
        p = p->next;
    }
    return preHead.next;
    }
};
    int main(){
        ListNode l1 = ListNode(1);
        ListNode l2 = ListNode(2);
        ListNode l3 = ListNode(3);
        ListNode *lp = &l1;
        ListNode *lp2 = lp;
        
    return 0;
    }