# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Types/Point.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Types import ComplexPolygon_pb2 as Types_dot_ComplexPolygon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Types/Point.proto',
  package='QikkDB.Types',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11Types/Point.proto\x12\x0cQikkDB.Types\x1a\x1aTypes/ComplexPolygon.proto\"1\n\x05Point\x12(\n\x08geoPoint\x18\x01 \x01(\x0b\x32\x16.QikkDB.Types.GeoPointb\x06proto3'
  ,
  dependencies=[Types_dot_ComplexPolygon__pb2.DESCRIPTOR,])




_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='QikkDB.Types.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='geoPoint', full_name='QikkDB.Types.Point.geoPoint', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=63,
  serialized_end=112,
)

_POINT.fields_by_name['geoPoint'].message_type = Types_dot_ComplexPolygon__pb2._GEOPOINT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'Types.Point_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.Types.Point)
  })
_sym_db.RegisterMessage(Point)


# @@protoc_insertion_point(module_scope)