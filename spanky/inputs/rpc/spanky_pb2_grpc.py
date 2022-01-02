# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from spanky.inputs.rpc import spanky_pb2 as spanky_dot_inputs_dot_rpc_dot_spanky__pb2


class SpankyStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.ExposeMethods = channel.unary_unary(
            "/spanky.Spanky/ExposeMethods",
            request_serializer=spanky_dot_inputs_dot_rpc_dot_spanky__pb2.NewCli.SerializeToString,
            response_deserializer=spanky_dot_inputs_dot_rpc_dot_spanky__pb2.AckCli.FromString,
        )
        self.DoWork = channel.stream_stream(
            "/spanky.Spanky/DoWork",
            request_serializer=spanky_dot_inputs_dot_rpc_dot_spanky__pb2.WorkRequest.SerializeToString,
            response_deserializer=spanky_dot_inputs_dot_rpc_dot_spanky__pb2.WorkRequest.FromString,
        )


class SpankyServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def ExposeMethods(self, request, context):
        """When a client connects it exposes methods that the server can call"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DoWork(self, request_iterator, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SpankyServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ExposeMethods": grpc.unary_unary_rpc_method_handler(
            servicer.ExposeMethods,
            request_deserializer=spanky_dot_inputs_dot_rpc_dot_spanky__pb2.NewCli.FromString,
            response_serializer=spanky_dot_inputs_dot_rpc_dot_spanky__pb2.AckCli.SerializeToString,
        ),
        "DoWork": grpc.stream_stream_rpc_method_handler(
            servicer.DoWork,
            request_deserializer=spanky_dot_inputs_dot_rpc_dot_spanky__pb2.WorkRequest.FromString,
            response_serializer=spanky_dot_inputs_dot_rpc_dot_spanky__pb2.WorkRequest.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "spanky.Spanky", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
