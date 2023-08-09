#include "lists.h"

/**
 * check_cycle - checks for cycle in a linked list
 * @list: head to the list
 *
 * Return: 1 on if circle else 0 is returned
*/
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *sec = list;

	while (sec != NULL)
	{
		first = first->next;
		sec = sec->next;
		if (sec == NULL)
			return (0);
		sec = sec->next;
		if (sec == first)
			return (1);
	}
	return (0);
}
