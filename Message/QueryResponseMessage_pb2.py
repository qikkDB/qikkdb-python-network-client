# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message/QueryResponseMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Types import ComplexPolygon_pb2 as Types_dot_ComplexPolygon__pb2
from Types import Point_pb2 as Types_dot_Point__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Message/QueryResponseMessage.proto',
  package='QikkDB.NetworkClient.Message',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"Message/QueryResponseMessage.proto\x12\x1cQikkDB.NetworkClient.Message\x1a\x1aTypes/ComplexPolygon.proto\x1a\x11Types/Point.proto\"*\n\x17QueryResponseIntPayload\x12\x0f\n\x07intData\x18\x01 \x03(\x05\".\n\x19QueryResponseInt64Payload\x12\x11\n\tint64Data\x18\x01 \x03(\x03\"4\n\x1cQueryResponseDateTimePayload\x12\x14\n\x0c\x64\x61teTimeData\x18\x01 \x03(\x03\".\n\x19QueryResponseFloatPayload\x12\x11\n\tfloatData\x18\x01 \x03(\x02\"0\n\x1aQueryResponseDoublePayload\x12\x12\n\ndoubleData\x18\x01 \x03(\x01\"P\n\x1bQueryResponsePolygonPayload\x12\x31\n\x0bpolygonData\x18\x01 \x03(\x0b\x32\x1c.QikkDB.Types.ComplexPolygon\"C\n\x19QueryResponsePointPayload\x12&\n\tpointData\x18\x01 \x03(\x0b\x32\x13.QikkDB.Types.Point\"0\n\x1aQueryResponseStringPayload\x12\x12\n\nstringData\x18\x01 \x03(\t\"(\n\x14QueryNullmaskPayload\x12\x10\n\x08nullMask\x18\x01 \x03(\x04\"\xb3\x05\n\x14QueryResponsePayload\x12K\n\nintPayload\x18\x02 \x01(\x0b\x32\x35.QikkDB.NetworkClient.Message.QueryResponseIntPayloadH\x00\x12O\n\x0c\x66loatPayload\x18\x03 \x01(\x0b\x32\x37.QikkDB.NetworkClient.Message.QueryResponseFloatPayloadH\x00\x12O\n\x0cint64Payload\x18\x04 \x01(\x0b\x32\x37.QikkDB.NetworkClient.Message.QueryResponseInt64PayloadH\x00\x12Q\n\rdoublePayload\x18\x05 \x01(\x0b\x32\x38.QikkDB.NetworkClient.Message.QueryResponseDoublePayloadH\x00\x12O\n\x0cpointPayload\x18\x06 \x01(\x0b\x32\x37.QikkDB.NetworkClient.Message.QueryResponsePointPayloadH\x00\x12S\n\x0epolygonPayload\x18\x07 \x01(\x0b\x32\x39.QikkDB.NetworkClient.Message.QueryResponsePolygonPayloadH\x00\x12Q\n\rstringPayload\x18\x08 \x01(\x0b\x32\x38.QikkDB.NetworkClient.Message.QueryResponseStringPayloadH\x00\x12U\n\x0f\x64\x61teTimePayload\x18\t \x01(\x0b\x32:.QikkDB.NetworkClient.Message.QueryResponseDateTimePayloadH\x00\x42\t\n\x07payload\"\xa8\x04\n\x14QueryResponseMessage\x12R\n\x08payloads\x18\x01 \x03(\x0b\x32@.QikkDB.NetworkClient.Message.QueryResponseMessage.PayloadsEntry\x12Z\n\x0cnullBitMasks\x18\x03 \x03(\x0b\x32\x44.QikkDB.NetworkClient.Message.QueryResponseMessage.NullBitMasksEntry\x12N\n\x06timing\x18\x02 \x03(\x0b\x32>.QikkDB.NetworkClient.Message.QueryResponseMessage.TimingEntry\x12\x13\n\x0b\x63olumnOrder\x18\x04 \x03(\t\x1a\x63\n\rPayloadsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.QikkDB.NetworkClient.Message.QueryResponsePayload:\x02\x38\x01\x1ag\n\x11NullBitMasksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.QikkDB.NetworkClient.Message.QueryNullmaskPayload:\x02\x38\x01\x1a-\n\x0bTimingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x62\x06proto3'
  ,
  dependencies=[Types_dot_ComplexPolygon__pb2.DESCRIPTOR,Types_dot_Point__pb2.DESCRIPTOR,])




_QUERYRESPONSEINTPAYLOAD = _descriptor.Descriptor(
  name='QueryResponseIntPayload',
  full_name='QikkDB.NetworkClient.Message.QueryResponseIntPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='intData', full_name='QikkDB.NetworkClient.Message.QueryResponseIntPayload.intData', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=115,
  serialized_end=157,
)


