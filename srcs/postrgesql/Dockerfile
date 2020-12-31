FROM    alpine:latest

# install all what i need for up postgresql
RUN     apk update && apk upgrade
RUN     apk add wget vim postgresql openrc supervisor

#RUN adduser -D -g 'postgres' postgres
# create new dir for postgresql pid
RUN     mkdir -p /var/run/postgresql

# change own for the dir, cuz postgresql need it
RUN     chown -R postgres:postgres /var/run/postgresql

VOLUME ["/var/lib"]

COPY    start.sh /
RUN     chmod +x /start.sh

EXPOSE 3306

USER    postgres
CMD     sh start.sh

