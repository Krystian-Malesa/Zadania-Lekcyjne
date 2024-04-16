#Eksploracja Poziom po Poziomie

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if root in None:
        return
    
    queue = deque([root])


    while queue:
        current_node = queue.popleft()
        print(current_node.value)

        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)


root = None(1)
root.left = None(2)
root.right = None(3)
root.left.left = None(4)
root.left.right = None(5)
root.right.right = None(6)


print("Przeszukiwanie wszerz (BFS): ")

