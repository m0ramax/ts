class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def deleteDuplicated(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print('None')

list = LinkedList()
list.insert(3)
list.insert(3)
list.insert(3)
list.insert(2)
list.insert(2)
list.insert(1)
list.insert(1)
list.insert(1)
list.insert(1)

list.show()

list.deleteDuplicated()
list.show()