import random


class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right


def insert(data, root=None):
    current = root
    parent = None
    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right
    if root is None:
        root = Node(data)
    elif data <= parent.data:
        parent.left = Node(data, parent)
    else:
        parent.right = Node(data, parent)


def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
            if current is None:
                return None
            continue
        else:
            current = current.right
            if current is None:
                return None
            continue


def find_height(node):
    if node is None:
        return -1
    left_height = find_height(node.left)
    right_height = find_height(node.right)
    return max(left_height, right_height) + 1


def print_balance_factors(node):
    if node is not None:
        left_height = find_height(node.left)
        right_height = find_height(node.right)
        balance_factor = left_height - right_height
        print(f"Node {node.data}: Balance: {balance_factor}")
        print_balance_factors(node.left)
        print_balance_factors(node.right)


num_list = [random.randint(0, 10000) for _ in range(1000)]
root = Node(random.randint(0, 10000))
for num in num_list[1:]:
    insert(num, root)
target = random.choice(num_list)
for i in range(1000):
    search(target, root)

