# manually copied from github.com/posthog/proxy-provisioner@6b0fc2d
# ruff: noqa
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _CertificateState:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CertificateStateEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CertificateState.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN: _CertificateState.ValueType  # 0
    ISSUING: _CertificateState.ValueType  # 1
    READY: _CertificateState.ValueType  # 2

class CertificateState(_CertificateState, metaclass=_CertificateStateEnumTypeWrapper): ...

UNKNOWN: CertificateState.ValueType  # 0
ISSUING: CertificateState.ValueType  # 1
READY: CertificateState.ValueType  # 2
global___CertificateState = CertificateState

class _ErrorType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ErrorTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ErrorType.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OK: _ErrorType.ValueType  # 0
    UNKNOWN_ERROR: _ErrorType.ValueType  # 1
    INVALID_REQUEST: _ErrorType.ValueType  # 2
    NOT_FOUND: _ErrorType.ValueType  # 3
    INTERNAL_ERROR: _ErrorType.ValueType  # 4

class ErrorType(_ErrorType, metaclass=_ErrorTypeEnumTypeWrapper): ...

OK: ErrorType.ValueType  # 0
UNKNOWN_ERROR: ErrorType.ValueType  # 1
INVALID_REQUEST: ErrorType.ValueType  # 2
NOT_FOUND: ErrorType.ValueType  # 3
INTERNAL_ERROR: ErrorType.ValueType  # 4
global___ErrorType = ErrorType

@typing_extensions.final
class CreateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    domain: builtins.str
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
        domain: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["domain", b"domain", "uuid", b"uuid"]) -> None: ...

global___CreateRequest = CreateRequest

@typing_extensions.final
class CreateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CreateResponse = CreateResponse

@typing_extensions.final
class StatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    domain: builtins.str
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
        domain: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["domain", b"domain", "uuid", b"uuid"]) -> None: ...

global___StatusRequest = StatusRequest

@typing_extensions.final
class StatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_STATUS_FIELD_NUMBER: builtins.int
    certificate_status: global___CertificateState.ValueType
    def __init__(
        self,
        *,
        certificate_status: global___CertificateState.ValueType = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["certificate_status", b"certificate_status"]
    ) -> None: ...

global___StatusResponse = StatusResponse

@typing_extensions.final
class DeleteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    domain: builtins.str
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
        domain: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["domain", b"domain", "uuid", b"uuid"]) -> None: ...

global___DeleteRequest = DeleteRequest

@typing_extensions.final
class DeleteResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteResponse = DeleteResponse

@typing_extensions.final
class ResponseStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    error: global___ErrorType.ValueType
    message: builtins.str
    def __init__(
        self,
        *,
        error: global___ErrorType.ValueType = ...,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error", b"error", "message", b"message"]) -> None: ...

global___ResponseStatus = ResponseStatus
