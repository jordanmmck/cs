# PSQL

## Connect

```psql
# start psql as postgres superuser
$ psql postgres
postgres=# CREATE ROLE me WITH LOGIN PASSWORD 'password';
postgres=# ALTER ROLE me CREATEDB;
postgres=# \q
$ psql -d postgres -U me
postgres=> CREATE DATABASE api;
postgres=> \l
postgres=> \c api;
api=> CREATE TABLE comics (
  ID SERIAL PRIMARY KEY,
  name VARCHAR(60),
  author VARCHAR(30)
);
api=> INSERT INTO comics (name, author)
  VALUES ('Spider-man vs. Deadpool', 'F. Hayak'), ('The Superman', 'F. Nietzsche');
api=> select * from users;
```

```psql
// install postgres
// switch user to user 'postgres'
$ sudo su - postgres
// start psql command prompt
$ psql

$ sudo su - postgres
postgres@cmdcenter:~$ createdb auth
postgres@cmdcenter:~$ createuser auth

CREATE DATABASE mything;
CREATE USER mythinguser WITH PASSWORD 'password';
// django:
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
// quit psql command prompt back to postgres user bash
# \q
// back home
```

## Change postgres password

```
$ \c template1
$ ALTER USER postgres PASSWORD 'newPassword';
```

## Quick psql cmd prompt

`$ sudo -u postgres psql`

## connect

`\c dbname`

## Drop user/role

`# DROP USER openproblems;`

## Drop database

`# DROP DATABASE openproblems;`

```
// get useful info like db name, user, port etc
$ \conninfo
$ sudo pkill -u postgres
$ \d myTable
// list db's
$ \l
// list everything
$ \dt *.
```

## Change port

`edit /etc/postgresql/9.5/main/postgresql.conf`

## Restart

`/etc/init.d/postgresql restart`

## admin password

`psql –c "ALTER USER user PASSWORD 'password';"`
