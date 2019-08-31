# Arrays

## Concept

An array is a contiguous block in memory with fixed overall size and fixed size for each element. 
Each spot in the array may hold a number, address, word or whatever. 
A list is an abstract data type which may be implemented using an array.

`random access`: O(1)
`insert/delete`: O(n)
`wasted space`: 0
`sort`: O(nlogn)

## Common Problems

### Reverse list

1. Two pointers, one at start, one at end
2. Swap values of element at each pointer
3. Increment one, decrement other
4. Reapeat as long as i<j

### Rotate Array

1. Calculate the shift = `(size - num_rotations) % size`
2. Make new array T
3. `T[(i+shift)%size]=A[i]`

`runtime`: O(n)
`space`: O(n)

1. Store num_rotations elements in temp array
2. Shift other elements
3. append temp array to original

`runtime`: O(n)
`space`: O(num_rotations)

### Given NxN matrix rotate matrix by 90 degrees (can you do it in place?)
