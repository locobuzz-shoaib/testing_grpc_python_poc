# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fibonacci.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x66ibonacci.proto\x12\tfibonacci\"\"\n\x10\x46ibonacciRequest\x12\x0e\n\x06number\x18\x01 \x01(\x05\"%\n\x11\x46ibonacciResponse\x12\x10\n\x08sequence\x18\x01 \x03(\x05\x32U\n\tFibonacci\x12H\n\tCalculate\x12\x1b.fibonacci.FibonacciRequest\x1a\x1c.fibonacci.FibonacciResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fibonacci_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FIBONACCIREQUEST']._serialized_start=30
  _globals['_FIBONACCIREQUEST']._serialized_end=64
  _globals['_FIBONACCIRESPONSE']._serialized_start=66
  _globals['_FIBONACCIRESPONSE']._serialized_end=103
  _globals['_FIBONACCI']._serialized_start=105
  _globals['_FIBONACCI']._serialized_end=190
# @@protoc_insertion_point(module_scope)