_QUERYRESPONSEINT64PAYLOAD = _descriptor.Descriptor(
  name='QueryResponseInt64Payload',
  full_name='QikkDB.NetworkClient.Message.QueryResponseInt64Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='int64Data', full_name='QikkDB.NetworkClient.Message.QueryResponseInt64Payload.int64Data', index=0,
      number=1, type=3, cpp_type=2, label=3,
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
  serialized_start=159,
  serialized_end=205,
)


_QUERYRESPONSEDATETIMEPAYLOAD = _descriptor.Descriptor(
  name='QueryResponseDateTimePayload',
  full_name='QikkDB.NetworkClient.Message.QueryResponseDateTimePayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dateTimeData', full_name='QikkDB.NetworkClient.Message.QueryResponseDateTimePayload.dateTimeData', index=0,
      number=1, type=3, cpp_type=2, label=3,
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
  serialized_start=207,
  serialized_end=259,
)


_QUERYRESPONSEFLOATPAYLOAD = _descriptor.Descriptor(
  name='QueryResponseFloatPayload',
  full_name='QikkDB.NetworkClient.Message.QueryResponseFloatPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='floatData', full_name='QikkDB.NetworkClient.Message.QueryResponseFloatPayload.floatData', index=0,
      number=1, type=2, cpp_type=6, label=3,
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
  serialized_start=261,
  serialized_end=307,
)


_QUERYRESPONSEDOUBLEPAYLOAD = _descriptor.Descriptor(
  name='QueryResponseDoublePayload',
  full_name='QikkDB.NetworkClient.Message.QueryResponseDoublePayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='doubleData', full_name='QikkDB.NetworkClient.Message.QueryResponseDoublePayload.doubleData', index=0,
      number=1, type=1, cpp_type=5, label=3,
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
  serialized_start=309,
  serialized_end=357,
)


_QUERYRESPONSEPOLYGONPAYLOAD = _descriptor.Descriptor(
  name='QueryResponsePolygonPayload',
  full_name='QikkDB.NetworkClient.Message.QueryResponsePolygonPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='polygonData', full_name='QikkDB.NetworkClient.Message.QueryResponsePolygonPayload.polygonData', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=359,
  serialized_end=439,
)


_QUERYRESPONSEPOINTPAYLOAD = _descriptor.Descriptor(
  name='QueryResponsePointPayload',
  full_name='QikkDB.NetworkClient.Message.QueryResponsePointPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pointData', full_name='QikkDB.NetworkClient.Message.QueryResponsePointPayload.pointData', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=441,
  serialized_end=508,
)


_QUERYRESPONSESTRINGPAYLOAD = _descriptor.Descriptor(
  name='QueryResponseStringPayload',
  full_name='QikkDB.NetworkClient.Message.QueryResponseStringPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stringData', full_name='QikkDB.NetworkClient.Message.QueryResponseStringPayload.stringData', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=510,
  serialized_end=558,
)


_QUERYNULLMASKPAYLOAD = _descriptor.Descriptor(
  name='QueryNullmaskPayload',
  full_name='QikkDB.NetworkClient.Message.QueryNullmaskPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nullMask', full_name='QikkDB.NetworkClient.Message.QueryNullmaskPayload.nullMask', index=0,
      number=1, type=4, cpp_type=4, label=3,
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
  serialized_start=560,
  serialized_end=600,
)


_QUERYRESPONSEPAYLOAD = _descriptor.Descriptor(
  name='QueryResponsePayload',
  full_name='QikkDB.NetworkClient.Message.QueryResponsePayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='intPayload', full_name='QikkDB.NetworkClient.Message.QueryResponsePayload.intPayload', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='floatPayload', full_name='QikkDB.NetworkClient.Message.QueryResponsePayload.floatPayload', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64Payload', full_name='QikkDB.NetworkClient.Message.QueryResponsePayload.int64Payload', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doublePayload', full_name='QikkDB.NetworkClient.Message.QueryResponsePayload.doublePayload', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pointPayload', full_name='QikkDB.NetworkClient.Message.QueryResponsePayload.pointPayload', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='polygonPayload', full_name='QikkDB.NetworkClient.Message.QueryResponsePayload.polygonPayload', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stringPayload', full_name='QikkDB.NetworkClient.Message.QueryResponsePayload.stringPayload', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dateTimePayload', full_name='QikkDB.NetworkClient.Message.QueryResponsePayload.dateTimePayload', index=7,
      number=9, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='QikkDB.NetworkClient.Message.QueryResponsePayload.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=603,
  serialized_end=1294,
)


