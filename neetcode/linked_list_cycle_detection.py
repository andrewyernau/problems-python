#Given the beginning of a linked list head, return true if there is a cycle in the linked list. 
# Otherwise, return false.

#There is a cycle in a linked list if at least one node in the list can be visited again by 
# following the next pointer.

#Internally, index determines the index of the beginning of the cycle, if it exists. 
# The tail node of the list will set it's next pointer to the index-th node. If index = -1, 
# then the tail node points to null and no cycle exists.

#Note: index is not given to you as a parameter.

class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow,fast = head,head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            


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
list1 = build_linked_list([1,2,3,4])
index = 1
print(f"Input: {linked_list_to_list(list1),index}")
output = solution.hasCycle(list1)


print(f"Output: {(output)}") # Output : [1,1,2,3,4,5]