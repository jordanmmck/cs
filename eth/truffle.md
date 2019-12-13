# Truffle

```zsh
truffle compile
```

## Ganache

To use Ganache,

```js (truffle-config.js)
module.exports = {
  networks: {
    development: {
      host: '127.0.0.1',
      port: 7545,
      network_id: '*',
    },
  },
};
```

```zsh
truffle migrate
truffle console
```