_QUERYRESPONSEMESSAGE_PAYLOADSENTRY = _descriptor.Descriptor(
  name='PayloadsEntry',
  full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.PayloadsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.PayloadsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.PayloadsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1598,
  serialized_end=1697,
)

_QUERYRESPONSEMESSAGE_NULLBITMASKSENTRY = _descriptor.Descriptor(
  name='NullBitMasksEntry',
  full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.NullBitMasksEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.NullBitMasksEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.NullBitMasksEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1699,
  serialized_end=1802,
)

_QUERYRESPONSEMESSAGE_TIMINGENTRY = _descriptor.Descriptor(
  name='TimingEntry',
  full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.TimingEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.TimingEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.TimingEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1804,
  serialized_end=1849,
)

_QUERYRESPONSEMESSAGE = _descriptor.Descriptor(
  name='QueryResponseMessage',
  full_name='QikkDB.NetworkClient.Message.QueryResponseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payloads', full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.payloads', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nullBitMasks', full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.nullBitMasks', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timing', full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.timing', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='columnOrder', full_name='QikkDB.NetworkClient.Message.QueryResponseMessage.columnOrder', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_QUERYRESPONSEMESSAGE_PAYLOADSENTRY, _QUERYRESPONSEMESSAGE_NULLBITMASKSENTRY, _QUERYRESPONSEMESSAGE_TIMINGENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1297,
  serialized_end=1849,
)

_QUERYRESPONSEPOLYGONPAYLOAD.fields_by_name['polygonData'].message_type = Types_dot_ComplexPolygon__pb2._COMPLEXPOLYGON
_QUERYRESPONSEPOINTPAYLOAD.fields_by_name['pointData'].message_type = Types_dot_Point__pb2._POINT
_QUERYRESPONSEPAYLOAD.fields_by_name['intPayload'].message_type = _QUERYRESPONSEINTPAYLOAD
_QUERYRESPONSEPAYLOAD.fields_by_name['floatPayload'].message_type = _QUERYRESPONSEFLOATPAYLOAD
_QUERYRESPONSEPAYLOAD.fields_by_name['int64Payload'].message_type = _QUERYRESPONSEINT64PAYLOAD
_QUERYRESPONSEPAYLOAD.fields_by_name['doublePayload'].message_type = _QUERYRESPONSEDOUBLEPAYLOAD
_QUERYRESPONSEPAYLOAD.fields_by_name['pointPayload'].message_type = _QUERYRESPONSEPOINTPAYLOAD
_QUERYRESPONSEPAYLOAD.fields_by_name['polygonPayload'].message_type = _QUERYRESPONSEPOLYGONPAYLOAD
_QUERYRESPONSEPAYLOAD.fields_by_name['stringPayload'].message_type = _QUERYRESPONSESTRINGPAYLOAD
_QUERYRESPONSEPAYLOAD.fields_by_name['dateTimePayload'].message_type = _QUERYRESPONSEDATETIMEPAYLOAD
_QUERYRESPONSEPAYLOAD.oneofs_by_name['payload'].fields.append(
  _QUERYRESPONSEPAYLOAD.fields_by_name['intPayload'])
_QUERYRESPONSEPAYLOAD.fields_by_name['intPayload'].containing_oneof = _QUERYRESPONSEPAYLOAD.oneofs_by_name['payload']
_QUERYRESPONSEPAYLOAD.oneofs_by_name['payload'].fields.append(
  _QUERYRESPONSEPAYLOAD.fields_by_name['floatPayload'])
_QUERYRESPONSEPAYLOAD.fields_by_name['floatPayload'].containing_oneof = _QUERYRESPONSEPAYLOAD.oneofs_by_name['payload']
_QUERYRESPONSEPAYLOAD.oneofs_by_name['payload'].fields.append(
  _QUERYRESPONSEPAYLOAD.fields_by_name['int64Payload'])
_QUERYRESPONSEPAYLOAD.fields_by_name['int64Payload'].containing_oneof = _QUERYRESPONSEPAYLOAD.oneofs_by_name['payload']
_QUERYRESPONSEPAYLOAD.oneofs_by_name['payload'].fields.append(
  _QUERYRESPONSEPAYLOAD.fields_by_name['doublePayload'])
_QUERYRESPONSEPAYLOAD.fields_by_name['doublePayload'].containing_oneof = _QUERYRESPONSEPAYLOAD.oneofs_by_name['payload']
_QUERYRESPONSEPAYLOAD.oneofs_by_name['payload'].fields.append(
  _QUERYRESPONSEPAYLOAD.fields_by_name['pointPayload'])
