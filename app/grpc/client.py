# import grpc
# from app.grpc.generated import helloworld_pb2_grpc
#
# channel = grpc.insecure_channel('localhost:50051')
# stub = helloworld_pb2_grpc.GreeterStub(channel)

import grpc

from app.grpc.generated import helloworld_pb2, helloworld_pb2_grpc


class GRPCClient:
    def __init__(self):
        self.channel = grpc.aio.insecure_channel('localhost:50051')
        self.stub = helloworld_pb2_grpc.GreeterStub(self.channel)

    async def say_hello(self, name: str):
        request = helloworld_pb2.HelloRequest(name=name)
        response = await self.stub.SayHello(request)
        return response.message


grpc_client = GRPCClient()
