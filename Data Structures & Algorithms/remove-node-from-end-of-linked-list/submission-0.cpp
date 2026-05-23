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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head->next == NULL){
            head = NULL;
            return head;
        }

        ListNode* temp = head;
        int total_nodes = 0;
        while(temp!= NULL){
            total_nodes++;
            temp = temp->next;
        }

        int fromstart = total_nodes - n + 1;
        ListNode* current = head;
        ListNode* prev = NULL;
        ListNode* front = head->next;
        while (fromstart > 0) {
            fromstart--;
            if(fromstart == 0 && prev == NULL){
                current->next = NULL;
                return front;
            }

            if(fromstart == 0){
                prev->next = front;
                current->next = NULL;
                return head;
            }

            prev = current;
            current = front;
            front = front->next;
        }

        
    }
};
