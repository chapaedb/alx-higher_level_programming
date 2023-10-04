#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *prev, *nxt;

    if (list == NULL || list->next == NULL)
        return (0);

    prev = list;
    nxt = list->next;

    while (nxt && nxt->next)
    {
        if (prev == nxt)
            return (1);

        prev = prev->next;
        nxt = nxt->next->next;
    }

    return (0);
}
