def has_cycle(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head
    while(1):
        slow = slow.next
        fast = fast.next

        if fast is None or fast.next is None:
            return False
        fast = fast.next
        if slow == fast:
            return True
