from fastapi import APIRouter

from app.grpc.client import stub
from app.grpc.generated import helloworld_pb2

router = APIRouter()


@router.get("/{name}")
async def say_hello(name: str):
    response = stub.SayHello.future(helloworld_pb2.HelloRequest(name=name))
    print(response)
    return {"message": name}


@router.get("/check/{name}")
async def say_hello(name: str):
    print(f"here is the name is: {name}")
    return {"message": name}