_QUERYRESPONSEPAYLOAD.fields_by_name['pointPayload'].containing_oneof = _QUERYRESPONSEPAYLOAD.oneofs_by_name['payload']
_QUERYRESPONSEPAYLOAD.oneofs_by_name['payload'].fields.append(
  _QUERYRESPONSEPAYLOAD.fields_by_name['polygonPayload'])
_QUERYRESPONSEPAYLOAD.fields_by_name['polygonPayload'].containing_oneof = _QUERYRESPONSEPAYLOAD.oneofs_by_name['payload']
_QUERYRESPONSEPAYLOAD.oneofs_by_name['payload'].fields.append(
  _QUERYRESPONSEPAYLOAD.fields_by_name['stringPayload'])
_QUERYRESPONSEPAYLOAD.fields_by_name['stringPayload'].containing_oneof = _QUERYRESPONSEPAYLOAD.oneofs_by_name['payload']
_QUERYRESPONSEPAYLOAD.oneofs_by_name['payload'].fields.append(
  _QUERYRESPONSEPAYLOAD.fields_by_name['dateTimePayload'])
_QUERYRESPONSEPAYLOAD.fields_by_name['dateTimePayload'].containing_oneof = _QUERYRESPONSEPAYLOAD.oneofs_by_name['payload']
_QUERYRESPONSEMESSAGE_PAYLOADSENTRY.fields_by_name['value'].message_type = _QUERYRESPONSEPAYLOAD
_QUERYRESPONSEMESSAGE_PAYLOADSENTRY.containing_type = _QUERYRESPONSEMESSAGE
_QUERYRESPONSEMESSAGE_NULLBITMASKSENTRY.fields_by_name['value'].message_type = _QUERYNULLMASKPAYLOAD
_QUERYRESPONSEMESSAGE_NULLBITMASKSENTRY.containing_type = _QUERYRESPONSEMESSAGE
_QUERYRESPONSEMESSAGE_TIMINGENTRY.containing_type = _QUERYRESPONSEMESSAGE
_QUERYRESPONSEMESSAGE.fields_by_name['payloads'].message_type = _QUERYRESPONSEMESSAGE_PAYLOADSENTRY
_QUERYRESPONSEMESSAGE.fields_by_name['nullBitMasks'].message_type = _QUERYRESPONSEMESSAGE_NULLBITMASKSENTRY
_QUERYRESPONSEMESSAGE.fields_by_name['timing'].message_type = _QUERYRESPONSEMESSAGE_TIMINGENTRY
DESCRIPTOR.message_types_by_name['QueryResponseIntPayload'] = _QUERYRESPONSEINTPAYLOAD
DESCRIPTOR.message_types_by_name['QueryResponseInt64Payload'] = _QUERYRESPONSEINT64PAYLOAD
DESCRIPTOR.message_types_by_name['QueryResponseDateTimePayload'] = _QUERYRESPONSEDATETIMEPAYLOAD
DESCRIPTOR.message_types_by_name['QueryResponseFloatPayload'] = _QUERYRESPONSEFLOATPAYLOAD
DESCRIPTOR.message_types_by_name['QueryResponseDoublePayload'] = _QUERYRESPONSEDOUBLEPAYLOAD
DESCRIPTOR.message_types_by_name['QueryResponsePolygonPayload'] = _QUERYRESPONSEPOLYGONPAYLOAD
DESCRIPTOR.message_types_by_name['QueryResponsePointPayload'] = _QUERYRESPONSEPOINTPAYLOAD
DESCRIPTOR.message_types_by_name['QueryResponseStringPayload'] = _QUERYRESPONSESTRINGPAYLOAD
DESCRIPTOR.message_types_by_name['QueryNullmaskPayload'] = _QUERYNULLMASKPAYLOAD
DESCRIPTOR.message_types_by_name['QueryResponsePayload'] = _QUERYRESPONSEPAYLOAD
DESCRIPTOR.message_types_by_name['QueryResponseMessage'] = _QUERYRESPONSEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryResponseIntPayload = _reflection.GeneratedProtocolMessageType('QueryResponseIntPayload', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSEINTPAYLOAD,
  '__module__' : 'Message.QueryResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponseIntPayload)
  })
_sym_db.RegisterMessage(QueryResponseIntPayload)

QueryResponseInt64Payload = _reflection.GeneratedProtocolMessageType('QueryResponseInt64Payload', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSEINT64PAYLOAD,
  '__module__' : 'Message.QueryResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponseInt64Payload)
  })
_sym_db.RegisterMessage(QueryResponseInt64Payload)

