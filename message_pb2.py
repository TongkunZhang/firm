# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='interaction',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmessage.proto\x12\x0binteraction\"^\n\x0fToServerMessage\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04node\x18\x02 \x02(\t\x12\n\n\x02id\x18\x03 \x02(\t\x12#\n\x06\x61\x63tion\x18\x04 \x02(\x0b\x32\x13.interaction.Action\"\xb2\x01\n\x0fToClientMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04node\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x02(\t\x12!\n\x05usage\x18\x04 \x02(\x0b\x32\x12.interaction.Usage\x12!\n\x05limit\x18\x05 \x02(\x0b\x32\x12.interaction.Limit\x12!\n\x05other\x18\x06 \x02(\x0b\x32\x12.interaction.Other\x12\x0e\n\x06status\x18\x07 \x02(\t\"5\n\x0b\x43omponentId\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04node\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x02(\t\"O\n\x06\x41\x63tion\x12\x0b\n\x03\x63pu\x18\x01 \x02(\x05\x12\x0e\n\x06memory\x18\x02 \x02(\x05\x12\x0b\n\x03llc\x18\x03 \x02(\x05\x12\n\n\x02io\x18\x04 \x02(\x05\x12\x0f\n\x07network\x18\x05 \x02(\x05\"N\n\x05Limit\x12\x0b\n\x03\x63pu\x18\x01 \x02(\x05\x12\x0e\n\x06memory\x18\x02 \x02(\x05\x12\x0b\n\x03llc\x18\x03 \x02(\x05\x12\n\n\x02io\x18\x04 \x02(\x05\x12\x0f\n\x07network\x18\x05 \x02(\x05\"N\n\x05Usage\x12\x0b\n\x03\x63pu\x18\x01 \x02(\x05\x12\x0e\n\x06memory\x18\x02 \x02(\x05\x12\x0b\n\x03llc\x18\x03 \x02(\x05\x12\n\n\x02io\x18\x04 \x02(\x05\x12\x0f\n\x07network\x18\x05 \x02(\x05\"c\n\x05Other\x12\x16\n\x0eslo_retainment\x18\x01 \x02(\x02\x12\x19\n\x11\x63urr_arrival_rate\x18\x02 \x02(\x05\x12\x12\n\nrate_ratio\x18\x03 \x02(\x02\x12\x13\n\x0bpercentages\x18\x04 \x03(\x02\x32\xa2\x01\n\x0bInteraction\x12\x44\n\x08GetState\x12\x18.interaction.ComponentId\x1a\x1c.interaction.ToClientMessage\"\x00\x12M\n\rPerformAction\x12\x1c.interaction.ToServerMessage\x1a\x1c.interaction.ToClientMessage\"\x00'
)




_TOSERVERMESSAGE = _descriptor.Descriptor(
  name='ToServerMessage',
  full_name='interaction.ToServerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='interaction.ToServerMessage.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node', full_name='interaction.ToServerMessage.node', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='interaction.ToServerMessage.id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='interaction.ToServerMessage.action', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=124,
)


_TOCLIENTMESSAGE = _descriptor.Descriptor(
  name='ToClientMessage',
  full_name='interaction.ToClientMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='interaction.ToClientMessage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node', full_name='interaction.ToClientMessage.node', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='interaction.ToClientMessage.id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='usage', full_name='interaction.ToClientMessage.usage', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='interaction.ToClientMessage.limit', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='other', full_name='interaction.ToClientMessage.other', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='interaction.ToClientMessage.status', index=6,
      number=7, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=305,
)


_COMPONENTID = _descriptor.Descriptor(
  name='ComponentId',
  full_name='interaction.ComponentId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='interaction.ComponentId.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node', full_name='interaction.ComponentId.node', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='interaction.ComponentId.id', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=360,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='interaction.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu', full_name='interaction.Action.cpu', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory', full_name='interaction.Action.memory', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='llc', full_name='interaction.Action.llc', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='io', full_name='interaction.Action.io', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network', full_name='interaction.Action.network', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=441,
)


