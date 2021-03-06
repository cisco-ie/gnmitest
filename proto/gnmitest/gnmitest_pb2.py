# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/gnmitest/gnmitest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.openconfig.gnmitest.proto.suite import suite_pb2 as github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_suite_dot_suite__pb2
from github.com.openconfig.gnmitest.proto.report import report_pb2 as github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_report_dot_report__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/gnmitest/gnmitest.proto',
  package='gnmitest',
  syntax='proto3',
  serialized_pb=_b('\n\x1dproto/gnmitest/gnmitest.proto\x12\x08gnmitest\x1a\x36github.com/openconfig/gnmitest/proto/suite/suite.proto\x1a\x38github.com/openconfig/gnmitest/proto/report/report.proto2/\n\x08GNMITest\x12#\n\x03Run\x12\x0c.suite.Suite\x1a\x0e.report.Reportb\x06proto3')
  ,
  dependencies=[github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_suite_dot_suite__pb2.DESCRIPTOR,github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_report_dot_report__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class GNMITestStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Run = channel.unary_unary(
          '/gnmitest.GNMITest/Run',
          request_serializer=github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_suite_dot_suite__pb2.Suite.SerializeToString,
          response_deserializer=github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_report_dot_report__pb2.Report.FromString,
          )


  class GNMITestServicer(object):

    def Run(self, request, context):
      """Run runs the given Suite proto and returns Report proto.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_GNMITestServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Run': grpc.unary_unary_rpc_method_handler(
            servicer.Run,
            request_deserializer=github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_suite_dot_suite__pb2.Suite.FromString,
            response_serializer=github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_report_dot_report__pb2.Report.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'gnmitest.GNMITest', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaGNMITestServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Run(self, request, context):
      """Run runs the given Suite proto and returns Report proto.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaGNMITestStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Run(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Run runs the given Suite proto and returns Report proto.
      """
      raise NotImplementedError()
    Run.future = None


  def beta_create_GNMITest_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('gnmitest.GNMITest', 'Run'): github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_suite_dot_suite__pb2.Suite.FromString,
    }
    response_serializers = {
      ('gnmitest.GNMITest', 'Run'): github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_report_dot_report__pb2.Report.SerializeToString,
    }
    method_implementations = {
      ('gnmitest.GNMITest', 'Run'): face_utilities.unary_unary_inline(servicer.Run),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_GNMITest_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('gnmitest.GNMITest', 'Run'): github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_suite_dot_suite__pb2.Suite.SerializeToString,
    }
    response_deserializers = {
      ('gnmitest.GNMITest', 'Run'): github_dot_com_dot_openconfig_dot_gnmitest_dot_proto_dot_report_dot_report__pb2.Report.FromString,
    }
    cardinalities = {
      'Run': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'gnmitest.GNMITest', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
