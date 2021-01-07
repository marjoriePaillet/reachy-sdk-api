# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: camera.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='camera.proto',
  package='reachy.sdk.camera',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63\x61mera.proto\x12\x11reachy.sdk.camera\"\x16\n\x05Image\x12\r\n\x05image\x18\x01 \x01(\x0c\"\x14\n\x04Side\x12\x0c\n\x04side\x18\x01 \x01(\x08\x32N\n\rCameraService\x12=\n\x08GetImage\x12\x17.reachy.sdk.camera.Side\x1a\x18.reachy.sdk.camera.Imageb\x06proto3'
)




_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='reachy.sdk.camera.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='reachy.sdk.camera.Image.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=35,
  serialized_end=57,
)


_SIDE = _descriptor.Descriptor(
  name='Side',
  full_name='reachy.sdk.camera.Side',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='side', full_name='reachy.sdk.camera.Side.side', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=59,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['Side'] = _SIDE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'camera_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.camera.Image)
  })
_sym_db.RegisterMessage(Image)

Side = _reflection.GeneratedProtocolMessageType('Side', (_message.Message,), {
  'DESCRIPTOR' : _SIDE,
  '__module__' : 'camera_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.camera.Side)
  })
_sym_db.RegisterMessage(Side)



_CAMERASERVICE = _descriptor.ServiceDescriptor(
  name='CameraService',
  full_name='reachy.sdk.camera.CameraService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=81,
  serialized_end=159,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetImage',
    full_name='reachy.sdk.camera.CameraService.GetImage',
    index=0,
    containing_service=None,
    input_type=_SIDE,
    output_type=_IMAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMERASERVICE)

DESCRIPTOR.services_by_name['CameraService'] = _CAMERASERVICE

# @@protoc_insertion_point(module_scope)
