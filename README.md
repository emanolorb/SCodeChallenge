# SCode Challenge
## _The Last API List Formatter, Ever_

### Installation with Docker containers

You will need [`Docker`](https://docs.docker.com/install/) and [`Docker Compose`](https://docs.docker.com/compose/install/) (version 1.25.0 or later) installed in your machine.

#### Generic Docker Compose

1.  Create `.env` file in `/` path, please use the `.env.example`

2.  Build the containers:

```
docker-compose build
```

3.  Run the container:

```
docker-compose up
```


## How to use

Follow  [`http://localhost:8000/`](http://localhost:8000/). to check that the server is working

Go to [`http://localhost:8000/docs`](http://localhost:8000/docs) to test and view documentation

## Plus Ultra

You can also visit [`http://localhost:5050`](http://localhost:5050) to check the data base 
 by adding a server with these credentials:
 
 ```
user: admin@scodechallenge.com
pass: Holi1234#
```
 ```
 Host: db
 port: 5432
 username: postgres
 password: postgres
 role: postgres
 ```


 Powered by
[![Build Status](https://www.codewars.com/users/emanolorb/badges/large)](https://www.codewars.com/users/emanolorb)