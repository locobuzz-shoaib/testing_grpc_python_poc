###  Below is the project structure
```
fastapi_grpc_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── grpc/
│   │   ├── __init__.py
│   │   ├── services.py
│   │   ├── client.py
│   │   ├── protos/
│   │   │   ├── __init__.py
│   │   │   └── helloworld.proto
│   │   ├── generated/
│   │   │   ├── __init__.py
│   │   │   ├── helloworld_pb2.py
│   │   │   └── helloworld_pb2_grpc.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── endpoints/
│   │       │   ├── __init__.py
│   │       │   └── hello.py
│   │       └── routers.py
├── Dockerfile
├── compile_protos.py
├── requirements.txt
└── README.md
```

