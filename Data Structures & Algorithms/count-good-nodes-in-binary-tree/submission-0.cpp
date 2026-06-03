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
    int count_nodes(TreeNode* root, int greatest){
        if(root == NULL){
            return 0;
        }

        if(root->val >= greatest){
            return 1 + count_nodes(root->left, root->val) + count_nodes(root->right, root->val);

        }

        if(root->val < greatest){
            return 0 + count_nodes(root->left, greatest) + count_nodes(root->right, greatest);

        }


    }
    int goodNodes(TreeNode* root) {
        int total_count = count_nodes(root, root->val);
        
        return total_count;
    }
};
