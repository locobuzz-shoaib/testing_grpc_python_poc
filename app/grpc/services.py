from concurrent import futures
import grpc
import fibonacci_pb2
import fibonacci_pb2_grpc
import grpc

from app.grpc.generated import helloworld_pb2_grpc, helloworld_pb2


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message=f'Hello, {request.name}!')



class FibonacciServicer(fibonacci_pb2_grpc.FibonacciServicer):
    def Calculate(self, request, context):
        n = request.number
        sequence = self.fibonacci_sequence(n)
        return fibonacci_pb2.FibonacciResponse(sequence=sequence)

    def fibonacci_sequence(self, n):
        if n <= 0:
            return []
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[:n]

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fibonacci_pb2_grpc.add_FibonacciServicer_to_server(FibonacciServicer(), server)
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
