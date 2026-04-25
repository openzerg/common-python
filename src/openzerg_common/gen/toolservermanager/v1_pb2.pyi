from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToolServerUrl(_message.Message):
    __slots__ = ("name", "url", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    url: str
    config: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., url: _Optional[str] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...

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

class ContainerEnv(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class StartToolServerRequest(_message.Message):
    __slots__ = ("type", "image", "env", "command")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    type: str
    image: str
    env: _containers.RepeatedCompositeFieldContainer[ContainerEnv]
    command: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[str] = ..., image: _Optional[str] = ..., env: _Optional[_Iterable[_Union[ContainerEnv, _Mapping]]] = ..., command: _Optional[_Iterable[str]] = ...) -> None: ...

class StartToolServerResponse(_message.Message):
    __slots__ = ("containerName", "instanceId")
    CONTAINERNAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    containerName: str
    instanceId: str
    def __init__(self, containerName: _Optional[str] = ..., instanceId: _Optional[str] = ...) -> None: ...

class StopToolServerRequest(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: str
    def __init__(self, type: _Optional[str] = ...) -> None: ...

class StopToolServerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListToolServersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ToolServerInfo(_message.Message):
    __slots__ = ("instanceId", "name", "type", "url", "port", "lifecycle", "toolCount", "containerName")
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    TOOLCOUNT_FIELD_NUMBER: _ClassVar[int]
    CONTAINERNAME_FIELD_NUMBER: _ClassVar[int]
    instanceId: str
    name: str
    type: str
    url: str
    port: int
    lifecycle: str
    toolCount: int
    containerName: str
    def __init__(self, instanceId: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., url: _Optional[str] = ..., port: _Optional[int] = ..., lifecycle: _Optional[str] = ..., toolCount: _Optional[int] = ..., containerName: _Optional[str] = ...) -> None: ...

class ListToolServersResponse(_message.Message):
    __slots__ = ("servers",)
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[ToolServerInfo]
    def __init__(self, servers: _Optional[_Iterable[_Union[ToolServerInfo, _Mapping]]] = ...) -> None: ...

class RefreshToolCacheRequest(_message.Message):
    __slots__ = ("instanceType",)
    INSTANCETYPE_FIELD_NUMBER: _ClassVar[int]
    instanceType: str
    def __init__(self, instanceType: _Optional[str] = ...) -> None: ...

class RefreshToolCacheResponse(_message.Message):
    __slots__ = ("toolCount",)
    TOOLCOUNT_FIELD_NUMBER: _ClassVar[int]
    toolCount: int
    def __init__(self, toolCount: _Optional[int] = ...) -> None: ...

class ResolveToolsRequest(_message.Message):
    __slots__ = ("sessionId", "toolServerTypes")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    TOOLSERVERTYPES_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    toolServerTypes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sessionId: _Optional[str] = ..., toolServerTypes: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolveToolsResponse(_message.Message):
    __slots__ = ("tools", "systemContext", "toolServerUrls")
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    SYSTEMCONTEXT_FIELD_NUMBER: _ClassVar[int]
    TOOLSERVERURLS_FIELD_NUMBER: _ClassVar[int]
    tools: _containers.RepeatedCompositeFieldContainer[ToolDefinition]
    systemContext: str
    toolServerUrls: _containers.RepeatedCompositeFieldContainer[ToolServerUrl]
    def __init__(self, tools: _Optional[_Iterable[_Union[ToolDefinition, _Mapping]]] = ..., systemContext: _Optional[str] = ..., toolServerUrls: _Optional[_Iterable[_Union[ToolServerUrl, _Mapping]]] = ...) -> None: ...

class ExecuteToolRequest(_message.Message):
    __slots__ = ("sessionId", "toolName", "argsJson", "sessionToken")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    TOOLNAME_FIELD_NUMBER: _ClassVar[int]
    ARGSJSON_FIELD_NUMBER: _ClassVar[int]
    SESSIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    toolName: str
    argsJson: str
    sessionToken: str
    def __init__(self, sessionId: _Optional[str] = ..., toolName: _Optional[str] = ..., argsJson: _Optional[str] = ..., sessionToken: _Optional[str] = ...) -> None: ...

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

class HealthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HealthResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
