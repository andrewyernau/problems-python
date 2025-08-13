#Given the beginning of a singly linked list head, reverse the list, 
# and return the new beginning of the list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev,curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
            


#CHATGPT to create a linked list for testing
# Helper para crear lista enlazada desde lista Python
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper para convertir lista enlazada a lista Python (para imprimir)
def linked_list_to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

solution = Solution()
head = build_linked_list([0,1,2,3])
output = solution.reverseList(head)

print(f"Input: {head}")
print(f"Output: {linked_list_to_list(output)}") # Output : [3,2,1,0]