import grpc
from app.grpc.generated import helloworld_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = helloworld_pb2_grpc.GreeterStub(channel)