# Przykladowa tablica reprezentująca drzewo binarne
tree = [1, 2, 3, 4, 5, 6, 7]

def get_left_child(index):
    #Zwarca lewe dziecko węzła o danym indeksie.
    return 2 * index + 1

def get_right_child(index):
    #Zwarca prawe dziecko węzła o danym indeksie.
    return 2 * index + 1

def get_parent(index):
    #Zwarca rodzica węzła o danym indeksie.
    return (index -1) // 2


# Dostęp do elementów drzewa
index = 0 # Korzeń drzewa
left_child_index = get_left_child(index)
right_right_child = get_right_child(index)

print(f"Wartość korzenia: {tree[index]}")
print(f"lewe korzenia: {tree[left_child_index]}")
print(f"Prawe korzenia: {tree[right_right_child]}")
