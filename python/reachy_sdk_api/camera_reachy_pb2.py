# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: camera_reachy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='camera_reachy.proto',
  package='reachy.sdk.camera',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x63\x61mera_reachy.proto\x12\x11reachy.sdk.camera\"\x15\n\x05Image\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"1\n\x06\x43\x61mera\x12\'\n\x02id\x18\x01 \x01(\x0e\x32\x1b.reachy.sdk.camera.CameraId\"9\n\x0cImageRequest\x12)\n\x06\x63\x61mera\x18\x01 \x01(\x0b\x32\x19.reachy.sdk.camera.Camera\"F\n\x12StreamImageRequest\x12\x30\n\x07request\x18\x01 \x01(\x0b\x32\x1f.reachy.sdk.camera.ImageRequest\"\x1a\n\tZoomSpeed\x12\r\n\x05speed\x18\x01 \x01(\r\"\x0c\n\nZoomHoming\"E\n\tZoomLevel\x12\x38\n\x05level\x18\x01 \x01(\x0e\x32).reachy.sdk.camera.ZoomLevelPossibilities\"!\n\x0eZoomCommandAck\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\xea\x01\n\x0bZoomCommand\x12)\n\x06\x63\x61mera\x18\x01 \x01(\x0b\x32\x19.reachy.sdk.camera.Camera\x12\x37\n\x0ehoming_command\x18\x02 \x01(\x0b\x32\x1d.reachy.sdk.camera.ZoomHomingH\x00\x12\x35\n\rspeed_command\x18\x03 \x01(\x0b\x32\x1c.reachy.sdk.camera.ZoomSpeedH\x00\x12\x35\n\rlevel_command\x18\x04 \x01(\x0b\x32\x1c.reachy.sdk.camera.ZoomLevelH\x00\x42\t\n\x07\x63ommand*\x1f\n\x08\x43\x61meraId\x12\x08\n\x04LEFT\x10\x00\x12\t\n\x05RIGHT\x10\x01*>\n\x16ZoomLevelPossibilities\x12\x08\n\x04ZERO\x10\x00\x12\x06\n\x02IN\x10\x01\x12\t\n\x05INTER\x10\x02\x12\x07\n\x03OUT\x10\x03\x32\x90\x03\n\rCameraService\x12\x45\n\x08GetImage\x12\x1f.reachy.sdk.camera.ImageRequest\x1a\x18.reachy.sdk.camera.Image\x12P\n\x0bStreamImage\x12%.reachy.sdk.camera.StreamImageRequest\x1a\x18.reachy.sdk.camera.Image0\x01\x12G\n\x0cGetZoomLevel\x12\x19.reachy.sdk.camera.Camera\x1a\x1c.reachy.sdk.camera.ZoomLevel\x12G\n\x0cGetZoomSpeed\x12\x19.reachy.sdk.camera.Camera\x1a\x1c.reachy.sdk.camera.ZoomSpeed\x12T\n\x0fSendZoomCommand\x12\x1e.reachy.sdk.camera.ZoomCommand\x1a!.reachy.sdk.camera.ZoomCommandAckb\x06proto3'
)

_CAMERAID = _descriptor.EnumDescriptor(
  name='CameraId',
  full_name='reachy.sdk.camera.CameraId',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LEFT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RIGHT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=632,
  serialized_end=663,
)
_sym_db.RegisterEnumDescriptor(_CAMERAID)

CameraId = enum_type_wrapper.EnumTypeWrapper(_CAMERAID)
_ZOOMLEVELPOSSIBILITIES = _descriptor.EnumDescriptor(
  name='ZoomLevelPossibilities',
  full_name='reachy.sdk.camera.ZoomLevelPossibilities',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ZERO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OUT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=665,
  serialized_end=727,
)
_sym_db.RegisterEnumDescriptor(_ZOOMLEVELPOSSIBILITIES)

ZoomLevelPossibilities = enum_type_wrapper.EnumTypeWrapper(_ZOOMLEVELPOSSIBILITIES)
LEFT = 0
RIGHT = 1
ZERO = 0
IN = 1
INTER = 2
OUT = 3



_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='reachy.sdk.camera.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='reachy.sdk.camera.Image.data', index=0,
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
  serialized_start=42,
  serialized_end=63,
)


_CAMERA = _descriptor.Descriptor(
  name='Camera',
  full_name='reachy.sdk.camera.Camera',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='reachy.sdk.camera.Camera.id', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=114,
)


