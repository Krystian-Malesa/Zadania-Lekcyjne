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


root = TreeNode(9)
root.left = TreeNode(2)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(8)
root.left.right.right.left = TreeNode(5)
root.left.right.right.left.right = TreeNode(7)
root.right.left = TreeNode(11)
root.right.left.left = TreeNode(10)
root.right.left.right = TreeNode(13)
root.right.left.right.left = TreeNode(12)
root.right.left.right.right = TreeNode(14)

print("Pre-order:")
preorder(root)

print("\nIn-order:")
inorder(root)

print("\nPost-order:")
postorder(root)



