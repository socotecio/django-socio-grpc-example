
# Async Example Bibliography


/doc This is an async example app of the django SOCIO gRPC framework (DSG). Describe the overall workflow of the Django Socio gRPC framework example. An Async connection is used in this example. Describe the structure of the app, how the .proto file is generated and how the gRPC service is started. Also describe, how a gRPC client can call a remote procedure.


## Workflow to create a gRPC service

1. Create a django app
2. Create a django model

(3. Create a django viewset)
(4. Create a django filterset)

5. Create a serializer

In the context of the Django SOCIO gRPC framework (DSG), a serializer is responsible for converting complex data types, such as Django models, 
into a format that can be easily transmitted over the network. The DSG serializer is used to serialize and deserialize data between the gRPC client and server. 
It is responsible for converting the data into a format that can be transmitted over the network, and then converting it back into the 
original format on the other end. The DSG serializer is an important component of the framework,
 as it allows for easy communication between the client and server, and ensures that the data is transmitted in a consistent and reliable manner.

To create a serializer, you need to create a file called serializers.py in your app directory. 
This file will contain all of the serializers for your app.
First just create an initial structure for the serializer:

```python
from dsg import serializers
from .models import Book, Author, Publisher

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# [...]        
```

Then create the gRPC services file, named services.py:

```python
```


6. Create handlers for the gRPC services in handlers.py

```python

```

7. add handlers to the settings.py file

```python
# dsg_example/settings.py
...
GRPC_FRAMEWORK = {
    "ROOT_HANDLERS_HOOK" : 'async_example_app.handlers.grpc_handlers',
    ...
}
```


8. Generate the proto file and stubs with the DSG management command:

```bash
python manage.py generateproto
```


9. Add the stubs to the serializers.py file

```python
```



9. Start the gRPC service

```bash
python manage.py grpcrunaioserver --dev
```

10. run the gRPC client

```bash
# this runs the sync client
python bib_example_sync_client.py  
```

```bash
# this runs the async client
python bib_example_async_client.py  
```
