/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:


    ListNode* final;
    void gethead(ListNode* current, ListNode* ahead, ListNode* head){
        ListNode* second;
        if(current == head){
            current->next = NULL;
        }

        if(ahead->next == NULL){
            ahead->next = current;
            final = ahead;
            return;
        }

        second = ahead->next;
        ahead->next = current;

        gethead(ahead, second, head);
        
    }

    ListNode* reverseList(ListNode* head) {
    
    

    if(head == NULL){
        return NULL;
    }

    if(head->next == NULL){
        return head;
    }

    
    gethead(head, head->next, head);
    return final;
    
        
    }
};
