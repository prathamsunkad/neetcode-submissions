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
    TreeNode* invertTree(TreeNode* root) {
        queue<TreeNode*> q;
        vector<vector<TreeNode*>> v;
        if(root == NULL){
            return root;
        }

        if(root->left == NULL && root->right == NULL){
            return root;
        }
        q.push(root);
        while(!q.empty()){
            TreeNode* temp = q.front();
            q.pop();
            if(temp->left == NULL and temp->right == NULL){
                continue;
            }

            if(temp->left == NULL and temp->right!=NULL){
                q.push(temp->right);
                temp->left = temp->right;
                temp->right = NULL;
                continue;
            }

            
            if(temp->left != NULL and temp->right==NULL){
                q.push(temp->left);
                temp->right = temp->left;
                temp->left = NULL;
                continue;
            }
            
            TreeNode* exchange = temp->left;
            temp->left = temp->right;
            temp->right = exchange;
            q.push(temp->left);
            q.push(temp->right);
        }

        return root; 
        
    }
};
