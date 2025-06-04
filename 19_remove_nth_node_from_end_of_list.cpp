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
class Solution
{
public:
    int listSize(ListNode *head)
    {
        if (!head->next)
        {
            return 1;
        }

        return 1 + listSize(head->next);
    }

    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        int size = listSize(head);

        if (size == 1 && n == 1)
        {
            return nullptr;
        }

        if (size == 2 && n == 1)
        {
            head->next = nullptr;
            return head;
        }

        if (size == n)
        {
            return head->next;
        }

        ListNode *dummy = head;

        for (int i = 0; i < size - n - 1; i++)
        {
            dummy = dummy->next;
        }

        dummy->next = dummy->next->next;
        return head;
    }
};