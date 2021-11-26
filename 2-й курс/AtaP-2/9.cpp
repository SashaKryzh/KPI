#include <iostream>

struct Node
{
	int data;
	Node *next;
};

Node *createNote(const int data)
{
	Node *n = new Node();
	n->data = data;
	n->next = NULL;
	return n;
}

void appendNode(const Node *list, const int data)
{
	Node *n = (Node *)list;
	for (; n->next != NULL; n = n->next)
		continue;
	n->next = createNote(data);
}

Node *deleteFirstNode(Node *list)
{
	Node *tmp = list->next;
	delete list;
	return tmp;
}

void deleteList(Node *list)
{
	for (Node *n = deleteFirstNode(list); n != NULL; n = deleteFirstNode(n))
		continue;
}

void printList(const Node *list)
{
	for (Node *n = (Node *)list; n != NULL; n = n->next)
		std::cout << n->data << " ";
	std::cout << std::endl;
}

Node *process(const Node *list)
{
	Node *res = NULL;
	Node *prev = NULL;
	for (Node *n = (Node *)list; n != NULL; n = n->next)
	{
		if ((prev == NULL || prev->data <= n->data) &&
			(n->next == NULL || n->next->data <= n->data))
		{
			if (res == NULL)
				res = createNote(n->data);
			else
				appendNode(res, n->data);
		}
		prev = n;
	}
	return res;
}

int main(void)
{
	srand(time(0));
	Node *list = createNote(rand() % 10);
	for (int i = 0; i < 10; i++)
		appendNode(list, rand() % 10);
	printList(list);
	Node *res = process(list);
	printList(res);
	deleteList(list);
	deleteList(res);
	return 0;
}
