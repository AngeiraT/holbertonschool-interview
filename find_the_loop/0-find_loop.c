#include "lists.h"

/**
 * find_listint_loop - Finds the loop in a linked list.
 *
 * @head: The head of the node.
 * Return: The address of the node where the loop starts or NULL.
 */
listint_t *find_listint_loop(listint_t *head)
{
	listint_t *fast, *slow;

	if (!head)
		return (NULL);
	fast = slow = head;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = (fast->next)->next;
		if (fast == slow)
		{
			slow = head;
			while (slow && fast)
			{
				if (slow == fast)
					return (slow);
				slow = slow->next;
				fast = fast->next;
			}
		}
	}
	return (NULL);
}
