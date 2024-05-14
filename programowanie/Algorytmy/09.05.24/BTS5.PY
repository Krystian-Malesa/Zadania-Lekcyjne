class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Wysokość węzła inicjalnie ustawiona na 1

def update_height(node):
    # Aktualizacja wysokości węzła na podstawie wysokości jego dzieci
    max(height(node.left), height )

def height(node):
    # Pobieranie wysokości węzła, jeśli węzeł nie istnieje zwróć 0

def right_rotate(x):

def right_rotate(y):
    # Wykonanie rotacji w prawo na węźle y
    x = y.left
    T2 = x.right

    # Przeprowadzenie  rotacji
    x.right = y
    y.left = T2 

    update_height(x)
    update_height(y)

    return x

def right_left_rotate(node):


# Użycie:
# Załóżmy, że mamy drzewo AVL i potrzebujemy wykonać rotację w prawo na węźle 'y'
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print(root.key)
# Wykonanie rotacji w prawo
root = right_rotate (root)
print(root.key)