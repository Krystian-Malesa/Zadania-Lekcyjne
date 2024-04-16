class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_preorder(node):
    if node:
        print(node.value)  # Odwiedź węzeł
        dfs_preorder(node.left)  # Eksploruj lewe poddrzewo
        dfs_preorder(node.right)  # Eksploruj prawe poddrzewo


# Tworzenie przykładowego drzewa 
#      1
#     / \
#     2  3
#    / \
#   4   5


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# Rozpoczecie przeszukiwania w głab (DFS) z korzenia
print("Przeszukiwanie w głab (DFS) - Pre-order: ")
dfs_preorder(root)

                 

    