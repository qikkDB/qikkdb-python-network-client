# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message/CSVImportMessage.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Message/CSVImportMessage.proto',
  package='QikkDB.NetworkClient.Message',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eMessage/CSVImportMessage.proto\x12\x1cQikkDB.NetworkClient.Message\"\x87\x01\n\x10\x43SVImportMessage\x12\x14\n\x0c\x44\x61tabaseName\x18\x01 \x01(\t\x12\x0f\n\x07\x43SVName\x18\x02 \x01(\t\x12\x0f\n\x07Payload\x18\x03 \x01(\t\x12;\n\x0b\x43olumnTypes\x18\x04 \x03(\x0e\x32&.QikkDB.NetworkClient.Message.DataType*\xd4\x02\n\x08\x44\x61taType\x12\r\n\tCONST_INT\x10\x00\x12\x18\n\x0b\x43ONST_ERROR\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0e\n\nCONST_LONG\x10\x01\x12\x0f\n\x0b\x43ONST_FLOAT\x10\x02\x12\x10\n\x0c\x43ONST_DOUBLE\x10\x03\x12\x0f\n\x0b\x43ONST_POINT\x10\x04\x12\x11\n\rCONST_POLYGON\x10\x05\x12\x10\n\x0c\x43ONST_STRING\x10\x06\x12\x10\n\x0c\x43ONST_INT8_T\x10\x07\x12\x0e\n\nCOLUMN_INT\x10\x08\x12\x0f\n\x0b\x43OLUMN_LONG\x10\t\x12\x10\n\x0c\x43OLUMN_FLOAT\x10\n\x12\x11\n\rCOLUMN_DOUBLE\x10\x0b\x12\x10\n\x0c\x43OLUMN_POINT\x10\x0c\x12\x12\n\x0e\x43OLUMN_POLYGON\x10\r\x12\x11\n\rCOLUMN_STRING\x10\x0e\x12\x11\n\rCOLUMN_INT8_T\x10\x0f\x12\x12\n\x0e\x44\x41TA_TYPE_SIZE\x10\x10\x62\x06proto3'
)

_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='QikkDB.NetworkClient.Message.DataType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONST_INT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONST_ERROR', index=1, number=-1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONST_LONG', index=2, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONST_FLOAT', index=3, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONST_DOUBLE', index=4, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONST_POINT', index=5, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONST_POLYGON', index=6, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONST_STRING', index=7, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONST_INT8_T', index=8, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COLUMN_INT', index=9, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COLUMN_LONG', index=10, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COLUMN_FLOAT', index=11, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COLUMN_DOUBLE', index=12, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COLUMN_POINT', index=13, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COLUMN_POLYGON', index=14, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COLUMN_STRING', index=15, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COLUMN_INT8_T', index=16, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DATA_TYPE_SIZE', index=17, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=203,
  serialized_end=543,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
CONST_INT = 0
CONST_ERROR = -1
CONST_LONG = 1
CONST_FLOAT = 2
CONST_DOUBLE = 3
CONST_POINT = 4
CONST_POLYGON = 5
CONST_STRING = 6
CONST_INT8_T = 7
COLUMN_INT = 8
COLUMN_LONG = 9
COLUMN_FLOAT = 10
COLUMN_DOUBLE = 11
COLUMN_POINT = 12
COLUMN_POLYGON = 13
COLUMN_STRING = 14
COLUMN_INT8_T = 15
DATA_TYPE_SIZE = 16



_CSVIMPORTMESSAGE = _descriptor.Descriptor(
  name='CSVImportMessage',
  full_name='QikkDB.NetworkClient.Message.CSVImportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DatabaseName', full_name='QikkDB.NetworkClient.Message.CSVImportMessage.DatabaseName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CSVName', full_name='QikkDB.NetworkClient.Message.CSVImportMessage.CSVName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Payload', full_name='QikkDB.NetworkClient.Message.CSVImportMessage.Payload', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ColumnTypes', full_name='QikkDB.NetworkClient.Message.CSVImportMessage.ColumnTypes', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=65,
  serialized_end=200,
)

_CSVIMPORTMESSAGE.fields_by_name['ColumnTypes'].enum_type = _DATATYPE
DESCRIPTOR.message_types_by_name['CSVImportMessage'] = _CSVIMPORTMESSAGE
DESCRIPTOR.enum_types_by_name['DataType'] = _DATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CSVImportMessage = _reflection.GeneratedProtocolMessageType('CSVImportMessage', (_message.Message,), {
  'DESCRIPTOR' : _CSVIMPORTMESSAGE,
  '__module__' : 'Message.CSVImportMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.CSVImportMessage)
  })
_sym_db.RegisterMessage(CSVImportMessage)


# @@protoc_insertion_point(module_scope)