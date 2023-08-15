#include "lists.h"

/**
 * is_palindrome - checks if a Linked list is a palindrome
 * @head:
 *
 * Return: 1 if linked list is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	int arr_num[3000];
	int i, j;

	if (cur == NULL || cur->next == NULL)
		return (1);

	for (i = 0; cur != NULL; i++)
	{
		arr_num[i] = cur->n;
		cur = cur->next;
	}
	i--;
	for (j = 0; i > j; i--, j++)
		if (arr_num[j] != arr_num[i])
			return (0);

	return (1);
}
