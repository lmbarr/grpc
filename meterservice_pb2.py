# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meterservice.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12meterservice.proto\x12\x05meter\"b\n\rReadingPacket\x12\'\n\x08Readings\x18\x01 \x03(\x0b\x32\x15.meter.ReadingMessage\x12(\n\nSuccessful\x18\x02 \x01(\x0e\x32\x14.meter.ReadingStatus\"p\n\x0eReadingMessage\x12\x12\n\nCustomerId\x18\x01 \x01(\x05\x12\x14\n\x0cReadingValue\x18\x02 \x01(\x05\x12\r\n\x05Notes\x18\x03 \x01(\t\x12\x13\n\x0bReadingTime\x18\x05 \x01(\tJ\x04\x08\x04\x10\x05R\nSuccessful\"G\n\rStatusMessage\x12%\n\x07Success\x18\x01 \x01(\x0e\x32\x14.meter.ReadingStatus\x12\x0f\n\x07Message\x18\x02 \x01(\t*6\n\rReadingStatus\x12\x0b\n\x07Unknown\x10\x00\x12\x0b\n\x07Success\x10\x01\x12\x0b\n\x07\x46\x61ilure\x10\x02\x32O\n\x13MeterReadingService\x12\x38\n\nAddReading\x12\x14.meter.ReadingPacket\x1a\x14.meter.StatusMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meterservice_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_READINGSTATUS']._serialized_start=316
  _globals['_READINGSTATUS']._serialized_end=370
  _globals['_READINGPACKET']._serialized_start=29
  _globals['_READINGPACKET']._serialized_end=127
  _globals['_READINGMESSAGE']._serialized_start=129
  _globals['_READINGMESSAGE']._serialized_end=241
  _globals['_STATUSMESSAGE']._serialized_start=243
  _globals['_STATUSMESSAGE']._serialized_end=314
  _globals['_METERREADINGSERVICE']._serialized_start=372
  _globals['_METERREADINGSERVICE']._serialized_end=451
# @@protoc_insertion_point(module_scope)
