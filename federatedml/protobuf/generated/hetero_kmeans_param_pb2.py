# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hetero-kmeans-param.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hetero-kmeans-param.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=_b('B\025KmeansModelParamProto'),
  serialized_pb=_b('\n\x19hetero-kmeans-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"B\n\x10KmeansModelParam\x12\r\n\x05iters\x18\x01 \x01(\x05\x12\x14\n\x0cis_converged\x18\x02 \x01(\x05\x12\t\n\x01k\x18\x03 \x01(\x05\x42\x17\x42\x15KmeansModelParamProtob\x06proto3')
)




_KMEANSMODELPARAM = _descriptor.Descriptor(
  name='KmeansModelParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.KmeansModelParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iters', full_name='com.webank.ai.fate.core.mlmodel.buffer.KmeansModelParam.iters', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_converged', full_name='com.webank.ai.fate.core.mlmodel.buffer.KmeansModelParam.is_converged', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k', full_name='com.webank.ai.fate.core.mlmodel.buffer.KmeansModelParam.k', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=135,
)

DESCRIPTOR.message_types_by_name['KmeansModelParam'] = _KMEANSMODELPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KmeansModelParam = _reflection.GeneratedProtocolMessageType('KmeansModelParam', (_message.Message,), {
  'DESCRIPTOR' : _KMEANSMODELPARAM,
  '__module__' : 'hetero_kmeans_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.KmeansModelParam)
  })
_sym_db.RegisterMessage(KmeansModelParam)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
