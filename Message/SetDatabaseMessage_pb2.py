# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message/SetDatabaseMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Message/SetDatabaseMessage.proto',
  package='QikkDB.NetworkClient.Message',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n Message/SetDatabaseMessage.proto\x12\x1cQikkDB.NetworkClient.Message\"*\n\x12SetDatabaseMessage\x12\x14\n\x0c\x44\x61tabaseName\x18\x01 \x01(\tb\x06proto3'
)




_SETDATABASEMESSAGE = _descriptor.Descriptor(
  name='SetDatabaseMessage',
  full_name='QikkDB.NetworkClient.Message.SetDatabaseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DatabaseName', full_name='QikkDB.NetworkClient.Message.SetDatabaseMessage.DatabaseName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=66,
  serialized_end=108,
)

DESCRIPTOR.message_types_by_name['SetDatabaseMessage'] = _SETDATABASEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetDatabaseMessage = _reflection.GeneratedProtocolMessageType('SetDatabaseMessage', (_message.Message,), {
  'DESCRIPTOR' : _SETDATABASEMESSAGE,
  '__module__' : 'Message.SetDatabaseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.SetDatabaseMessage)
  })
_sym_db.RegisterMessage(SetDatabaseMessage)


# @@protoc_insertion_point(module_scope)