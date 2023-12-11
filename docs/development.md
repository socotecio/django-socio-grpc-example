# Development Guide


## gRPC-Web

To develop the gRPC-Web client, you will need the following components:

- envoy proxy
- Django Socio gRPC server (backend)
- vue.js development environment

### Envoy Proxy

In order to develop the gRPC-Web client, you need to run the development envoy proxy. 
This can be done by running the following command from the root of the repository:

```bash
   # build the envoy image
   docker compose -f docker-compose.dev.yaml build
   # run the envoy proxy
   docker compose -f docker-compose.dev.yaml up
``

This will start the envoy proxy on port 9991.


### Django Socio gRPC Server

In order to develop the gRPC-Web client, you need to run the Django Socio gRPC server.
In the backend directory of the repository, run the following command:

```bash
   # run the Django Socio gRPC server
   cd backend
   python manage.py grpcrunaioserver --dev

   # to run the django development server, run the following command
    python manage.py runserver
   
```

### Vue.js Development Environment

To develop the gRPC-Web client, you will need to install the vue.js development environment.
This can be done by running the following command from the root of the repository:

```bash
   # install the vue.js development environment
   cd frontend/grpc-web-example
   npm install
   npm run dev

```
The vite / vue.js development server will show the url to access the gRPC-Web client,
e.g, http://localhost:5173/
