# Hashtables

## Concept

A hashtable can be used to implement an associative array (an array of keys mapping to an array of values).
A mapping of keys to values.
The table may be an array which holds numbers, but could also be a pointer to an object.

`load factor` = number of entires/number of buckets

## Performance

`operation`   `average`   `worst`
space           O(n)        O(n)
search          O(1)        O(n)
insert          O(1)        O(n)
delete          O(1)        O(n)
