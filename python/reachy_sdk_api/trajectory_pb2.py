# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trajectory.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='trajectory.proto',
  package='reachy.sdk.trajectory',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10trajectory.proto\x12\x15reachy.sdk.trajectory\x1a\x1egoogle/protobuf/wrappers.proto\"\xd9\x01\n\x11TrajectoryRequest\x12\x36\n\x11starting_position\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x34\n\x0ftarget_position\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12-\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\'\n\x02\x64t\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"+\n\nTrajectory\x12\x11\n\tpositions\x18\x01 \x03(\x01\x12\n\n\x02\x64t\x18\x02 \x01(\x01\x32\x80\x01\n\x11TrajectoryService\x12k\n\x1c\x43omputeMinimumJerkTrajectory\x12(.reachy.sdk.trajectory.TrajectoryRequest\x1a!.reachy.sdk.trajectory.Trajectoryb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_TRAJECTORYREQUEST = _descriptor.Descriptor(
  name='TrajectoryRequest',
  full_name='reachy.sdk.trajectory.TrajectoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='starting_position', full_name='reachy.sdk.trajectory.TrajectoryRequest.starting_position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_position', full_name='reachy.sdk.trajectory.TrajectoryRequest.target_position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration', full_name='reachy.sdk.trajectory.TrajectoryRequest.duration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dt', full_name='reachy.sdk.trajectory.TrajectoryRequest.dt', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=76,
  serialized_end=293,
)


_TRAJECTORY = _descriptor.Descriptor(
  name='Trajectory',
  full_name='reachy.sdk.trajectory.Trajectory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='positions', full_name='reachy.sdk.trajectory.Trajectory.positions', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dt', full_name='reachy.sdk.trajectory.Trajectory.dt', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=338,
)

_TRAJECTORYREQUEST.fields_by_name['starting_position'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_TRAJECTORYREQUEST.fields_by_name['target_position'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_TRAJECTORYREQUEST.fields_by_name['duration'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_TRAJECTORYREQUEST.fields_by_name['dt'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
DESCRIPTOR.message_types_by_name['TrajectoryRequest'] = _TRAJECTORYREQUEST
DESCRIPTOR.message_types_by_name['Trajectory'] = _TRAJECTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrajectoryRequest = _reflection.GeneratedProtocolMessageType('TrajectoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAJECTORYREQUEST,
  '__module__' : 'trajectory_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.trajectory.TrajectoryRequest)
  })
_sym_db.RegisterMessage(TrajectoryRequest)

Trajectory = _reflection.GeneratedProtocolMessageType('Trajectory', (_message.Message,), {
  'DESCRIPTOR' : _TRAJECTORY,
  '__module__' : 'trajectory_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.trajectory.Trajectory)
  })
_sym_db.RegisterMessage(Trajectory)



_TRAJECTORYSERVICE = _descriptor.ServiceDescriptor(
  name='TrajectoryService',
  full_name='reachy.sdk.trajectory.TrajectoryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=341,
  serialized_end=469,
  methods=[
  _descriptor.MethodDescriptor(
    name='ComputeMinimumJerkTrajectory',
    full_name='reachy.sdk.trajectory.TrajectoryService.ComputeMinimumJerkTrajectory',
    index=0,
    containing_service=None,
    input_type=_TRAJECTORYREQUEST,
    output_type=_TRAJECTORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRAJECTORYSERVICE)

DESCRIPTOR.services_by_name['TrajectoryService'] = _TRAJECTORYSERVICE

# @@protoc_insertion_point(module_scope)
