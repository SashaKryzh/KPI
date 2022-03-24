#include <iostream>
#include <iomanip>

struct Node
{
	int data;
	Node *left;
	Node *right;
};

Node *createNode(int data)
{
	Node *n = new Node();
	n->data = data;
	n->left = NULL;
	n->right = NULL;
	return n;
}

Node *insert(Node *root, int data)
{
	if (!root)
		return createNode(data);

	if (data <= root->data)
		root->left = insert(root->left, data);
	else
		root->right = insert(root->right, data);

	return root;
}

void printTree(const Node *root, int lvl = 1)
{
	if (!root)
		return;
	printTree(root->right, lvl + 1);
	printf("%*d\n", lvl * 4, root->data);
	printTree(root->left, lvl + 1);
}

Node *minValueNode(Node *node)
{
	Node *current = node;
	while (current && current->left != NULL)
		current = current->left;
	return current;
}

Node *deleteNode(Node *root, int data)
{
	if (root == NULL)
		return root;

	if (data < root->data)
		root->left = deleteNode(root->left, data);

	else if (data > root->data)
		root->right = deleteNode(root->right, data);

	else
	{
		if (root->left == NULL and root->right == NULL)
			return NULL;

		else if (root->left == NULL)
		{
			Node *temp = root->right;
			delete root;
			return temp;
		}
		else if (root->right == NULL)
		{
			Node *temp = root->left;
			delete root;
			return temp;
		}

		Node *temp = minValueNode(root->right);
		root->data = temp->data;
		root->right = deleteNode(root->right, temp->data);
	}

	return root;
}

Node *deleteTree(const Node *root)
{
	if (!root)
		return;
	deleteTree(root->left);
	deleteTree(root->right);
	delete root;
	return NULL;
}

int treeDepth(Node *root, int depth = 0)
{
	if (!root)
		return depth;
	return std::max<int>(treeDepth(root->left, depth + 1), treeDepth(root->right, depth + 1));
}

void countNodes(Node *root, int count[], int depth = 0)
{
	if (!root)
		return;
	if (!root->left && !root->right)
		count[depth]++;
	countNodes(root->left, count, depth + 1);
	countNodes(root->right, count, depth + 1);
}

void process(Node *root)
{
	int depth = treeDepth(root);
	int *count = new int[depth];
	memset(count, 0, depth * sizeof(int));
	countNodes(root, count);
	std::cout << "lvl: n\n------" << std::endl;
	for (int i = 0; i < depth; i++)
		std::cout << std::setw(3) << i << ": " << count[i] << std::endl;
	delete[] count;
}

int main()
{
	Node *root = NULL;
	int data = 0;

	std::cout << "Enter 15 values to insert in the tree:" << std::endl;
	for (int i = 0; i < 15; i++)
	{
		// std::cin >> data;
		data = rand() % 20;
		root = insert(root, data);
	}

	printTree(root);
	std::cout << std::endl;
	process(root);

	int del;
	std::cout << "\nEnter value to delete from tree: ";
	std::cin >> del;
	deleteNode(root, del);
	printTree(root);

	root = deleteTree(root);
	printTree(root);

	return 0;
}