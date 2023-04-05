from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4

import grpc
from grpc_reflection.v1alpha import reflection

import logging
import rides_pb2 as pb
import rides_pb2_grpc as rpc

from validate import Error


def new_ride_id():
    return uuid4().hex

class Rides(rpc.RidesServicer):
    def Start(self, request, context):
        logging.info('ride: %r', request)

        try:
            Error.start_request(request)
        except Error as err:
            logging.error('bad request', err)
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return err

if __name__=='__main__':
    import config 


# server = grpc.server(ThreadPoolExecutor())
# rpc.add_RidesServicer_to_server(Rides(), server)


# addr = f'[::]:{config.port}'
# server.add_insecure_port(addr)
# server.start()


# logging.info('server ready on  %s', addr)
# server.wait_for_termination()




server = grpc.server(ThreadPoolExecutor())
rpc.add_RidesServicer_to_server(Rides(), server)
names = (
    pb.DESCRIPTOR.services_by_name['Rides'].full_name,
    reflection.SERVICE_NAME,
)

reflection.enable_server_reflection(names, server)


addr = f'[::]:{config.port}'