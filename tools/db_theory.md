# Databases

## Normal Forms

### 1st normal

- No top-to-bottom ordering to the rows.
- No left-to-right ordering to the columns.
- No duplicate rows.
- Every row-and-column intersection contains exactly one value from the applicable domain (and nothing else).
- All columns are regular [i.e. rows have no hidden components such as row IDs, object IDs, or hidden timestamps].
- All column entries must be same length and one value (so tel # can't have two numbers in it)
- Data must be from applicable domain (tel #'s are 12 characters long for example)
- Can't have multiple groups for a domain (can't have multiple tel # columns)
- No nulls

### 2nd normal

- 1NF + rows must be dependent on whole candidate (re: representative) key

### 3rd normal
- Every non-key attribute "must provide a fact about the key, the whole key, and nothing but the key" -> the information must be relevant directly to the key, not transitively through another column

+ Joins
  * inner: Only rows that match the WHERE
  * left:  Include all rows from left table, when there is not a match with the right table its corresponding columns are NULL
  * right: Opposite of left
  * full:  All rows returned, those columns where both tables do not match have NULL for the non-matching table's columns
+ Keys
  * primary: Unique identifier in a table
  * foreign: Primary key from another table
