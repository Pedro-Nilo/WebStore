# WebStore API Demo

RESTFul API demo simulating a web store. Contains CRUD operations for customers, products and orders.

## Database Diagram

To represent the user, product and order relationship, I elaborated the following diagram:

![alt text](https://github.com/Pedro-Nilo/WebStore/blob/main/resources/database_uml.png?raw=true)

Note that it includes the auxiliary table of order items to enable the inclusion of an order with multiple items.

## API Documentation

For the sake of simplicity, I generated the API documentation on Postman, since I used it for unit testing of it. I posted it in:

<https://documenter.getpostman.com/view/13226741/TVYGbHZP>

With time and for an on-premises implementation API, probably the best approach would be to use the swagger, but as it was basic, I followed that approach.

## Running on Docker enviroment

To running this project on Docker environment you will needs [Docker](https://www.docker.com/) v19.03.8+ and [Docker-Compose](https://docs.docker.com/compose/) v1.25.5+.

To clone project :

```sh
$ git clone https://github.com/Pedro-Nilo/WebStore.git
```

To generate webstore image, run this command from inside of cloned directory:

```sh
$ docker build -f ./Dockerfile -t webstore:1.0 .
```

After build image, to up containers ecosystem, run this command:

```sh
$ docker-compose -f ./docker-compose.yml up -d --build
```