_IMAGEREQUEST = _descriptor.Descriptor(
  name='ImageRequest',
  full_name='reachy.sdk.camera.ImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera', full_name='reachy.sdk.camera.ImageRequest.camera', index=0,
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
  serialized_start=116,
  serialized_end=173,
)


_STREAMIMAGEREQUEST = _descriptor.Descriptor(
  name='StreamImageRequest',
  full_name='reachy.sdk.camera.StreamImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='reachy.sdk.camera.StreamImageRequest.request', index=0,
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
  serialized_start=175,
  serialized_end=245,
)


_ZOOMSPEED = _descriptor.Descriptor(
  name='ZoomSpeed',
  full_name='reachy.sdk.camera.ZoomSpeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='speed', full_name='reachy.sdk.camera.ZoomSpeed.speed', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=273,
)


_ZOOMHOMING = _descriptor.Descriptor(
  name='ZoomHoming',
  full_name='reachy.sdk.camera.ZoomHoming',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=275,
  serialized_end=287,
)


_ZOOMLEVEL = _descriptor.Descriptor(
  name='ZoomLevel',
  full_name='reachy.sdk.camera.ZoomLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='reachy.sdk.camera.ZoomLevel.level', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=358,
)


_ZOOMCOMMANDACK = _descriptor.Descriptor(
  name='ZoomCommandAck',
  full_name='reachy.sdk.camera.ZoomCommandAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='reachy.sdk.camera.ZoomCommandAck.success', index=0,
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
  serialized_start=360,
  serialized_end=393,
)


_ZOOMCOMMAND = _descriptor.Descriptor(
  name='ZoomCommand',
  full_name='reachy.sdk.camera.ZoomCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera', full_name='reachy.sdk.camera.ZoomCommand.camera', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='homing_command', full_name='reachy.sdk.camera.ZoomCommand.homing_command', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed_command', full_name='reachy.sdk.camera.ZoomCommand.speed_command', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level_command', full_name='reachy.sdk.camera.ZoomCommand.level_command', index=3,
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
    _descriptor.OneofDescriptor(
      name='command', full_name='reachy.sdk.camera.ZoomCommand.command',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=396,
  serialized_end=630,
)

_CAMERA.fields_by_name['id'].enum_type = _CAMERAID
_IMAGEREQUEST.fields_by_name['camera'].message_type = _CAMERA
_STREAMIMAGEREQUEST.fields_by_name['request'].message_type = _IMAGEREQUEST
_ZOOMLEVEL.fields_by_name['level'].enum_type = _ZOOMLEVELPOSSIBILITIES
_ZOOMCOMMAND.fields_by_name['camera'].message_type = _CAMERA
_ZOOMCOMMAND.fields_by_name['homing_command'].message_type = _ZOOMHOMING
_ZOOMCOMMAND.fields_by_name['speed_command'].message_type = _ZOOMSPEED
_ZOOMCOMMAND.fields_by_name['level_command'].message_type = _ZOOMLEVEL
_ZOOMCOMMAND.oneofs_by_name['command'].fields.append(
  _ZOOMCOMMAND.fields_by_name['homing_command'])
_ZOOMCOMMAND.fields_by_name['homing_command'].containing_oneof = _ZOOMCOMMAND.oneofs_by_name['command']
_ZOOMCOMMAND.oneofs_by_name['command'].fields.append(
  _ZOOMCOMMAND.fields_by_name['speed_command'])
_ZOOMCOMMAND.fields_by_name['speed_command'].containing_oneof = _ZOOMCOMMAND.oneofs_by_name['command']
_ZOOMCOMMAND.oneofs_by_name['command'].fields.append(
  _ZOOMCOMMAND.fields_by_name['level_command'])
_ZOOMCOMMAND.fields_by_name['level_command'].containing_oneof = _ZOOMCOMMAND.oneofs_by_name['command']
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['Camera'] = _CAMERA
DESCRIPTOR.message_types_by_name['ImageRequest'] = _IMAGEREQUEST
DESCRIPTOR.message_types_by_name['StreamImageRequest'] = _STREAMIMAGEREQUEST
DESCRIPTOR.message_types_by_name['ZoomSpeed'] = _ZOOMSPEED
DESCRIPTOR.message_types_by_name['ZoomHoming'] = _ZOOMHOMING
DESCRIPTOR.message_types_by_name['ZoomLevel'] = _ZOOMLEVEL
DESCRIPTOR.message_types_by_name['ZoomCommandAck'] = _ZOOMCOMMANDACK
DESCRIPTOR.message_types_by_name['ZoomCommand'] = _ZOOMCOMMAND
DESCRIPTOR.enum_types_by_name['CameraId'] = _CAMERAID
DESCRIPTOR.enum_types_by_name['ZoomLevelPossibilities'] = _ZOOMLEVELPOSSIBILITIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'camera_reachy_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.camera.Image)
  })
