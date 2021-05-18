# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import agent_manager_pb2 as src_dot_ray_dot_protobuf_dot_agent__manager__pb2


class AgentManagerServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RegisterAgent = channel.unary_unary(
        '/ray.rpc.AgentManagerService/RegisterAgent',
        request_serializer=src_dot_ray_dot_protobuf_dot_agent__manager__pb2.RegisterAgentRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_agent__manager__pb2.RegisterAgentReply.FromString,
        )


class AgentManagerServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RegisterAgent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AgentManagerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RegisterAgent': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterAgent,
          request_deserializer=src_dot_ray_dot_protobuf_dot_agent__manager__pb2.RegisterAgentRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_agent__manager__pb2.RegisterAgentReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ray.rpc.AgentManagerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