_LIMIT = _descriptor.Descriptor(
  name='Limit',
  full_name='interaction.Limit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu', full_name='interaction.Limit.cpu', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory', full_name='interaction.Limit.memory', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='llc', full_name='interaction.Limit.llc', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='io', full_name='interaction.Limit.io', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network', full_name='interaction.Limit.network', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=443,
  serialized_end=521,
)


_USAGE = _descriptor.Descriptor(
  name='Usage',
  full_name='interaction.Usage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu', full_name='interaction.Usage.cpu', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory', full_name='interaction.Usage.memory', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='llc', full_name='interaction.Usage.llc', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='io', full_name='interaction.Usage.io', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network', full_name='interaction.Usage.network', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=523,
  serialized_end=601,
)


_OTHER = _descriptor.Descriptor(
  name='Other',
  full_name='interaction.Other',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='slo_retainment', full_name='interaction.Other.slo_retainment', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='curr_arrival_rate', full_name='interaction.Other.curr_arrival_rate', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_ratio', full_name='interaction.Other.rate_ratio', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='percentages', full_name='interaction.Other.percentages', index=3,
      number=4, type=2, cpp_type=6, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=702,
)

_TOSERVERMESSAGE.fields_by_name['action'].message_type = _ACTION
_TOCLIENTMESSAGE.fields_by_name['usage'].message_type = _USAGE
_TOCLIENTMESSAGE.fields_by_name['limit'].message_type = _LIMIT
_TOCLIENTMESSAGE.fields_by_name['other'].message_type = _OTHER
DESCRIPTOR.message_types_by_name['ToServerMessage'] = _TOSERVERMESSAGE
DESCRIPTOR.message_types_by_name['ToClientMessage'] = _TOCLIENTMESSAGE
DESCRIPTOR.message_types_by_name['ComponentId'] = _COMPONENTID
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['Limit'] = _LIMIT
DESCRIPTOR.message_types_by_name['Usage'] = _USAGE
DESCRIPTOR.message_types_by_name['Other'] = _OTHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ToServerMessage = _reflection.GeneratedProtocolMessageType('ToServerMessage', (_message.Message,), {
  'DESCRIPTOR' : _TOSERVERMESSAGE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:interaction.ToServerMessage)
  })
_sym_db.RegisterMessage(ToServerMessage)

ToClientMessage = _reflection.GeneratedProtocolMessageType('ToClientMessage', (_message.Message,), {
  'DESCRIPTOR' : _TOCLIENTMESSAGE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:interaction.ToClientMessage)
  })
_sym_db.RegisterMessage(ToClientMessage)

ComponentId = _reflection.GeneratedProtocolMessageType('ComponentId', (_message.Message,), {
  'DESCRIPTOR' : _COMPONENTID,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:interaction.ComponentId)
  })
_sym_db.RegisterMessage(ComponentId)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:interaction.Action)
  })
_sym_db.RegisterMessage(Action)

Limit = _reflection.GeneratedProtocolMessageType('Limit', (_message.Message,), {
  'DESCRIPTOR' : _LIMIT,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:interaction.Limit)
  })
_sym_db.RegisterMessage(Limit)

Usage = _reflection.GeneratedProtocolMessageType('Usage', (_message.Message,), {
  'DESCRIPTOR' : _USAGE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:interaction.Usage)
  })
_sym_db.RegisterMessage(Usage)

Other = _reflection.GeneratedProtocolMessageType('Other', (_message.Message,), {
  'DESCRIPTOR' : _OTHER,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:interaction.Other)
  })
_sym_db.RegisterMessage(Other)



_INTERACTION = _descriptor.ServiceDescriptor(
  name='Interaction',
  full_name='interaction.Interaction',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=705,
  serialized_end=867,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetState',
    full_name='interaction.Interaction.GetState',
    index=0,
    containing_service=None,
    input_type=_COMPONENTID,
    output_type=_TOCLIENTMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PerformAction',
    full_name='interaction.Interaction.PerformAction',
    index=1,
    containing_service=None,
    input_type=_TOSERVERMESSAGE,
    output_type=_TOCLIENTMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_INTERACTION)

DESCRIPTOR.services_by_name['Interaction'] = _INTERACTION

# @@protoc_insertion_point(module_scope)
