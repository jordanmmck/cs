# Hashtables

- can be used to implement associative array (dictionary)
- table might hold numbers, or point to objects

`load factor` = num_entries/num_buckets (how full is it)

## Performance

`operation`   `average`   `worst`
space           O(n)        O(n)
search          O(1)        O(n)
insert          O(1)        O(n)
delete          O(1)        O(n)
