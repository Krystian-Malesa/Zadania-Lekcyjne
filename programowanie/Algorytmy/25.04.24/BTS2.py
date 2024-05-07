# Zadanie 1: Spradzanie wysokosci drzewa
# Zadanie: Napisz funkcję, która oblicza wysokość drzewa binarnego. Wysokość drzewa jest najdluższą ścieżką od korzenia do liscia.


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(3)
root.right.left = TreeNode(15)
root.right.right = TreeNode(30)

print("Pre-order:")
preorder(root)

print("\nIn-order:")
inorder(root)

print("\nPost-order:")
postorder(root)

print("Wysokość drzewa:", height(root))
