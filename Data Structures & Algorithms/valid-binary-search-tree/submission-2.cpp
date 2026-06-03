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
    int max_val(TreeNode* root){
        if(root->left == NULL && root->right == NULL){
            return root->val;
        }

        if(root->left == NULL && root->right != NULL){
            return max(root->val, max_val(root->right));
        }

        if(root->right == NULL && root->left != NULL){
            return max(root->val, max_val(root->left));
        }

        else{
            return max({root->val, max_val(root->left), max_val(root->right)});
        }


    }


    int min_val(TreeNode* root){
        if(root->left == NULL && root->right == NULL){
            return root->val;
        }

        if(root->left == NULL && root->right != NULL){
            return min(root->val, min_val(root->right));
        }

        if(root->right == NULL && root->left != NULL){
            return min(root->val, min_val(root->left));
        }

        else{
            return min({root->val, min_val(root->left), min_val(root->right)});
        }


    }

    bool isValidBST(TreeNode* root) {

        if(root->left == NULL && root->right == NULL){
            return true;
        }

        if(root->left != NULL && root->right == NULL){
            if(root->val > max_val(root->left)){
            return true && isValidBST(root->left);
        }

        else return false;

        }


        if(root->left == NULL && root->right != NULL){
            if(root->val < min_val(root->right)){
            return true && isValidBST(root->right);
        }
            else return false;
        }

        if(root->left != NULL && root->right != NULL) {
        if(root->val > max_val(root->left) && root->val < min_val(root->right)){
            return true && isValidBST(root->left) && isValidBST(root->right);
        }
        else return false;
        }

    

        
    }
};
