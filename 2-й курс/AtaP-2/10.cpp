#include <iostream>

struct Node
{
	int data;
	Node *next;
	Node *prev;
};

Node *createNote(const int data)
{
	Node *n = new Node();
	n->data = data;
	n->next = NULL;
	n->prev = NULL;
	return n;
}

Node *append(const Node *list, const int data)
{
	Node *n = (Node *)list;
	for (; n->next != NULL; n = n->next)
		continue;
	n->next = createNote(data);
	n->next->prev = n;
	return n->next;
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

void printCircularList(const Node *list)
{
	Node *first = (Node *)list;
	std::cout << first->data << " ";
	for (Node *n = first->next; n != first; n = n->next)
		std::cout << n->data << " ";
	std::cout << std::endl;
}

Node *process(const Node *list)
{
	Node *res = NULL;
	Node *first = (Node *)list;
	bool check = true;
	for (Node *n = first; check || n != first; n = n->next)
	{
		check = false;
		if (n->prev->data <= n->data && n->data >= n->next->data)
		{
			Node *new_n = createNote(n->data);
			if (res == NULL)
			{
				res = new_n;
				res->next = res;
				res->prev = res;
			}
			else
			{
				new_n->next = res;
				new_n->prev = res->prev;
				res->prev->next = new_n;
				res->prev = new_n;
			}
		}
	}
	return res;
}

int main(void)
{
	srand(time(0));
	Node *list = createNote(rand() % 10);
	Node *last;
	for (int i = 0; i < 10; i++)
		last = append(list, rand() % 10);
	last->next = list;
	list->prev = last;
	printCircularList(list);
	Node *res = process(list);
	printCircularList(res);
	list->prev->next = NULL;
	res->prev->next = NULL;
	deleteList(list);
	deleteList(res);
	return 0;
}
