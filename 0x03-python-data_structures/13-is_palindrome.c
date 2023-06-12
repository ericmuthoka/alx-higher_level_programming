#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - function that checks palindrome
 * @head: pointer to head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t** head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	listint_t* slow = *head;
	listint_t* fast = *head;
	listint_t* prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		listint_t* next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
		{
			return (0);
		}

		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}

