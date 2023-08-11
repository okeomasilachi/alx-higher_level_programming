#include "lists.h"
#include <stdbool.h>

/**
 * sort_list - Sorts a linked list in ascending order
 * @head: The head of the linked list
 *
 * Return: A pointer to the sorted linked list
 */
listint_t *sort_list(listint_t *head)
{
	bool swapped;
	listint_t *current;
	listint_t *last_swapped = NULL;

	if (head == NULL || head->next == NULL)
		return (head);

	do {
		swapped = false;
		current = head;

		while (current->next != last_swapped)
		{
			if (current->n > current->next->n)
			{
				int temp = current->n;

				current->n = current->next->n;
				current->next->n = temp;
				swapped = true;
			}
			current = current->next;
		}
		last_swapped = current;
	} while (swapped);

	return (head);
}

/**
 * insert_node - inserts into a sorted list
 * @head: pointer to the head of list
 * @number: numberto insert
 *
 * Return: list if successful
*/
listint_t *insert_node(listint_t **head, int number)
{
	add_nodeint_end(head, number);
	return (sort_list(*head));
}
