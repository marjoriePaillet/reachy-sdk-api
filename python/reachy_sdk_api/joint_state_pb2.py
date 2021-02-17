# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: joint_state.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='joint_state.proto',
  package='reachy.sdk.joint',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11joint_state.proto\x12\x10reachy.sdk.joint\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xe1\x03\n\nJointState\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x10present_position\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x32\n\rpresent_speed\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x31\n\x0cpresent_load\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x30\n\x0btemperature\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12-\n\tcompliant\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\rgoal_position\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x30\n\x0bspeed_limit\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x31\n\x0ctorque_limit\x18\r \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12-\n\ttimestamp\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1b\n\nJointNames\x12\r\n\x05names\x18\x01 \x03(\t\"m\n\x0e\x41llJointsState\x12,\n\x06joints\x18\x01 \x03(\x0b\x32\x1c.reachy.sdk.joint.JointState\x12-\n\ttimestamp\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x88\x01\n\x0cJointRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12;\n\x10requested_fields\x18\x02 \x03(\x0e\x32!.reachy.sdk.joint.JointStateField\x12-\n\ttimestamp\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"~\n\x10\x41llJointsRequest\x12;\n\x10requested_fields\x18\x02 \x03(\x0e\x32!.reachy.sdk.joint.JointStateField\x12-\n\ttimestamp\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x9f\x01\n\x16StreamAllJointsRequest\x12;\n\x10requested_fields\x18\x02 \x03(\x0e\x32!.reachy.sdk.joint.JointStateField\x12\x19\n\x11publish_frequency\x18\x03 \x01(\x02\x12-\n\ttimestamp\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp*\xc8\x01\n\x0fJointStateField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x14\n\x10PRESENT_POSITION\x10\x02\x12\x11\n\rPRESENT_SPEED\x10\x03\x12\x10\n\x0cPRESENT_LOAD\x10\x04\x12\x0f\n\x0bTEMPERATURE\x10\x05\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f\x32\xed\x02\n\x11JointStateService\x12H\n\x10GetAllJointNames\x12\x16.google.protobuf.Empty\x1a\x1c.reachy.sdk.joint.JointNames\x12M\n\rGetJointState\x12\x1e.reachy.sdk.joint.JointRequest\x1a\x1c.reachy.sdk.joint.JointState\x12Y\n\x11GetAllJointsState\x12\".reachy.sdk.joint.AllJointsRequest\x1a .reachy.sdk.joint.AllJointsState\x12\x64\n\x14StreamAllJointsState\x12(.reachy.sdk.joint.StreamAllJointsRequest\x1a .reachy.sdk.joint.AllJointsState0\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_JOINTSTATEFIELD = _descriptor.EnumDescriptor(
  name='JointStateField',
  full_name='reachy.sdk.joint.JointStateField',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NAME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRESENT_POSITION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRESENT_SPEED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRESENT_LOAD', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEMPERATURE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLIANT', index=6, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOAL_POSITION', index=7, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPEED_LIMIT', index=8, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TORQUE_LIMIT', index=9, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PID', index=10, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALL', index=11, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1187,
  serialized_end=1387,
)
_sym_db.RegisterEnumDescriptor(_JOINTSTATEFIELD)

JointStateField = enum_type_wrapper.EnumTypeWrapper(_JOINTSTATEFIELD)
NONE = 0
NAME = 1
PRESENT_POSITION = 2
PRESENT_SPEED = 3
PRESENT_LOAD = 4
TEMPERATURE = 5
COMPLIANT = 8
GOAL_POSITION = 9
SPEED_LIMIT = 10
TORQUE_LIMIT = 11
PID = 12
ALL = 15



_JOINTSTATE = _descriptor.Descriptor(
  name='JointState',
  full_name='reachy.sdk.joint.JointState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='reachy.sdk.joint.JointState.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='present_position', full_name='reachy.sdk.joint.JointState.present_position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='present_speed', full_name='reachy.sdk.joint.JointState.present_speed', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='present_load', full_name='reachy.sdk.joint.JointState.present_load', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='reachy.sdk.joint.JointState.temperature', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compliant', full_name='reachy.sdk.joint.JointState.compliant', index=5,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='goal_position', full_name='reachy.sdk.joint.JointState.goal_position', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed_limit', full_name='reachy.sdk.joint.JointState.speed_limit', index=7,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='torque_limit', full_name='reachy.sdk.joint.JointState.torque_limit', index=8,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='reachy.sdk.joint.JointState.timestamp', index=9,
      number=15, type=11, cpp_type=10, label=1,
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
  serialized_start=134,
  serialized_end=615,
)


_JOINTNAMES = _descriptor.Descriptor(
  name='JointNames',
  full_name='reachy.sdk.joint.JointNames',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='reachy.sdk.joint.JointNames.names', index=0,
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
  serialized_start=617,
  serialized_end=644,
)


_ALLJOINTSSTATE = _descriptor.Descriptor(
  name='AllJointsState',
  full_name='reachy.sdk.joint.AllJointsState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='joints', full_name='reachy.sdk.joint.AllJointsState.joints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='reachy.sdk.joint.AllJointsState.timestamp', index=1,
      number=15, type=11, cpp_type=10, label=1,
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
  serialized_start=646,
  serialized_end=755,
)


_JOINTREQUEST = _descriptor.Descriptor(
  name='JointRequest',
  full_name='reachy.sdk.joint.JointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='reachy.sdk.joint.JointRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requested_fields', full_name='reachy.sdk.joint.JointRequest.requested_fields', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='reachy.sdk.joint.JointRequest.timestamp', index=2,
      number=15, type=11, cpp_type=10, label=1,
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
  serialized_start=758,
  serialized_end=894,
)


_ALLJOINTSREQUEST = _descriptor.Descriptor(
  name='AllJointsRequest',
  full_name='reachy.sdk.joint.AllJointsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='requested_fields', full_name='reachy.sdk.joint.AllJointsRequest.requested_fields', index=0,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='reachy.sdk.joint.AllJointsRequest.timestamp', index=1,
      number=15, type=11, cpp_type=10, label=1,
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
  serialized_start=896,
  serialized_end=1022,
)


_STREAMALLJOINTSREQUEST = _descriptor.Descriptor(
  name='StreamAllJointsRequest',
  full_name='reachy.sdk.joint.StreamAllJointsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='requested_fields', full_name='reachy.sdk.joint.StreamAllJointsRequest.requested_fields', index=0,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='publish_frequency', full_name='reachy.sdk.joint.StreamAllJointsRequest.publish_frequency', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='reachy.sdk.joint.StreamAllJointsRequest.timestamp', index=2,
      number=15, type=11, cpp_type=10, label=1,
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
  serialized_start=1025,
  serialized_end=1184,
)

_JOINTSTATE.fields_by_name['present_position'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_JOINTSTATE.fields_by_name['present_speed'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_JOINTSTATE.fields_by_name['present_load'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_JOINTSTATE.fields_by_name['temperature'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_JOINTSTATE.fields_by_name['compliant'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_JOINTSTATE.fields_by_name['goal_position'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_JOINTSTATE.fields_by_name['speed_limit'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_JOINTSTATE.fields_by_name['torque_limit'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_JOINTSTATE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ALLJOINTSSTATE.fields_by_name['joints'].message_type = _JOINTSTATE
_ALLJOINTSSTATE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOINTREQUEST.fields_by_name['requested_fields'].enum_type = _JOINTSTATEFIELD
_JOINTREQUEST.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ALLJOINTSREQUEST.fields_by_name['requested_fields'].enum_type = _JOINTSTATEFIELD
_ALLJOINTSREQUEST.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STREAMALLJOINTSREQUEST.fields_by_name['requested_fields'].enum_type = _JOINTSTATEFIELD
_STREAMALLJOINTSREQUEST.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['JointState'] = _JOINTSTATE
DESCRIPTOR.message_types_by_name['JointNames'] = _JOINTNAMES
DESCRIPTOR.message_types_by_name['AllJointsState'] = _ALLJOINTSSTATE
DESCRIPTOR.message_types_by_name['JointRequest'] = _JOINTREQUEST
DESCRIPTOR.message_types_by_name['AllJointsRequest'] = _ALLJOINTSREQUEST
DESCRIPTOR.message_types_by_name['StreamAllJointsRequest'] = _STREAMALLJOINTSREQUEST
DESCRIPTOR.enum_types_by_name['JointStateField'] = _JOINTSTATEFIELD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JointState = _reflection.GeneratedProtocolMessageType('JointState', (_message.Message,), {
  'DESCRIPTOR' : _JOINTSTATE,
  '__module__' : 'joint_state_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.joint.JointState)
  })
_sym_db.RegisterMessage(JointState)

JointNames = _reflection.GeneratedProtocolMessageType('JointNames', (_message.Message,), {
  'DESCRIPTOR' : _JOINTNAMES,
  '__module__' : 'joint_state_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.joint.JointNames)
  })
_sym_db.RegisterMessage(JointNames)

AllJointsState = _reflection.GeneratedProtocolMessageType('AllJointsState', (_message.Message,), {
  'DESCRIPTOR' : _ALLJOINTSSTATE,
  '__module__' : 'joint_state_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.joint.AllJointsState)
  })
_sym_db.RegisterMessage(AllJointsState)

JointRequest = _reflection.GeneratedProtocolMessageType('JointRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOINTREQUEST,
  '__module__' : 'joint_state_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.joint.JointRequest)
  })
_sym_db.RegisterMessage(JointRequest)

AllJointsRequest = _reflection.GeneratedProtocolMessageType('AllJointsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALLJOINTSREQUEST,
  '__module__' : 'joint_state_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.joint.AllJointsRequest)
  })
_sym_db.RegisterMessage(AllJointsRequest)

StreamAllJointsRequest = _reflection.GeneratedProtocolMessageType('StreamAllJointsRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMALLJOINTSREQUEST,
  '__module__' : 'joint_state_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.joint.StreamAllJointsRequest)
  })
_sym_db.RegisterMessage(StreamAllJointsRequest)



_JOINTSTATESERVICE = _descriptor.ServiceDescriptor(
  name='JointStateService',
  full_name='reachy.sdk.joint.JointStateService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1390,
  serialized_end=1755,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllJointNames',
    full_name='reachy.sdk.joint.JointStateService.GetAllJointNames',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_JOINTNAMES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetJointState',
    full_name='reachy.sdk.joint.JointStateService.GetJointState',
    index=1,
    containing_service=None,
    input_type=_JOINTREQUEST,
    output_type=_JOINTSTATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllJointsState',
    full_name='reachy.sdk.joint.JointStateService.GetAllJointsState',
    index=2,
    containing_service=None,
    input_type=_ALLJOINTSREQUEST,
    output_type=_ALLJOINTSSTATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamAllJointsState',
    full_name='reachy.sdk.joint.JointStateService.StreamAllJointsState',
    index=3,
    containing_service=None,
    input_type=_STREAMALLJOINTSREQUEST,
    output_type=_ALLJOINTSSTATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_JOINTSTATESERVICE)

DESCRIPTOR.services_by_name['JointStateService'] = _JOINTSTATESERVICE

# @@protoc_insertion_point(module_scope)
