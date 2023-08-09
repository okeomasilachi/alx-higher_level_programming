#include "lists.h"

/**
 * check_cycle - checks for cycle in a linked list
 * @list: ponter to the head of the list
 *
 * Return: 1 on if circle else 0 is returned
*/
int check_cycle(listint_t *list)
{
	listint_t *first = list->next;
	listint_t *sec = list->next;

	while (sec != NULL)
	{
		if (sec == NULL)
			return (0);
		sec = sec->next;
		if (sec == first)
			return (1);
	}
	return (0);
}
