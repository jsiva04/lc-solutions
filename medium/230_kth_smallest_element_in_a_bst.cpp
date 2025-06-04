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
class Solution
{
public:
    void helper(TreeNode *root, vector<int> &tree)
    {
        if (root == NULL)
            return;

        tree.push_back(root->val);
        helper(root->left, tree);
        helper(root->right, tree);
    }

    int kthSmallest(TreeNode *root, int k)
    {
        vector<int> tree;
        helper(root, tree);
        std::sort(tree.begin(), tree.end());

        return (tree[k - 1]);
    }
};