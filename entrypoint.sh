#!/bin/bash

echo "Initializing application"

export DATABASE_URL="$DBPROVIDER://$DBUSR:$DBPSW@$DBHOST:$DBPORT/$DBNAME"


if [[ -z $DBNAME ]]
then
  echo "DATABASE evironment is undefined"
else
  echo "Waiting for $DBNAME..."

  while ! nc -z $DBHOST $DBPORT; do
    sleep 0.1
  done

  echo "Database is up and running"

  echo "Update the database tables..."
  flask db upgrade
  echo "Tables updated"
fi

exec "$@"