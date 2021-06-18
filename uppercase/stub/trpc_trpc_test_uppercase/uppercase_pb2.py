# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uppercase.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='uppercase.proto',
  package='trpc.trpc_test.uppercase',
  syntax='proto3',
  serialized_options=b'\n6com.tencent.trpcprotocol.trpc_test.uppercase.uppercaseB\tuppercaseP\000Z0git.code.oa.com/trpcprotocol/trpc_test/uppercase',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fuppercase.proto\x12\x18trpc.trpc_test.uppercase\"\x1e\n\x07Request\x12\x13\n\x0blowerString\x18\x01 \x01(\t\"\x1c\n\x05Reply\x12\x13\n\x0bupperString\x18\x01 \x01(\t2Z\n\tUppercase\x12M\n\x07\x63onvert\x12!.trpc.trpc_test.uppercase.Request\x1a\x1f.trpc.trpc_test.uppercase.ReplyBw\n6com.tencent.trpcprotocol.trpc_test.uppercase.uppercaseB\tuppercaseP\x00Z0git.code.oa.com/trpcprotocol/trpc_test/uppercaseb\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='trpc.trpc_test.uppercase.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lowerString', full_name='trpc.trpc_test.uppercase.Request.lowerString', index=0,
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
  serialized_start=45,
  serialized_end=75,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='trpc.trpc_test.uppercase.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='upperString', full_name='trpc.trpc_test.uppercase.Reply.upperString', index=0,
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
  serialized_start=77,
  serialized_end=105,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'uppercase_pb2'
  # @@protoc_insertion_point(class_scope:trpc.trpc_test.uppercase.Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'uppercase_pb2'
  # @@protoc_insertion_point(class_scope:trpc.trpc_test.uppercase.Reply)
  })
_sym_db.RegisterMessage(Reply)


DESCRIPTOR._options = None

_UPPERCASE = _descriptor.ServiceDescriptor(
  name='Uppercase',
  full_name='trpc.trpc_test.uppercase.Uppercase',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=107,
  serialized_end=197,
  methods=[
  _descriptor.MethodDescriptor(
    name='convert',
    full_name='trpc.trpc_test.uppercase.Uppercase.convert',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_REPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_UPPERCASE)

DESCRIPTOR.services_by_name['Uppercase'] = _UPPERCASE

# @@protoc_insertion_point(module_scope)
