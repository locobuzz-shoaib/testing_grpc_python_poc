from fastapi import APIRouter

from app.grpc.client import grpc_client
# from app.grpc.client import stub
from app.grpc.generated import helloworld_pb2

router = APIRouter()


@router.get("/{name}")
async def say_hello(name: str):
    message = await grpc_client.say_hello(name)
    print(message)
    return {"message": name}


@router.get("/check/{number}")
async def say_hello(number: int):
    num_list = []
    for i in range(10):
        num_list.append(fibonacci_recursive(i))
    return {"response": num_list}


def fibonacci_recursive(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)