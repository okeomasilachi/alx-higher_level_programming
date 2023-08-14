#include "lists.h"

/**
 * dup_list - Duplicates a linked list
 * @head: The head of the linked list to duplicate
 *
 * Return: A pointer to the duplicated linked list
 */
listint_t *dup_list(listint_t *head)
{
	listint_t *new = NULL;

	if (head == NULL)
		return (new);
	new = malloc(sizeof(listint_t));
	new->n = head->n;
	new->next = dup_list(head->next);

	return (new);
}

/**
 * is_palindrome - checks if a Linked list is a palindrome
 * @head:
 *
 * Return: 1 if linked list is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *cur = *head, *_list, *_list_1, *next_1, *temp;

	if (cur == NULL || cur->next == NULL)
		return (1);
	_list = dup_list(*head);
	_list_1 = _list;
	next_1 = _list->next;
	_list->next = NULL;
	while (next_1 != NULL)
	{
		temp = next_1->next;
		next_1->next = _list_1;
		_list_1 = next_1;
		next_1 = temp;
	}
	while (cur != NULL)
	{
		if (cur->n != _list_1->n)
			return (0);
		cur = cur->next;
		_list_1 = _list_1->next;
	}
	free_listint(_list);
	free_listint(_list_1);
	free_listint(next_1);
	free(temp);
	return (1);
}
