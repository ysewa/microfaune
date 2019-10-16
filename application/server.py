import grpc
import microfaune_pb2_grpc

from .microfaune_servicer import MicrofauneServicer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    microfaune_pb2_grpc.add_Servicer_to_server(MicrofauneServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("Server starts!")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()
