# Linked Lists

A linked list consists of nodes connected via links.
In a singly linked list each node has it's value and a pointer to the next node.
In a doubly linked list each node points to its next as well as its previous.

## Performance

`random access`: O(n)
`insert/delete at head`: O(1)
`insert/delete at some index`: O(n) + O(1)
`wasted space`: O(n)
