/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        TreeNode* temp = root;
        queue<TreeNode*> q; 
        vector<int> final;
        if(root == NULL){
            /*final.push_back(root->val);*/
         return final;}

        if(root->left == NULL && root->right == NULL){
            final.push_back(root->val);
            return final;
        }

        q.push(temp);
        while(!q.empty()){
            TreeNode* top = q.front();
            if(top==NULL){
                continue;
            }
            queue<TreeNode*> tempq;
            if(top!=NULL){
                
                final.push_back(top->val);
                while(!q.empty()){
                    TreeNode* node = q.front();
                    q.pop();
                    if(node->right !=NULL){
                    tempq.push(node->right);}

                    if(node->left!=NULL){
                    tempq.push(node->left);}
                }

                while(!tempq.empty()){
                    TreeNode* node2 = tempq.front();
                    tempq.pop();
                    q.push(node2);
                }

                
            }
            
            continue;

        }

        return final;
        
    }
};
