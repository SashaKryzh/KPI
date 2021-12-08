#include <iostream>

struct Node
{
	int data;
	Node *next;
};

void push(Node **head, int data)
{
	Node *n = new Node();
	n->data = data;
	n->next = *head;
	*head = n;
}

int pop(Node **head)
{
	int tmp = (*head)->data;
	*head = (*head)->next;
	return tmp;
}

void deleteStack(Node *head)
{
	for (Node *n = head; n != NULL;)
	{
		Node *tmp = n->next;
		delete n;
		n = tmp;
	}
}

void printStack(const Node *head)
{
	for (Node *n = (Node *)head; n != NULL; n = n->next)
		std::cout << n->data << " ";
	std::cout << std::endl;
}

void process(const Node *head)
{
	int min = head->data;
	int max = head->data;
	for (Node *n = (Node *)head; n != NULL; n = n->next)
	{
		if (n->data < min)
			min = n->data;
		else if (n->data > max)
			max = n->data;
	}
	printf("min: %d, max: %d\n", min, max);
}

int main(void)
{
	srand(time(0));
	Node *stack = NULL;
	for (int i = 0; i < 10; i++)
		push(&stack, rand() % 100 - 50);
	printStack(stack);
	process(stack);
	return 0;
}
