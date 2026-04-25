from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderConfig(_message.Message):
    __slots__ = ("upstream", "apiKey", "modelId", "maxTokens", "contextLength", "autoCompactLength")
    UPSTREAM_FIELD_NUMBER: _ClassVar[int]
    APIKEY_FIELD_NUMBER: _ClassVar[int]
    MODELID_FIELD_NUMBER: _ClassVar[int]
    MAXTOKENS_FIELD_NUMBER: _ClassVar[int]
    CONTEXTLENGTH_FIELD_NUMBER: _ClassVar[int]
    AUTOCOMPACTLENGTH_FIELD_NUMBER: _ClassVar[int]
    upstream: str
    apiKey: str
    modelId: str
    maxTokens: int
    contextLength: int
    autoCompactLength: int
    def __init__(self, upstream: _Optional[str] = ..., apiKey: _Optional[str] = ..., modelId: _Optional[str] = ..., maxTokens: _Optional[int] = ..., contextLength: _Optional[int] = ..., autoCompactLength: _Optional[int] = ...) -> None: ...

class ToolServerEntry(_message.Message):
    __slots__ = ("type", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    type: str
    config: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[str] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SkillRef(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class WorkspaceConfig(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("apiKey",)
    APIKEY_FIELD_NUMBER: _ClassVar[int]
    apiKey: str
    def __init__(self, apiKey: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("userToken", "expiresInSec")
    USERTOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRESINSEC_FIELD_NUMBER: _ClassVar[int]
    userToken: str
    expiresInSec: int
    def __init__(self, userToken: _Optional[str] = ..., expiresInSec: _Optional[int] = ...) -> None: ...

class RegisterRequest(_message.Message):
    __slots__ = ("name", "instanceType", "ip", "port", "publicUrl", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCETYPE_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PUBLICURL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    instanceType: str
    ip: str
    port: int
    publicUrl: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., instanceType: _Optional[str] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ..., publicUrl: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ("instanceId", "serviceToken")
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    SERVICETOKEN_FIELD_NUMBER: _ClassVar[int]
    instanceId: str
    serviceToken: str
    def __init__(self, instanceId: _Optional[str] = ..., serviceToken: _Optional[str] = ...) -> None: ...

class HeartbeatRequest(_message.Message):
    __slots__ = ("instanceId",)
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    instanceId: str
    def __init__(self, instanceId: _Optional[str] = ...) -> None: ...

class HeartbeatResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListInstancesRequest(_message.Message):
    __slots__ = ("instanceType",)
    INSTANCETYPE_FIELD_NUMBER: _ClassVar[int]
    instanceType: str
    def __init__(self, instanceType: _Optional[str] = ...) -> None: ...

class InstanceInfo(_message.Message):
    __slots__ = ("instanceId", "name", "instanceType", "url", "lifecycle", "lastSeen", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCETYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    LASTSEEN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    instanceId: str
    name: str
    instanceType: str
    url: str
    lifecycle: str
    lastSeen: int
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, instanceId: _Optional[str] = ..., name: _Optional[str] = ..., instanceType: _Optional[str] = ..., url: _Optional[str] = ..., lifecycle: _Optional[str] = ..., lastSeen: _Optional[int] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListInstancesResponse(_message.Message):
    __slots__ = ("instances",)
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[InstanceInfo]
    def __init__(self, instances: _Optional[_Iterable[_Union[InstanceInfo, _Mapping]]] = ...) -> None: ...

class TemplateInfo(_message.Message):
    __slots__ = ("id", "name", "description", "systemPrompt", "providerConfig", "toolServerConfig", "skillConfig", "workspaceConfig", "extraPackage", "createdAt", "updatedAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SYSTEMPROMPT_FIELD_NUMBER: _ClassVar[int]
    PROVIDERCONFIG_FIELD_NUMBER: _ClassVar[int]
    TOOLSERVERCONFIG_FIELD_NUMBER: _ClassVar[int]
    SKILLCONFIG_FIELD_NUMBER: _ClassVar[int]
    WORKSPACECONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTRAPACKAGE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    systemPrompt: str
    providerConfig: ProviderConfig
    toolServerConfig: _containers.RepeatedCompositeFieldContainer[ToolServerEntry]
    skillConfig: _containers.RepeatedCompositeFieldContainer[SkillRef]
    workspaceConfig: WorkspaceConfig
    extraPackage: _containers.RepeatedScalarFieldContainer[str]
    createdAt: int
    updatedAt: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., systemPrompt: _Optional[str] = ..., providerConfig: _Optional[_Union[ProviderConfig, _Mapping]] = ..., toolServerConfig: _Optional[_Iterable[_Union[ToolServerEntry, _Mapping]]] = ..., skillConfig: _Optional[_Iterable[_Union[SkillRef, _Mapping]]] = ..., workspaceConfig: _Optional[_Union[WorkspaceConfig, _Mapping]] = ..., extraPackage: _Optional[_Iterable[str]] = ..., createdAt: _Optional[int] = ..., updatedAt: _Optional[int] = ...) -> None: ...

class ListTemplatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTemplatesResponse(_message.Message):
    __slots__ = ("templates",)
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[TemplateInfo]
    def __init__(self, templates: _Optional[_Iterable[_Union[TemplateInfo, _Mapping]]] = ...) -> None: ...

class GetTemplateRequest(_message.Message):
    __slots__ = ("templateId",)
    TEMPLATEID_FIELD_NUMBER: _ClassVar[int]
    templateId: str
    def __init__(self, templateId: _Optional[str] = ...) -> None: ...

class CreateTemplateRequest(_message.Message):
    __slots__ = ("name", "description", "systemPrompt", "providerConfig", "toolServerConfig", "skillConfig", "workspaceConfig", "extraPackage")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SYSTEMPROMPT_FIELD_NUMBER: _ClassVar[int]
    PROVIDERCONFIG_FIELD_NUMBER: _ClassVar[int]
    TOOLSERVERCONFIG_FIELD_NUMBER: _ClassVar[int]
    SKILLCONFIG_FIELD_NUMBER: _ClassVar[int]
    WORKSPACECONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTRAPACKAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    systemPrompt: str
    providerConfig: ProviderConfig
    toolServerConfig: _containers.RepeatedCompositeFieldContainer[ToolServerEntry]
    skillConfig: _containers.RepeatedCompositeFieldContainer[SkillRef]
    workspaceConfig: WorkspaceConfig
    extraPackage: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., systemPrompt: _Optional[str] = ..., providerConfig: _Optional[_Union[ProviderConfig, _Mapping]] = ..., toolServerConfig: _Optional[_Iterable[_Union[ToolServerEntry, _Mapping]]] = ..., skillConfig: _Optional[_Iterable[_Union[SkillRef, _Mapping]]] = ..., workspaceConfig: _Optional[_Union[WorkspaceConfig, _Mapping]] = ..., extraPackage: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateTemplateRequest(_message.Message):
    __slots__ = ("id", "name", "description", "systemPrompt", "providerConfig", "toolServerConfig", "skillConfig", "workspaceConfig", "extraPackage")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SYSTEMPROMPT_FIELD_NUMBER: _ClassVar[int]
    PROVIDERCONFIG_FIELD_NUMBER: _ClassVar[int]
    TOOLSERVERCONFIG_FIELD_NUMBER: _ClassVar[int]
    SKILLCONFIG_FIELD_NUMBER: _ClassVar[int]
    WORKSPACECONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTRAPACKAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    systemPrompt: str
    providerConfig: ProviderConfig
    toolServerConfig: _containers.RepeatedCompositeFieldContainer[ToolServerEntry]
    skillConfig: _containers.RepeatedCompositeFieldContainer[SkillRef]
    workspaceConfig: WorkspaceConfig
    extraPackage: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., systemPrompt: _Optional[str] = ..., providerConfig: _Optional[_Union[ProviderConfig, _Mapping]] = ..., toolServerConfig: _Optional[_Iterable[_Union[ToolServerEntry, _Mapping]]] = ..., skillConfig: _Optional[_Iterable[_Union[SkillRef, _Mapping]]] = ..., workspaceConfig: _Optional[_Union[WorkspaceConfig, _Mapping]] = ..., extraPackage: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteTemplateRequest(_message.Message):
    __slots__ = ("templateId",)
    TEMPLATEID_FIELD_NUMBER: _ClassVar[int]
    templateId: str
    def __init__(self, templateId: _Optional[str] = ...) -> None: ...

class DeleteTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SessionInfo(_message.Message):
    __slots__ = ("sessionId", "title", "state", "templateId", "createdAt", "updatedAt", "systemPrompt", "providerConfig", "toolServerConfig", "skillConfig", "workspaceConfig", "extraPackage", "workerId", "agentId", "sessionToken", "workspaceId", "inputTokens", "outputTokens", "lastActiveAt")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SYSTEMPROMPT_FIELD_NUMBER: _ClassVar[int]
    PROVIDERCONFIG_FIELD_NUMBER: _ClassVar[int]
    TOOLSERVERCONFIG_FIELD_NUMBER: _ClassVar[int]
    SKILLCONFIG_FIELD_NUMBER: _ClassVar[int]
    WORKSPACECONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTRAPACKAGE_FIELD_NUMBER: _ClassVar[int]
    WORKERID_FIELD_NUMBER: _ClassVar[int]
    AGENTID_FIELD_NUMBER: _ClassVar[int]
    SESSIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    WORKSPACEID_FIELD_NUMBER: _ClassVar[int]
    INPUTTOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTTOKENS_FIELD_NUMBER: _ClassVar[int]
    LASTACTIVEAT_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    title: str
    state: str
    templateId: str
    createdAt: int
    updatedAt: int
    systemPrompt: str
    providerConfig: ProviderConfig
    toolServerConfig: _containers.RepeatedCompositeFieldContainer[ToolServerEntry]
    skillConfig: _containers.RepeatedCompositeFieldContainer[SkillRef]
    workspaceConfig: WorkspaceConfig
    extraPackage: _containers.RepeatedScalarFieldContainer[str]
    workerId: str
    agentId: str
    sessionToken: str
    workspaceId: str
    inputTokens: int
    outputTokens: int
    lastActiveAt: int
    def __init__(self, sessionId: _Optional[str] = ..., title: _Optional[str] = ..., state: _Optional[str] = ..., templateId: _Optional[str] = ..., createdAt: _Optional[int] = ..., updatedAt: _Optional[int] = ..., systemPrompt: _Optional[str] = ..., providerConfig: _Optional[_Union[ProviderConfig, _Mapping]] = ..., toolServerConfig: _Optional[_Iterable[_Union[ToolServerEntry, _Mapping]]] = ..., skillConfig: _Optional[_Iterable[_Union[SkillRef, _Mapping]]] = ..., workspaceConfig: _Optional[_Union[WorkspaceConfig, _Mapping]] = ..., extraPackage: _Optional[_Iterable[str]] = ..., workerId: _Optional[str] = ..., agentId: _Optional[str] = ..., sessionToken: _Optional[str] = ..., workspaceId: _Optional[str] = ..., inputTokens: _Optional[int] = ..., outputTokens: _Optional[int] = ..., lastActiveAt: _Optional[int] = ...) -> None: ...

class ListSessionsRequest(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: str
    def __init__(self, state: _Optional[str] = ...) -> None: ...

class ListSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[SessionInfo]
    def __init__(self, sessions: _Optional[_Iterable[_Union[SessionInfo, _Mapping]]] = ...) -> None: ...

class GetSessionRequest(_message.Message):
    __slots__ = ("sessionId",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    def __init__(self, sessionId: _Optional[str] = ...) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ("title", "templateId", "systemPrompt", "providerConfig", "toolServerConfig", "skillConfig", "workspaceConfig", "extraPackage", "workspaceId")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEID_FIELD_NUMBER: _ClassVar[int]
    SYSTEMPROMPT_FIELD_NUMBER: _ClassVar[int]
    PROVIDERCONFIG_FIELD_NUMBER: _ClassVar[int]
    TOOLSERVERCONFIG_FIELD_NUMBER: _ClassVar[int]
    SKILLCONFIG_FIELD_NUMBER: _ClassVar[int]
    WORKSPACECONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTRAPACKAGE_FIELD_NUMBER: _ClassVar[int]
    WORKSPACEID_FIELD_NUMBER: _ClassVar[int]
    title: str
    templateId: str
    systemPrompt: str
    providerConfig: ProviderConfig
    toolServerConfig: _containers.RepeatedCompositeFieldContainer[ToolServerEntry]
    skillConfig: _containers.RepeatedCompositeFieldContainer[SkillRef]
    workspaceConfig: WorkspaceConfig
    extraPackage: _containers.RepeatedScalarFieldContainer[str]
    workspaceId: str
    def __init__(self, title: _Optional[str] = ..., templateId: _Optional[str] = ..., systemPrompt: _Optional[str] = ..., providerConfig: _Optional[_Union[ProviderConfig, _Mapping]] = ..., toolServerConfig: _Optional[_Iterable[_Union[ToolServerEntry, _Mapping]]] = ..., skillConfig: _Optional[_Iterable[_Union[SkillRef, _Mapping]]] = ..., workspaceConfig: _Optional[_Union[WorkspaceConfig, _Mapping]] = ..., extraPackage: _Optional[_Iterable[str]] = ..., workspaceId: _Optional[str] = ...) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ("sessionId", "sessionToken", "session")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SESSIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    sessionToken: str
    session: SessionInfo
    def __init__(self, sessionId: _Optional[str] = ..., sessionToken: _Optional[str] = ..., session: _Optional[_Union[SessionInfo, _Mapping]] = ...) -> None: ...

class UpdateSessionMetaRequest(_message.Message):
    __slots__ = ("sessionId", "title")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    title: str
    def __init__(self, sessionId: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class UpdateSessionHotConfigRequest(_message.Message):
    __slots__ = ("sessionId", "systemPrompt", "providerConfig", "skillConfig")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SYSTEMPROMPT_FIELD_NUMBER: _ClassVar[int]
    PROVIDERCONFIG_FIELD_NUMBER: _ClassVar[int]
    SKILLCONFIG_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    systemPrompt: str
    providerConfig: ProviderConfig
    skillConfig: _containers.RepeatedCompositeFieldContainer[SkillRef]
    def __init__(self, sessionId: _Optional[str] = ..., systemPrompt: _Optional[str] = ..., providerConfig: _Optional[_Union[ProviderConfig, _Mapping]] = ..., skillConfig: _Optional[_Iterable[_Union[SkillRef, _Mapping]]] = ...) -> None: ...

class UpdateSessionColdConfigRequest(_message.Message):
    __slots__ = ("sessionId", "toolServerConfig", "extraPackage")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    TOOLSERVERCONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTRAPACKAGE_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    toolServerConfig: _containers.RepeatedCompositeFieldContainer[ToolServerEntry]
    extraPackage: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sessionId: _Optional[str] = ..., toolServerConfig: _Optional[_Iterable[_Union[ToolServerEntry, _Mapping]]] = ..., extraPackage: _Optional[_Iterable[str]] = ...) -> None: ...

class SwitchSessionTemplateRequest(_message.Message):
    __slots__ = ("sessionId", "templateId")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    templateId: str
    def __init__(self, sessionId: _Optional[str] = ..., templateId: _Optional[str] = ...) -> None: ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ("sessionId",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    def __init__(self, sessionId: _Optional[str] = ...) -> None: ...

class DeleteSessionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartSessionRequest(_message.Message):
    __slots__ = ("sessionId",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    def __init__(self, sessionId: _Optional[str] = ...) -> None: ...

class StartSessionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StopSessionRequest(_message.Message):
    __slots__ = ("sessionId",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    def __init__(self, sessionId: _Optional[str] = ...) -> None: ...

class StopSessionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResolveSessionRequest(_message.Message):
    __slots__ = ("sessionToken",)
    SESSIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    sessionToken: str
    def __init__(self, sessionToken: _Optional[str] = ...) -> None: ...

class ToolServerUrl(_message.Message):
    __slots__ = ("name", "url", "config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    url: str
    config: str
    def __init__(self, name: _Optional[str] = ..., url: _Optional[str] = ..., config: _Optional[str] = ...) -> None: ...

class ResolveSessionResponse(_message.Message):
    __slots__ = ("sessionId", "templateId", "systemPrompt", "providerConfig", "toolServerConfig", "skillConfig", "extraPackage", "workerId", "workerUrl", "workerSecret", "workspaceRoot", "agentUrl", "toolServerUrls", "workspaceId")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEID_FIELD_NUMBER: _ClassVar[int]
    SYSTEMPROMPT_FIELD_NUMBER: _ClassVar[int]
    PROVIDERCONFIG_FIELD_NUMBER: _ClassVar[int]
    TOOLSERVERCONFIG_FIELD_NUMBER: _ClassVar[int]
    SKILLCONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTRAPACKAGE_FIELD_NUMBER: _ClassVar[int]
    WORKERID_FIELD_NUMBER: _ClassVar[int]
    WORKERURL_FIELD_NUMBER: _ClassVar[int]
    WORKERSECRET_FIELD_NUMBER: _ClassVar[int]
    WORKSPACEROOT_FIELD_NUMBER: _ClassVar[int]
    AGENTURL_FIELD_NUMBER: _ClassVar[int]
    TOOLSERVERURLS_FIELD_NUMBER: _ClassVar[int]
    WORKSPACEID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    templateId: str
    systemPrompt: str
    providerConfig: ProviderConfig
    toolServerConfig: _containers.RepeatedCompositeFieldContainer[ToolServerEntry]
    skillConfig: _containers.RepeatedCompositeFieldContainer[SkillRef]
    extraPackage: _containers.RepeatedScalarFieldContainer[str]
    workerId: str
    workerUrl: str
    workerSecret: str
    workspaceRoot: str
    agentUrl: str
    toolServerUrls: _containers.RepeatedCompositeFieldContainer[ToolServerUrl]
    workspaceId: str
    def __init__(self, sessionId: _Optional[str] = ..., templateId: _Optional[str] = ..., systemPrompt: _Optional[str] = ..., providerConfig: _Optional[_Union[ProviderConfig, _Mapping]] = ..., toolServerConfig: _Optional[_Iterable[_Union[ToolServerEntry, _Mapping]]] = ..., skillConfig: _Optional[_Iterable[_Union[SkillRef, _Mapping]]] = ..., extraPackage: _Optional[_Iterable[str]] = ..., workerId: _Optional[str] = ..., workerUrl: _Optional[str] = ..., workerSecret: _Optional[str] = ..., workspaceRoot: _Optional[str] = ..., agentUrl: _Optional[str] = ..., toolServerUrls: _Optional[_Iterable[_Union[ToolServerUrl, _Mapping]]] = ..., workspaceId: _Optional[str] = ...) -> None: ...

class MessageInfo(_message.Message):
    __slots__ = ("id", "sessionId", "role", "parentMessageId", "toolCallId", "toolName", "content", "tokenUsage", "metadata", "compacted", "createdAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PARENTMESSAGEID_FIELD_NUMBER: _ClassVar[int]
    TOOLCALLID_FIELD_NUMBER: _ClassVar[int]
    TOOLNAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TOKENUSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    COMPACTED_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    sessionId: str
    role: str
    parentMessageId: str
    toolCallId: str
    toolName: str
    content: str
    tokenUsage: str
    metadata: str
    compacted: bool
    createdAt: int
    def __init__(self, id: _Optional[str] = ..., sessionId: _Optional[str] = ..., role: _Optional[str] = ..., parentMessageId: _Optional[str] = ..., toolCallId: _Optional[str] = ..., toolName: _Optional[str] = ..., content: _Optional[str] = ..., tokenUsage: _Optional[str] = ..., metadata: _Optional[str] = ..., compacted: _Optional[bool] = ..., createdAt: _Optional[int] = ...) -> None: ...

class ListMessagesRequest(_message.Message):
    __slots__ = ("sessionId", "limit", "beforeId")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    BEFOREID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    limit: int
    beforeId: str
    def __init__(self, sessionId: _Optional[str] = ..., limit: _Optional[int] = ..., beforeId: _Optional[str] = ...) -> None: ...

class ListMessagesResponse(_message.Message):
    __slots__ = ("messages", "hasMore", "nextBeforeId")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    HASMORE_FIELD_NUMBER: _ClassVar[int]
    NEXTBEFOREID_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[MessageInfo]
    hasMore: bool
    nextBeforeId: str
    def __init__(self, messages: _Optional[_Iterable[_Union[MessageInfo, _Mapping]]] = ..., hasMore: _Optional[bool] = ..., nextBeforeId: _Optional[str] = ...) -> None: ...

class CreateMessageRequest(_message.Message):
    __slots__ = ("sessionId", "role", "parentMessageId", "toolCallId", "toolName", "content", "tokenUsage", "metadata")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PARENTMESSAGEID_FIELD_NUMBER: _ClassVar[int]
    TOOLCALLID_FIELD_NUMBER: _ClassVar[int]
    TOOLNAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TOKENUSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    role: str
    parentMessageId: str
    toolCallId: str
    toolName: str
    content: str
    tokenUsage: str
    metadata: str
    def __init__(self, sessionId: _Optional[str] = ..., role: _Optional[str] = ..., parentMessageId: _Optional[str] = ..., toolCallId: _Optional[str] = ..., toolName: _Optional[str] = ..., content: _Optional[str] = ..., tokenUsage: _Optional[str] = ..., metadata: _Optional[str] = ...) -> None: ...

class CreateMessageResponse(_message.Message):
    __slots__ = ("messageId",)
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    messageId: str
    def __init__(self, messageId: _Optional[str] = ...) -> None: ...

class DeleteMessagesFromRequest(_message.Message):
    __slots__ = ("sessionId", "messageId")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    messageId: str
    def __init__(self, sessionId: _Optional[str] = ..., messageId: _Optional[str] = ...) -> None: ...

class DeleteMessagesFromResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
