#!/bin/sh

initdb -D /var/lib/postgresql/data
echo "host all all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/
echo "listen_addresses='*'" >> /var/lib/postgresql/data/postgresql.conf
pg_ctl start -D /var/lib/postgresql/data

sh