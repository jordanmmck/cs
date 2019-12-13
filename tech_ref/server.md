- do not set a default secret key, the app should fail if missing
- defaults should be safe - debug default should be false

```
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1').split(',')
```

- each ADD/COPY/RUN command produces a layer in docker, so compress them

DJANGO_ALLOWED_HOSTS: Set this to the IP address of your Ubuntu server. For testing purposes, you can also set it to \*, a wildcard that will match all hosts. Be sure to set this value appropriately when running Django in a production environment.
