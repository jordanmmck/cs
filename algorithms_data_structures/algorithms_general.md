# General Algorithm stuff

## Types of Algorithms

`greedy`: make locally optimum choice at each stage
`dynamic programming`:
`hill climbing`: start with some solution, incrementally change single element of solution to improve solution
`heuristic`: a practical method not optimal or perfect, but sufficient to help in most cases
`exact algorithm`: algorithm that always solves problem to optimallity.

## Techniques

`memoization`: an optimization technique of storing the results of some expensive computation so that the next time the computation is demanded this cached result is returned.

## etc

Always consider hash tables (dictionaries) with their O(1)-ness. ("Tip: using a dictionary is the most common way to get from a brute force approach to something more clever. It should always be your first thought.")

If at all array-related, try sorting first.

If search-related, consider binary search.

Start with a brute force solution, look for repeat work in that solution, and modify it to only do that work once.

Space-time trade-off! That is, for better time complexity, try using auxiliary data structures. E.g., do something in a single pass over an array—O(N) time—by using a hash table—O(N) space—vs. doing something in multiple passes—O(N ^ 2)—without using any extra space—O(1). What information can I store to save time? (Another example: O(1) get_max method for a Stack class stores extra information (the max at and below each element) to save time (instead of iterating through the stack O(N)).)

Try a greedy solution: Iterate through the problem space taking the optimal solution "so far" until the end. (Optimal if the problem has "optimal substructure," which means stitching together optimal solutions to subproblems yields an optimal solution.)

Remember that I can use two pointers (e.g., to get the midpoint by having one pointer go twice as fast, or in a sum problem by having the pointers work inward from either end, or to test if a string is a palindrome).

If the problem involves parsing or tree/graph traversal (or reversal in some way), consider using a stack.

Does solving the problem for size (N – 1) make solving it for size N any easier? If so, try to solve recursively and/or with dynamic programming. (Using the max/min function can help a lot in recursive or dynamic programming problems.)

A lot of problems can be treated as graph problems and/or use breadth-first or depth-first traversal.

If you have a lot of strings, try putting them in a prefix tree / trie.

Any time you repeatedly have to take the min or max of a dynamic collection, think heaps. (If you don’t need to insert random elements, prefer a sorted array.)