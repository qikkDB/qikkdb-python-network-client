# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message/InfoMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Message/InfoMessage.proto',
  package='QikkDB.NetworkClient.Message',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19Message/InfoMessage.proto\x12\x1cQikkDB.NetworkClient.Message\"\xec\x01\n\x0bInfoMessage\x12\x42\n\x04\x43ode\x18\x01 \x01(\x0e\x32\x34.QikkDB.NetworkClient.Message.InfoMessage.StatusCode\x12\x0f\n\x07Message\x18\x02 \x01(\t\"\x87\x01\n\nStatusCode\x12\x06\n\x02OK\x10\x00\x12\x08\n\x04WAIT\x10\x01\x12\x13\n\x0fGET_NEXT_RESULT\x10\x06\x12\x0f\n\x0bQUERY_ERROR\x10\x02\x12\x10\n\x0cIMPORT_ERROR\x10\x03\x12\x12\n\x0e\x43ONN_ESTABLISH\x10\x04\x12\x0c\n\x08\x43ONN_END\x10\x05\x12\r\n\tHEARTBEAT\x10\x07\x62\x06proto3'
)



_INFOMESSAGE_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='QikkDB.NetworkClient.Message.InfoMessage.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WAIT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GET_NEXT_RESULT', index=2, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUERY_ERROR', index=3, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IMPORT_ERROR', index=4, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONN_ESTABLISH', index=5, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONN_END', index=6, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HEARTBEAT', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=161,
  serialized_end=296,
)
_sym_db.RegisterEnumDescriptor(_INFOMESSAGE_STATUSCODE)


_INFOMESSAGE = _descriptor.Descriptor(
  name='InfoMessage',
  full_name='QikkDB.NetworkClient.Message.InfoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Code', full_name='QikkDB.NetworkClient.Message.InfoMessage.Code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Message', full_name='QikkDB.NetworkClient.Message.InfoMessage.Message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INFOMESSAGE_STATUSCODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=296,
)

_INFOMESSAGE.fields_by_name['Code'].enum_type = _INFOMESSAGE_STATUSCODE
_INFOMESSAGE_STATUSCODE.containing_type = _INFOMESSAGE
DESCRIPTOR.message_types_by_name['InfoMessage'] = _INFOMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InfoMessage = _reflection.GeneratedProtocolMessageType('InfoMessage', (_message.Message,), {
  'DESCRIPTOR' : _INFOMESSAGE,
  '__module__' : 'Message.InfoMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.InfoMessage)
  })
_sym_db.RegisterMessage(InfoMessage)


# @@protoc_insertion_point(module_scope)
