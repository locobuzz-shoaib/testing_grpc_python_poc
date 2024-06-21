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

## Protocol Buffers Role in gRPC
- Protocol Buffers is used to define the:
  - Messages (data Request and Response)
  - Service (Service name and RPC endpoints)


## Efficiency of Protocol Buffers over JSON
- gRPC uses Protocol Buffers for communications
  - Let's measure the payload size vs JSOn
    ```json
    {
    "age": 35,
    "first_name":  "Stephane",
    "last_name": "Marek"
    }
    ```
  - JSON of size 55 bytes
  - Protocol Buffers of size 20 bytes
    - ```protobuf
        message Person {
            string first_name = 1;
            string last_name = 2;
            int32 age = 3;
        }
        ```
  - Protocol Buffers is 2.75 times smaller than JSON
  - We save in Network Bandwidth
  - Parsing JSON is actually <code style="color" : red>**CPU intensive**</code> (because the format is human readable)
  - Parsing Protocol Buffers (binary format) is **less CPU intensive** because it's closer to how a machine represent data. 
  - By using gRPC, the use of Protocol Buffers means **faster** and more **efficient** communications, friendly with mobile devices that have a slower CPU.

## gRPC Lnaguages
- gRPC will have these main implementations
  - GRPC-JAVA: Pure implementation of gRPC in Java.
  - GRPC-GO: Pure implementation in gRPC in Go.
  - GRPC-C: Pure Implementation of gRPC in C
    - gRPC-C++: C++ wrapper around gRPC-C
    - gRPC-C#: C# wrapper around gRPC-C
    - gRPC-Python: Python wrapper around gRPC-C
    - gRPC-Ruby: Ruby wrapper around gRPC-C
    - Objective-C: Objective-C wrapper around gRPC-C
    - PHP: PHP wrapper around gRPC-C
- Other languages implement gRPC natively or rely on C implementation

## gRPC can be used by any language
- Because the code can be generated for any language, it makes it super simple to create micro-services in any language that interact with each other.

