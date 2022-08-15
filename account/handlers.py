from .services import UserService

from account_proto import account_pb2_grpc


def grpc_handlers(server):
    account_pb2_grpc.add_UserControllerServicer_to_server(
        UserService.as_servicer(), server
    )
