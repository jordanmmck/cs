# Commands

## Planaria

```zsh
npm install --save neonplanaria mongodb
node index
npm install --save neonplanaria bitquery
node server
```

## PSQL

```psql
\c jordan;
DROP DATABASE lazy_prices;
CREATE DATABASE lazy_prices;
CREATE USER lazy_prices_user WITH PASSWORD 'lazy_password';
GRANT ALL PRIVILEGES ON DATABASE lazy_prices TO lazy_prices_user;
\c lazy_prices;
```

```psql
SELECT * FROM data_exchange;
SELECT name FROM data_company;
DELETE FROM data_company WHERE symbol<>'AE';
select count(*) from data_company;
```

```psql
delete from data_filingsection;
```

## MongoDB

```
show dbs
use planaria
show collections
```
