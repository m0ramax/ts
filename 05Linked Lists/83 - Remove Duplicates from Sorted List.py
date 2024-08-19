# 83. Remove Duplicates from Sorted List

# Given the head of a sorted linked list, 
# delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

# Definición de la clase ListNode para la lista enlazada
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Clase Solution con el método deleteDuplicates
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Saltar el nodo duplicado
            else:
                current = current.next  # Avanzar al siguiente nodo
        return head

# Función para construir una lista enlazada a partir de una lista de Python
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Función para imprimir la lista enlazada
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Pruebas
input_list = [1, 1, 2, 3, 3]  # Ejemplo de entrada
linked_list = build_linked_list(input_list)  # Construir la lista enlazada

print("Lista enlazada antes de eliminar duplicados:")
print_linked_list(linked_list)  # Mostrar la lista antes de eliminar duplicados

sol = Solution()
linked_list = sol.deleteDuplicates(linked_list)  # Eliminar duplicados

print("Lista enlazada después de eliminar duplicados:")
print_linked_list(linked_list)  # Mostrar la lista después de eliminar duplicados
