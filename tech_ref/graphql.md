# GraphQL

## SDL (schema def lang)

- relationship between Person and Post is defined
- `!` means you will _always_ get the type back, not null

```graphql
type Person {
  name: String!
  age: Int!
  posts: [Post!]!
}

type Post {
  title: String!
  author: Person!
}
```
