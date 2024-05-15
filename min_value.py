# Визначення класу вузла для BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функція для вставки вузла в BST
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Функція для пошуку найменшого значення у BST
def find_min_value(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.key

# Приклад використання
root = None
keys = [15, 1, 20, 8, 12, 7, 5]

for key in keys:
    root = insert(root, key)

print("Найменше значення у дереві:", find_min_value(root))