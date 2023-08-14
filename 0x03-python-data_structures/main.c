#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

    printf("%s", __TIME__);
    if (is_palindrome(&head) == 1)
    {
        printf("Linked list is a palindrome\n");
        printf("%s", __TIME__);
    }
    else
    {
        printf("Linked list is not a palindrome\n");
        printf("%s", __TIME__);
    }
    free_listint(head);

    return (0);
}