# # 19. Remove Nth Node From End of List


# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?
# Definición del nodo de una lista enlazada
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Nodo ficticio para manejar el caso donde el nodo a eliminar es el primero
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Mover `first` n+1 posiciones hacia adelante
        for _ in range(n + 1):
            first = first.next

        # Mover ambos punteros hasta que `first` llegue al final
        while first:
            first = first.next
            second = second.next

        # Eliminar el nodo saltando el enlace
        second.next = second.next.next

        # Retornar la nueva cabeza de la lista
        return dummy.next
