class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def update_height(self):
        self.height = max(find_height(self.left), find_height(self.right)) + 1

    def left_rotate(self):
        y = self.right
        l = y.left
        y.left = self
        self.right = l
        self.update_height()
        y.update_height()
        return y

    def right_rotate(self):
        y = self.left
        r = y.right
        y.right = self
        self.left = r
        self.update_height()
        y.update_height()
        return y

    def insert(self, key):
        if not self.data:
            self.data = key
            return self
        elif key < self.data:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left = self.left.insert(key)
        else:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right = self.right.insert(key)

        self.update_height()
        balance = balance_factors(self)

        if -2 < balance < 2:
            print("Case #1: Pivot not detected")
            return self

        if balance > 1:
            if key > self.left.data:
                print("Case #3a: adding a node to an outside subtree")
                self.left = self.left.left_rotate()
                return self.right_rotate()
            else:
                print("Case 3b not supported")
                return self
        if balance < -1:
            if key < self.right.data:
                print("Case #3a: adding a node to an outside subtree")
                self.right = self.right.right_rotate()
                return self.left_rotate()
            else:
                print("Case 3b not supported")
                return self

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
        return 0
    return node.height


def balance_factors(node):
    if node is None:
        return 0
    return find_height(node.left) - find_height(node.right)


print("Test Case 3a")
root = Node(20)
root = root.insert(30)
root = root.insert(25)  # This will trigger Case 3a

print("Test Case 3b")
root = Node(20)
root = root.insert(30)
root = root.insert(35)  # This will trigger Case 3b