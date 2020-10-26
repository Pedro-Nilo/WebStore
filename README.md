# WebStore API Demo

RESTFul API demo simulating a web store. Contains CRUD operations for customers, products and orders.

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