QueryResponseDateTimePayload = _reflection.GeneratedProtocolMessageType('QueryResponseDateTimePayload', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSEDATETIMEPAYLOAD,
  '__module__' : 'Message.QueryResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponseDateTimePayload)
  })
_sym_db.RegisterMessage(QueryResponseDateTimePayload)

QueryResponseFloatPayload = _reflection.GeneratedProtocolMessageType('QueryResponseFloatPayload', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSEFLOATPAYLOAD,
  '__module__' : 'Message.QueryResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponseFloatPayload)
  })
_sym_db.RegisterMessage(QueryResponseFloatPayload)

QueryResponseDoublePayload = _reflection.GeneratedProtocolMessageType('QueryResponseDoublePayload', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSEDOUBLEPAYLOAD,
  '__module__' : 'Message.QueryResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponseDoublePayload)
  })
_sym_db.RegisterMessage(QueryResponseDoublePayload)

QueryResponsePolygonPayload = _reflection.GeneratedProtocolMessageType('QueryResponsePolygonPayload', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSEPOLYGONPAYLOAD,
  '__module__' : 'Message.QueryResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponsePolygonPayload)
  })
_sym_db.RegisterMessage(QueryResponsePolygonPayload)

QueryResponsePointPayload = _reflection.GeneratedProtocolMessageType('QueryResponsePointPayload', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSEPOINTPAYLOAD,
  '__module__' : 'Message.QueryResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponsePointPayload)
  })
_sym_db.RegisterMessage(QueryResponsePointPayload)

QueryResponseStringPayload = _reflection.GeneratedProtocolMessageType('QueryResponseStringPayload', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSESTRINGPAYLOAD,
  '__module__' : 'Message.QueryResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponseStringPayload)
  })
_sym_db.RegisterMessage(QueryResponseStringPayload)

QueryNullmaskPayload = _reflection.GeneratedProtocolMessageType('QueryNullmaskPayload', (_message.Message,), {
  'DESCRIPTOR' : _QUERYNULLMASKPAYLOAD,
  '__module__' : 'Message.QueryResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryNullmaskPayload)
  })
_sym_db.RegisterMessage(QueryNullmaskPayload)

QueryResponsePayload = _reflection.GeneratedProtocolMessageType('QueryResponsePayload', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSEPAYLOAD,
  '__module__' : 'Message.QueryResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponsePayload)
  })
_sym_db.RegisterMessage(QueryResponsePayload)

QueryResponseMessage = _reflection.GeneratedProtocolMessageType('QueryResponseMessage', (_message.Message,), {

  'PayloadsEntry' : _reflection.GeneratedProtocolMessageType('PayloadsEntry', (_message.Message,), {
    'DESCRIPTOR' : _QUERYRESPONSEMESSAGE_PAYLOADSENTRY,
    '__module__' : 'Message.QueryResponseMessage_pb2'
    # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponseMessage.PayloadsEntry)
    })
  ,

  'NullBitMasksEntry' : _reflection.GeneratedProtocolMessageType('NullBitMasksEntry', (_message.Message,), {
    'DESCRIPTOR' : _QUERYRESPONSEMESSAGE_NULLBITMASKSENTRY,
    '__module__' : 'Message.QueryResponseMessage_pb2'
    # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponseMessage.NullBitMasksEntry)
    })
  ,

  'TimingEntry' : _reflection.GeneratedProtocolMessageType('TimingEntry', (_message.Message,), {
    'DESCRIPTOR' : _QUERYRESPONSEMESSAGE_TIMINGENTRY,
    '__module__' : 'Message.QueryResponseMessage_pb2'
    # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponseMessage.TimingEntry)
    })
  ,
  'DESCRIPTOR' : _QUERYRESPONSEMESSAGE,
  '__module__' : 'Message.QueryResponseMessage_pb2'
  # @@protoc_insertion_point(class_scope:QikkDB.NetworkClient.Message.QueryResponseMessage)
  })
_sym_db.RegisterMessage(QueryResponseMessage)
_sym_db.RegisterMessage(QueryResponseMessage.PayloadsEntry)
_sym_db.RegisterMessage(QueryResponseMessage.NullBitMasksEntry)
_sym_db.RegisterMessage(QueryResponseMessage.TimingEntry)


_QUERYRESPONSEMESSAGE_PAYLOADSENTRY._options = None
_QUERYRESPONSEMESSAGE_NULLBITMASKSENTRY._options = None
_QUERYRESPONSEMESSAGE_TIMINGENTRY._options = None
# @@protoc_insertion_point(module_scope)
