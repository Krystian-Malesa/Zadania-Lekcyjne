class Node:
    def __init__(self, reservation_id:int, passenger_name:str, flight_date:str):
        self.reservation_id = reservation_id
        self.passenger_name = passenger_name
        self.flight_date = flight_date
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def add_reservation(self, reservation_id:int, passenger_name:str, flight_date:str):
        if self.root is None:
            self.root = Node(reservation_id, passenger_name, flight_date)
        else:
            self._insert(self.root,reservation_id,passenger_name,flight_date)

    def _insert(self, current_node: Node, reservation_id:int,passenger_name:str, flight_date:str):
        


        if reservation_id < current_node. reservation_id:
            if current_node.left is None:
                current_node.left = Node(reservation_id, passenger_name,flight_date)
            else:
                self._insert(current_node.left, reservation_id, passenger_name, flight_date)
        elif reservation_id > current_node. reservation_id:
            if current_node.right is None:
                current_node.right = Node(reservation_id, passenger_name,flight_date)
            else:
                self._insert(current_node.right, reservation_id, passenger_name, flight_date)
        else:
            print("Rezerwacja już istnieje!")


    def find(self, reservation_id:int):
        return self._find(self.root, reservation_id)



    def _find(self, current_node, reservation_id:int):

        if current_node:
            if reservation_id == current_node.reservation_id:
                return current_node
            elif reservation_id < current_node.reservation_id:
                return self._find(current_node.left, reservation_id)
            else:
                return self._find(current_node.left, reservation_id)
        else:
            return None


    
    def delete(self, reservation_id):
        self.root = self._delete(self.root, reservation_id)
        return reservation_id



    def _delete(self, current_node: Node, reservation_id:int):
        if current_node is None:
            return current_node
        
        if reservation_id < current_node.reservation_id:
            current_node.left = self._delete(current_node.left, reservation_id)
        elif reservation_id > current_node.reservation_id:
            current_node.right = self._delete(current_node.right, reservation_id)
        else:
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp
            
        
        temp = self.find_min(current_node.right)

        current_node.reservation_id = temp.reservation_id
        current_node.passenger_name = temp.passenger_name
        current_node.flight_date = temp.flight_date

        current_node.right = self._delete(current_node)

    




    def find_min(self, current_node:Node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node





bst = BinarySearchTree


bst.insert(100, "John Dee", "2023-10-05")
bst.insert(101, "Jane Dee", "2023-10-05")
bst.insert(99, "Alice Dee", "2023-10-05")



found = bst.find(100)
if found:
    print(f"Znaleziono rezerwacje: {found.passanger_name} z dnia {found.flight_date}")
else:
    print("Rezerwacja nie znaleziona")

cancel = bst.delete(100)
print(f"Anulowano rezerwacje {cancel}")