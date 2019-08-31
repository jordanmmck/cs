# CSS, SCSS

## BEM block element modifier

- block, element, modifier
- the example below is just a naming convention which means the class `header__title` should be found in the header attached to a title of some kind
- block element
- element modifier

```scss
.header__title {
  color: red;
}
.button--link {
  color: red;
}
```

```html
<h1 className="header__title">Title</h1>
<button className="button button--link">OK</button>
```

## Normalize CSS

- all the browsers start with different baseline styles that we should reset so that our styles are consistent

## CSS

- padding: top, right, bottom, left
- margin: 0 top and bottom, 10 left and right
- "sass reference functions": darken(), etc.

```scss
.container {
  padding: 1px 2px 3px 4px;
  border: 0.6rem solid darken($purple, 10%);
  margin: 0 10;
}
.big-button:disabled {
  opacity: 0.5;
}
```

## media query

```scss
@media (min-width: 45rem) {
  .add-option {
    flex-direction: row;
  }
  .add-option__input {
    margin: 0 $s-size 0 0;
  }
}
```
