#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

#The new list should be made up of nodes from list1 and list2.

class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        dummy = tail = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next
            


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
list1 = build_linked_list([])
list2 = build_linked_list([1,2])
print(f"Input: {linked_list_to_list(list1),linked_list_to_list(list2)}")
output = solution.mergeTwoLists(list1,list2)


print(f"Output: {linked_list_to_list(output)}") # Output : [1,1,2,3,4,5]