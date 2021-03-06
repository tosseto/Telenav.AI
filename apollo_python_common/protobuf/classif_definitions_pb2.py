"""
Copyright 2018-2019 Telenav (http://telenav.com)

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: classif_definitions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='classif_definitions.proto',
  package='orbb',
  syntax='proto2',
  serialized_pb=_b('\n\x19\x63lassif_definitions.proto\x12\x04orbb\"@\n\x16\x43lassifPredictionClass\x12\x12\n\nclass_name\x18\x01 \x02(\t\x12\x12\n\nconfidence\x18\x02 \x02(\x01\"u\n\x11\x43lassifPrediction\x12\x11\n\talgorithm\x18\x01 \x02(\t\x12\x19\n\x11\x61lgorithm_version\x18\x02 \x02(\t\x12\x32\n\x0cpred_classes\x18\x03 \x03(\x0b\x32\x1c.orbb.ClassifPredictionClass')
)




_CLASSIFPREDICTIONCLASS = _descriptor.Descriptor(
  name='ClassifPredictionClass',
  full_name='orbb.ClassifPredictionClass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_name', full_name='orbb.ClassifPredictionClass.class_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='orbb.ClassifPredictionClass.confidence', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=99,
)


_CLASSIFPREDICTION = _descriptor.Descriptor(
  name='ClassifPrediction',
  full_name='orbb.ClassifPrediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='orbb.ClassifPrediction.algorithm', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='algorithm_version', full_name='orbb.ClassifPrediction.algorithm_version', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pred_classes', full_name='orbb.ClassifPrediction.pred_classes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=218,
)

_CLASSIFPREDICTION.fields_by_name['pred_classes'].message_type = _CLASSIFPREDICTIONCLASS
DESCRIPTOR.message_types_by_name['ClassifPredictionClass'] = _CLASSIFPREDICTIONCLASS
DESCRIPTOR.message_types_by_name['ClassifPrediction'] = _CLASSIFPREDICTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassifPredictionClass = _reflection.GeneratedProtocolMessageType('ClassifPredictionClass', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFPREDICTIONCLASS,
  __module__ = 'classif_definitions_pb2'
  # @@protoc_insertion_point(class_scope:orbb.ClassifPredictionClass)
  ))
_sym_db.RegisterMessage(ClassifPredictionClass)

ClassifPrediction = _reflection.GeneratedProtocolMessageType('ClassifPrediction', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFPREDICTION,
  __module__ = 'classif_definitions_pb2'
  # @@protoc_insertion_point(class_scope:orbb.ClassifPrediction)
  ))
_sym_db.RegisterMessage(ClassifPrediction)


# @@protoc_insertion_point(module_scope)
