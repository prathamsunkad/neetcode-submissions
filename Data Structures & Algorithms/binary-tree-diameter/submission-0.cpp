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
    int max_val = 0;
    int trial(TreeNode* root){
        if(root == NULL){
            return 0;
        }

        int current_node = trial(root->left) + trial(root->right);
        int carried_val = max(trial(root->left) ,trial(root->right));

        if(current_node>max_val){
            max_val = current_node;
        }

        return 1+carried_val;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        trial(root);
        return max_val;
    }
};
