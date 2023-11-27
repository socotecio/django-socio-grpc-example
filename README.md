# django-socio-grpc-example

Simple, but comprehensive examples of how to use (Django Socio Grpc (DSG))[https://github.com/socotecio/django-socio-grpc]

This example uses a simple django bibliography app to illustrate the following concepts:

* automatic generation of proto files from django models
* serialisation of UUID primary key fields
* serialization of different field types (char, integer, float, boolean, date)
* serialisation of foreign key fields
* serialisation of many-to-many fields
* Custom gRPC commands with @action decorator
* Filtersets
* connection to django in asynchronous mode


The example is completely containerised, and can be run with docker-compose.




## how to run the backend example

### with docker-compose

```bash
docker-compose up --build

docker compose exec dsg-example-grpc ./manage.py migrate

# TODO load data

docker compose exec dsg-example-grpc python bib_example_client.py
docker compose exec dsg-example-grpc python bib_example_filter_client.py

```

### locally, without docker-compose

```bash
# create a virtual environment
python3 -m venv dsg-example
source dsg-example/bin/activate

# install dependencies
pip install poetry
cd backend
poetry install

# create the database
python manage.py makemigrations example_bib_app
python manage.py migrate

# create a superuser
python manage.py createsuperuser


# create the proto files
python manage.py generateproto


# start the django development web server
python manage.py runserver


# start the gRPC server
python manage.py grpcrunaioserver
```

to visit the django admin page, go to http://localhost:8000/admin

### run the gPRC client

```bash

```



## how to run the frontend example

### with docker-compose

```bash
docker-compose up --build

docker compose exec dsg-example-grpc ./manage.py migrate

# TODO load data
```

Go to http://localhost:5173 and create elements



## how to update the js file when API update

Best practice want you to generate API in a separate repository or use BSR (Buf Schema Registry) to generate client and API for language. But for helping the understanding of how it work we simplified it to help everyone understand.

Doc are coming to explain the step for the grpc web example

```
cp backend/example_bib_app/grpc/*.proto frontend/grpc-web-example/proto/

docker compose exec dsg-example-front npx buf generate proto
```

npx: Execute package binary
buf: Package binary used to generate js file
generate: command of the buf cli
proto: directory where to find the .proto file

This command should be executed where the buf.gen.yaml file is.

This command generate src/gen/example_bib_app_pb.js file