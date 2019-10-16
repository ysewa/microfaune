import microfaune_pb2_grpc
import microfaune_pb2

class MicrofauneServicer(microfaune_pb2_grpc.MicrofauneServicer):

    def SayHello(self, request, context):
        logging.info("SayHello calling...")
        return microfaune_pb2.HelloReply(message='Hello, %s!' % request.name)
