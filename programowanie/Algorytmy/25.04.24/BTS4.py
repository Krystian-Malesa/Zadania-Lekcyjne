# Zadanie 3: Wizualizacja drzewa
# Zadanie: Stwórz program lub skrypt, który pozwoli wizualizować drzewo binarne. Użytkownik powinien móc podać ciąg operacji wstawiania.


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1

def is_balanced(root):
    if root is None:
        return True
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        if abs(left_height - right_height) > 1: 
            return False
        else:
            return is_balanced(root.left) and is_balanced(root.right)

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

print("\nHeight of the tree:", height(root))

if is_balanced(root):
    print("The tree is balanced.")
else:
    print("The tree is not balanced.")

