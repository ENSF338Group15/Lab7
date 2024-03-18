import random
import sys
import time
import timeit
from matplotlib import pyplot as plt

sys.setrecursionlimit(10000)

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        current = self
        parent = None
        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right
        if data <= parent.data:
            parent.left = Node(data, parent)
        else:
            parent.right = Node(data, parent)

    def search(self, data):
        current = self
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


def balance_factors(node):
    if node is not None:
        left_height = find_height(node.left)
        right_height = find_height(node.right)
        balance_factor = left_height - right_height
        return balance_factor
        # print(f"Node {node.data}: Balance: {balance_factor}")
        # print_balance_factors(node.left)
        # print_balance_factors(node.right)


# Simplifying to measure performance on a smaller set of tasks
for t in range(1000):
    tasks = random.sample(range(10000), 1000)

    bst = Node(tasks.pop(0))
    for i in tasks:
        bst.insert(i)

    performance_records = []
    balances = []
    search_time = timeit.timeit(lambda: bst.search(t), globals=globals(), number=10000)
    performance_records.append(search_time)  # Simplified measure of performance
    balances.append(balance_factors(bst))

# Plotting the simplified performance records
    plt.plot(balances, performance_records, 'o')
plt.xlabel('Balance')
plt.ylabel('Search Time (s)')
plt.title('Search Time for Each Task')
plt.savefig('ex1.png')
plt.show()
