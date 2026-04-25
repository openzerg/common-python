from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListToolsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ToolDefinition(_message.Message):
    __slots__ = ("name", "description", "inputSchemaJson", "outputSchemaJson", "group", "priority", "dependencies")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUTSCHEMAJSON_FIELD_NUMBER: _ClassVar[int]
    OUTPUTSCHEMAJSON_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    inputSchemaJson: str
    outputSchemaJson: str
    group: str
    priority: int
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., inputSchemaJson: _Optional[str] = ..., outputSchemaJson: _Optional[str] = ..., group: _Optional[str] = ..., priority: _Optional[int] = ..., dependencies: _Optional[_Iterable[str]] = ...) -> None: ...

class ListToolsResponse(_message.Message):
    __slots__ = ("tools", "systemContext")
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    SYSTEMCONTEXT_FIELD_NUMBER: _ClassVar[int]
    tools: _containers.RepeatedCompositeFieldContainer[ToolDefinition]
    systemContext: str
    def __init__(self, tools: _Optional[_Iterable[_Union[ToolDefinition, _Mapping]]] = ..., systemContext: _Optional[str] = ...) -> None: ...

class ExecuteToolRequest(_message.Message):
    __slots__ = ("toolName", "argsJson", "sessionToken")
    TOOLNAME_FIELD_NUMBER: _ClassVar[int]
    ARGSJSON_FIELD_NUMBER: _ClassVar[int]
    SESSIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    toolName: str
    argsJson: str
    sessionToken: str
    def __init__(self, toolName: _Optional[str] = ..., argsJson: _Optional[str] = ..., sessionToken: _Optional[str] = ...) -> None: ...

class ExecuteToolResponse(_message.Message):
    __slots__ = ("resultJson", "success", "error", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESULTJSON_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    resultJson: str
    success: bool
    error: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, resultJson: _Optional[str] = ..., success: _Optional[bool] = ..., error: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
