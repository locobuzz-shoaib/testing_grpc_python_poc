# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\x12\x07message\"\xe2\x01\n\x08UserInfo\x12\x16\n\x0e\x41uthorSocialID\x18\x01 \x01(\t\x12\x12\n\nAuthorName\x18\x02 \x01(\t\x12\x0b\n\x03Url\x18\x03 \x01(\t\x12\x15\n\rLocationsJson\x18\x04 \x01(\t\x12\x0b\n\x03\x42io\x18\x05 \x01(\t\x12\x16\n\x0eKnowsAboutJson\x18\x06 \x01(\t\x12\x12\n\nSchoolJson\x18\x07 \x01(\t\x12\x10\n\x08WorkJson\x18\x08 \x01(\t\x12\x14\n\x0cLanguageJson\x18\t \x01(\t\x12\x0e\n\x06PicUrl\x18\n \x01(\t\x12\x15\n\rUserTopicJson\x18\x0b \x01(\t\"\x0f\n\rBrandSettings\"\x9f\x01\n\tBrandInfo\x12\x0f\n\x07\x42randID\x18\x01 \x01(\x05\x12\x11\n\tBrandName\x18\x02 \x01(\t\x12\x12\n\nCategoryID\x18\x03 \x01(\x05\x12\x14\n\x0c\x43\x61tegoryName\x18\x04 \x01(\t\x12-\n\rBrandSettings\x18\x05 \x01(\x0b\x32\x16.message.BrandSettings\x12\x15\n\rOperationEnum\x18\x06 \x01(\t\"W\n\x16MentionTrackingDetails\x12\x1d\n\x15\x46\x65tchingServiceInTime\x18\x01 \x01(\t\x12\x1e\n\x16\x46\x65tchingServiceOutTime\x18\x02 \x01(\t\"\xeb\x02\n\x07RawData\x12\x10\n\x08ObjectId\x18\x01 \x01(\x03\x12\x10\n\x08SocialID\x18\x02 \x01(\t\x12\x0f\n\x07OrderID\x18\x03 \x01(\x05\x12\x13\n\x0b\x43reatedDate\x18\x04 \x01(\t\x12\x18\n\x10NumCommentsCount\x18\x05 \x01(\x05\x12\x15\n\rNumShareCount\x18\x06 \x01(\x05\x12\x15\n\rNumVideoViews\x18\x07 \x01(\x05\x12\x13\n\x0b\x44\x65scription\x18\x08 \x01(\t\x12\x14\n\x0cLanguageName\x18\t \x01(\t\x12\x16\n\x0e\x46ilterKeywords\x18\n \x01(\t\x12#\n\x08UserInfo\x18\x0b \x01(\x0b\x32\x11.message.UserInfo\x12\x0b\n\x03URL\x18\x0c \x01(\t\x12\x14\n\x0c\x41nswerCounts\x18\r \x01(\x05\x12\x16\n\x0eSimplifiedText\x18\x0e \x01(\t\x12\x15\n\rNumLikesCount\x18\x0f \x01(\x05\x12\x14\n\x0cPostSocialId\x18\x10 \x01(\t\"\xd4\x01\n\x07Message\x12!\n\x07RawData\x18\x01 \x01(\x0b\x32\x10.message.RawData\x12\x14\n\x0c\x43hannelGroup\x18\x02 \x01(\x05\x12\x13\n\x0b\x43hannelType\x18\x03 \x01(\x05\x12%\n\tBrandInfo\x18\x04 \x01(\x0b\x32\x12.message.BrandInfo\x12?\n\x16MentionTrackingDetails\x18\x05 \x01(\x0b\x32\x1f.message.MentionTrackingDetails\x12\x13\n\x0bServiceName\x18\x06 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERINFO']._serialized_start=27
  _globals['_USERINFO']._serialized_end=253
  _globals['_BRANDSETTINGS']._serialized_start=255
  _globals['_BRANDSETTINGS']._serialized_end=270
  _globals['_BRANDINFO']._serialized_start=273
  _globals['_BRANDINFO']._serialized_end=432
  _globals['_MENTIONTRACKINGDETAILS']._serialized_start=434
  _globals['_MENTIONTRACKINGDETAILS']._serialized_end=521
  _globals['_RAWDATA']._serialized_start=524
  _globals['_RAWDATA']._serialized_end=887
  _globals['_MESSAGE']._serialized_start=890
  _globals['_MESSAGE']._serialized_end=1102
# @@protoc_insertion_point(module_scope)