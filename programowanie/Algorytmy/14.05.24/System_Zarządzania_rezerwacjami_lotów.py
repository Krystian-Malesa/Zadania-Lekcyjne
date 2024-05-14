class Node:
    def __init__(self, reservation_id, passenger_name, flight_date):
        self.reservation_id = reservation_id
        self.passenger_name = passenger_name
        self.flight_date = flight_date
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_reservation(self, reservation_id, passenger_name, flight_date):
        new_node = Node(reservation_id, passenger_name, flight_date)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current_node, new_node):
        if new_node.reservation_id < current_node.reservation_id:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert(current_node.left, new_node)
        elif new_node.reservation_id > current_node.reservation_id:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert(current_node.right, new_node)
        else:
            # Jeśli ID rezerwacji jest takie samo, nadpisujemy dane (lub można rzucić wyjątkiem)
            current_node.passenger_name = new_node.passenger_name
            current_node.flight_date = new_node.flight_date

    def find_reservation(self, reservation_id):
        return self._search(self.root, reservation_id)

    def _search(self, current_node, reservation_id):
        if current_node is None:
            return None
        if reservation_id == current_node.reservation_id:
            return current_node
        elif reservation_id < current_node.reservation_id:
            return self._search(current_node.left, reservation_id)
        else:
            return self._search(current_node.right, reservation_id)

    def delete_reservation(self, reservation_id):
        self.root = self._delete_node(self.root, reservation_id)

    def _delete_node(self, current_node, reservation_id):
        if current_node is None:
            return current_node
        if reservation_id < current_node.reservation_id:
            current_node.left = self._delete_node(current_node.left, reservation_id)
        elif reservation_id > current_node.reservation_id:
            current_node.right = self._delete_node(current_node.right, reservation_id)
        else:
            # Usuwanie wezła z dwoma dziećmi
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            temp = self._min_value_node(current_node.right)
            current_node.reservation_id = temp.reservation_id
            current_node.passenger_name = temp.passenger_name
            current_node.flight_date = temp.flight_date
            current_node.right = self._delete_node(current_node.right, temp.reservation_id)
        
        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def display_in_order(self):
        reservations = []
        self._in_order_traversal(self.root, reservations)
        for reservation in reservations:
            print(f"ID: {reservation.reservation_id}, Passenger: {reservation.passenger_name}, Flight Date: {reservation.flight_date}")

    def _in_order_traversal(self, node, reservations):
        if node:
            self._in_order_traversal(node.left, reservations)
            reservations.append(node)
            self._in_order_traversal(node.right, reservations)

# Przykładowe użycie:
tree = BinarySearchTree()
tree.add_reservation(1, "John Doe", "2023-05-15")
tree.add_reservation(2, "Jane Smith", "2023-06-20")
tree.add_reservation(3, "Emily Davis", "2023-07-25")

print("Wszystkie rezerwacje:")
tree.display_in_order()

print("\nSzukam rezerwacji z ID 2:")
reservation = tree.find_reservation(2)
if reservation:
    print(f"Znaleziono rezerwację: ID: {reservation.reservation_id}, Passenger: {reservation.passenger_name}, Flight Date: {reservation.flight_date}")
else:
    print("Rezerwacja nie znaleziona.")

print("\nUsuwam rezerwację z ID 2")
tree.delete_reservation(2)

print("\nWszystkie rezerwacje po usunięciu:")
tree.display_in_order()