_sym_db.RegisterMessage(Image)

Camera = _reflection.GeneratedProtocolMessageType('Camera', (_message.Message,), {
  'DESCRIPTOR' : _CAMERA,
  '__module__' : 'camera_reachy_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.camera.Camera)
  })
_sym_db.RegisterMessage(Camera)

ImageRequest = _reflection.GeneratedProtocolMessageType('ImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEREQUEST,
  '__module__' : 'camera_reachy_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.camera.ImageRequest)
  })
_sym_db.RegisterMessage(ImageRequest)

StreamImageRequest = _reflection.GeneratedProtocolMessageType('StreamImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMIMAGEREQUEST,
  '__module__' : 'camera_reachy_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.camera.StreamImageRequest)
  })
_sym_db.RegisterMessage(StreamImageRequest)

ZoomSpeed = _reflection.GeneratedProtocolMessageType('ZoomSpeed', (_message.Message,), {
  'DESCRIPTOR' : _ZOOMSPEED,
  '__module__' : 'camera_reachy_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.camera.ZoomSpeed)
  })
_sym_db.RegisterMessage(ZoomSpeed)

ZoomHoming = _reflection.GeneratedProtocolMessageType('ZoomHoming', (_message.Message,), {
  'DESCRIPTOR' : _ZOOMHOMING,
  '__module__' : 'camera_reachy_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.camera.ZoomHoming)
  })
_sym_db.RegisterMessage(ZoomHoming)

ZoomLevel = _reflection.GeneratedProtocolMessageType('ZoomLevel', (_message.Message,), {
  'DESCRIPTOR' : _ZOOMLEVEL,
  '__module__' : 'camera_reachy_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.camera.ZoomLevel)
  })
_sym_db.RegisterMessage(ZoomLevel)

ZoomCommandAck = _reflection.GeneratedProtocolMessageType('ZoomCommandAck', (_message.Message,), {
  'DESCRIPTOR' : _ZOOMCOMMANDACK,
  '__module__' : 'camera_reachy_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.camera.ZoomCommandAck)
  })
_sym_db.RegisterMessage(ZoomCommandAck)

ZoomCommand = _reflection.GeneratedProtocolMessageType('ZoomCommand', (_message.Message,), {
  'DESCRIPTOR' : _ZOOMCOMMAND,
  '__module__' : 'camera_reachy_pb2'
  # @@protoc_insertion_point(class_scope:reachy.sdk.camera.ZoomCommand)
  })
_sym_db.RegisterMessage(ZoomCommand)



_CAMERASERVICE = _descriptor.ServiceDescriptor(
  name='CameraService',
  full_name='reachy.sdk.camera.CameraService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=730,
  serialized_end=1130,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetImage',
    full_name='reachy.sdk.camera.CameraService.GetImage',
    index=0,
    containing_service=None,
    input_type=_IMAGEREQUEST,
    output_type=_IMAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamImage',
    full_name='reachy.sdk.camera.CameraService.StreamImage',
    index=1,
    containing_service=None,
    input_type=_STREAMIMAGEREQUEST,
    output_type=_IMAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetZoomLevel',
    full_name='reachy.sdk.camera.CameraService.GetZoomLevel',
    index=2,
    containing_service=None,
    input_type=_CAMERA,
    output_type=_ZOOMLEVEL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetZoomSpeed',
    full_name='reachy.sdk.camera.CameraService.GetZoomSpeed',
    index=3,
    containing_service=None,
    input_type=_CAMERA,
    output_type=_ZOOMSPEED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendZoomCommand',
    full_name='reachy.sdk.camera.CameraService.SendZoomCommand',
    index=4,
    containing_service=None,
    input_type=_ZOOMCOMMAND,
    output_type=_ZOOMCOMMANDACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMERASERVICE)

DESCRIPTOR.services_by_name['CameraService'] = _CAMERASERVICE

# @@protoc_insertion_point(module_scope)
