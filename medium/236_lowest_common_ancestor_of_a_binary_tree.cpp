/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution
{
public:
    bool checkExists(TreeNode *root, TreeNode *p)
    {
        if (root == NULL)
            return false;
        if (!root->left && !root->right && root != p)
            return false;
        if (root == p)
            return true;

        return (checkExists(root->left, p) || checkExists(root->right, p));
    }

    void makeList(TreeNode *root, vector<TreeNode *> &list, TreeNode *p, TreeNode *q)
    {
        if (root == NULL)
            return;
        if (checkExists(root, p) && checkExists(root, q))
            list.push_back(root);
        makeList(root->left, list, p, q);
        makeList(root->right, list, p, q);
    }

    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
    {
        vector<TreeNode *> list;

        makeList(root, list, p, q);

        return list.back();
    }
};