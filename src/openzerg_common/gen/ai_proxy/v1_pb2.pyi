from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListProxiesRequest(_message.Message):
    __slots__ = ("enabledOnly",)
    ENABLEDONLY_FIELD_NUMBER: _ClassVar[int]
    enabledOnly: bool
    def __init__(self, enabledOnly: _Optional[bool] = ...) -> None: ...

class ProxyInfo(_message.Message):
    __slots__ = ("id", "sourceModel", "providerModelConfigId", "apiKey", "enabled", "createdAt", "updatedAt", "providerId", "providerName", "modelId", "modelName", "upstream", "targetModel", "supportStreaming", "supportTools", "supportVision", "supportReasoning", "defaultMaxTokens", "contextLength", "autoCompactLength")
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCEMODEL_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODELCONFIGID_FIELD_NUMBER: _ClassVar[int]
    APIKEY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERNAME_FIELD_NUMBER: _ClassVar[int]
    MODELID_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    UPSTREAM_FIELD_NUMBER: _ClassVar[int]
    TARGETMODEL_FIELD_NUMBER: _ClassVar[int]
    SUPPORTSTREAMING_FIELD_NUMBER: _ClassVar[int]
    SUPPORTTOOLS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTVISION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTREASONING_FIELD_NUMBER: _ClassVar[int]
    DEFAULTMAXTOKENS_FIELD_NUMBER: _ClassVar[int]
    CONTEXTLENGTH_FIELD_NUMBER: _ClassVar[int]
    AUTOCOMPACTLENGTH_FIELD_NUMBER: _ClassVar[int]
    id: str
    sourceModel: str
    providerModelConfigId: str
    apiKey: str
    enabled: bool
    createdAt: int
    updatedAt: int
    providerId: str
    providerName: str
    modelId: str
    modelName: str
    upstream: str
    targetModel: str
    supportStreaming: bool
    supportTools: bool
    supportVision: bool
    supportReasoning: bool
    defaultMaxTokens: int
    contextLength: int
    autoCompactLength: int
    def __init__(self, id: _Optional[str] = ..., sourceModel: _Optional[str] = ..., providerModelConfigId: _Optional[str] = ..., apiKey: _Optional[str] = ..., enabled: _Optional[bool] = ..., createdAt: _Optional[int] = ..., updatedAt: _Optional[int] = ..., providerId: _Optional[str] = ..., providerName: _Optional[str] = ..., modelId: _Optional[str] = ..., modelName: _Optional[str] = ..., upstream: _Optional[str] = ..., targetModel: _Optional[str] = ..., supportStreaming: _Optional[bool] = ..., supportTools: _Optional[bool] = ..., supportVision: _Optional[bool] = ..., supportReasoning: _Optional[bool] = ..., defaultMaxTokens: _Optional[int] = ..., contextLength: _Optional[int] = ..., autoCompactLength: _Optional[int] = ...) -> None: ...

class ListProxiesResponse(_message.Message):
    __slots__ = ("proxies",)
    PROXIES_FIELD_NUMBER: _ClassVar[int]
    proxies: _containers.RepeatedCompositeFieldContainer[ProxyInfo]
    def __init__(self, proxies: _Optional[_Iterable[_Union[ProxyInfo, _Mapping]]] = ...) -> None: ...

class GetProxyRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CreateProxyRequest(_message.Message):
    __slots__ = ("sourceModel", "providerModelConfigId")
    SOURCEMODEL_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODELCONFIGID_FIELD_NUMBER: _ClassVar[int]
    sourceModel: str
    providerModelConfigId: str
    def __init__(self, sourceModel: _Optional[str] = ..., providerModelConfigId: _Optional[str] = ...) -> None: ...

class UpdateProxyRequest(_message.Message):
    __slots__ = ("id", "sourceModel", "providerModelConfigId", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCEMODEL_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODELCONFIGID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    sourceModel: str
    providerModelConfigId: str
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., sourceModel: _Optional[str] = ..., providerModelConfigId: _Optional[str] = ..., enabled: _Optional[bool] = ...) -> None: ...

class DeleteProxyRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteProxyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProviderModelConfigsRequest(_message.Message):
    __slots__ = ("enabledOnly",)
    ENABLEDONLY_FIELD_NUMBER: _ClassVar[int]
    enabledOnly: bool
    def __init__(self, enabledOnly: _Optional[bool] = ...) -> None: ...

class ProviderModelConfigInfo(_message.Message):
    __slots__ = ("id", "providerId", "providerName", "modelId", "modelName", "upstream", "apiKey", "supportStreaming", "supportTools", "supportVision", "supportReasoning", "defaultMaxTokens", "contextLength", "autoCompactLength", "enabled", "createdAt", "updatedAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERNAME_FIELD_NUMBER: _ClassVar[int]
    MODELID_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    UPSTREAM_FIELD_NUMBER: _ClassVar[int]
    APIKEY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTSTREAMING_FIELD_NUMBER: _ClassVar[int]
    SUPPORTTOOLS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTVISION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTREASONING_FIELD_NUMBER: _ClassVar[int]
    DEFAULTMAXTOKENS_FIELD_NUMBER: _ClassVar[int]
    CONTEXTLENGTH_FIELD_NUMBER: _ClassVar[int]
    AUTOCOMPACTLENGTH_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    providerId: str
    providerName: str
    modelId: str
    modelName: str
    upstream: str
    apiKey: str
    supportStreaming: bool
    supportTools: bool
    supportVision: bool
    supportReasoning: bool
    defaultMaxTokens: int
    contextLength: int
    autoCompactLength: int
    enabled: bool
    createdAt: int
    updatedAt: int
    def __init__(self, id: _Optional[str] = ..., providerId: _Optional[str] = ..., providerName: _Optional[str] = ..., modelId: _Optional[str] = ..., modelName: _Optional[str] = ..., upstream: _Optional[str] = ..., apiKey: _Optional[str] = ..., supportStreaming: _Optional[bool] = ..., supportTools: _Optional[bool] = ..., supportVision: _Optional[bool] = ..., supportReasoning: _Optional[bool] = ..., defaultMaxTokens: _Optional[int] = ..., contextLength: _Optional[int] = ..., autoCompactLength: _Optional[int] = ..., enabled: _Optional[bool] = ..., createdAt: _Optional[int] = ..., updatedAt: _Optional[int] = ...) -> None: ...

class ListProviderModelConfigsResponse(_message.Message):
    __slots__ = ("configs",)
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[ProviderModelConfigInfo]
    def __init__(self, configs: _Optional[_Iterable[_Union[ProviderModelConfigInfo, _Mapping]]] = ...) -> None: ...

class GetProviderModelConfigRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CreateProviderModelConfigRequest(_message.Message):
    __slots__ = ("providerId", "providerName", "modelId", "modelName", "upstream", "apiKey", "supportStreaming", "supportTools", "supportVision", "supportReasoning", "defaultMaxTokens", "contextLength", "autoCompactLength")
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERNAME_FIELD_NUMBER: _ClassVar[int]
    MODELID_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    UPSTREAM_FIELD_NUMBER: _ClassVar[int]
    APIKEY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTSTREAMING_FIELD_NUMBER: _ClassVar[int]
    SUPPORTTOOLS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTVISION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTREASONING_FIELD_NUMBER: _ClassVar[int]
    DEFAULTMAXTOKENS_FIELD_NUMBER: _ClassVar[int]
    CONTEXTLENGTH_FIELD_NUMBER: _ClassVar[int]
    AUTOCOMPACTLENGTH_FIELD_NUMBER: _ClassVar[int]
    providerId: str
    providerName: str
    modelId: str
    modelName: str
    upstream: str
    apiKey: str
    supportStreaming: bool
    supportTools: bool
    supportVision: bool
    supportReasoning: bool
    defaultMaxTokens: int
    contextLength: int
    autoCompactLength: int
    def __init__(self, providerId: _Optional[str] = ..., providerName: _Optional[str] = ..., modelId: _Optional[str] = ..., modelName: _Optional[str] = ..., upstream: _Optional[str] = ..., apiKey: _Optional[str] = ..., supportStreaming: _Optional[bool] = ..., supportTools: _Optional[bool] = ..., supportVision: _Optional[bool] = ..., supportReasoning: _Optional[bool] = ..., defaultMaxTokens: _Optional[int] = ..., contextLength: _Optional[int] = ..., autoCompactLength: _Optional[int] = ...) -> None: ...

class UpdateProviderModelConfigRequest(_message.Message):
    __slots__ = ("id", "providerName", "modelName", "upstream", "apiKey", "supportStreaming", "supportTools", "supportVision", "supportReasoning", "defaultMaxTokens", "contextLength", "autoCompactLength", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERNAME_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    UPSTREAM_FIELD_NUMBER: _ClassVar[int]
    APIKEY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTSTREAMING_FIELD_NUMBER: _ClassVar[int]
    SUPPORTTOOLS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTVISION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTREASONING_FIELD_NUMBER: _ClassVar[int]
    DEFAULTMAXTOKENS_FIELD_NUMBER: _ClassVar[int]
    CONTEXTLENGTH_FIELD_NUMBER: _ClassVar[int]
    AUTOCOMPACTLENGTH_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    providerName: str
    modelName: str
    upstream: str
    apiKey: str
    supportStreaming: bool
    supportTools: bool
    supportVision: bool
    supportReasoning: bool
    defaultMaxTokens: int
    contextLength: int
    autoCompactLength: int
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., providerName: _Optional[str] = ..., modelName: _Optional[str] = ..., upstream: _Optional[str] = ..., apiKey: _Optional[str] = ..., supportStreaming: _Optional[bool] = ..., supportTools: _Optional[bool] = ..., supportVision: _Optional[bool] = ..., supportReasoning: _Optional[bool] = ..., defaultMaxTokens: _Optional[int] = ..., contextLength: _Optional[int] = ..., autoCompactLength: _Optional[int] = ..., enabled: _Optional[bool] = ...) -> None: ...

class DeleteProviderModelConfigRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteProviderModelConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProvidersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProviderInfo(_message.Message):
    __slots__ = ("id", "name", "api", "doc", "env")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    DOC_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    api: str
    doc: str
    env: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., api: _Optional[str] = ..., doc: _Optional[str] = ..., env: _Optional[_Iterable[str]] = ...) -> None: ...

class ListProvidersResponse(_message.Message):
    __slots__ = ("providers",)
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[ProviderInfo]
    def __init__(self, providers: _Optional[_Iterable[_Union[ProviderInfo, _Mapping]]] = ...) -> None: ...

class ListProviderModelsRequest(_message.Message):
    __slots__ = ("providerId",)
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    providerId: str
    def __init__(self, providerId: _Optional[str] = ...) -> None: ...

class ProviderModelInfo(_message.Message):
    __slots__ = ("providerId", "providerName", "modelId", "modelName", "upstream", "supportStreaming", "supportTools", "supportVision", "supportReasoning", "defaultMaxTokens", "contextLength", "autoCompactLength", "status")
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERNAME_FIELD_NUMBER: _ClassVar[int]
    MODELID_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    UPSTREAM_FIELD_NUMBER: _ClassVar[int]
    SUPPORTSTREAMING_FIELD_NUMBER: _ClassVar[int]
    SUPPORTTOOLS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTVISION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTREASONING_FIELD_NUMBER: _ClassVar[int]
    DEFAULTMAXTOKENS_FIELD_NUMBER: _ClassVar[int]
    CONTEXTLENGTH_FIELD_NUMBER: _ClassVar[int]
    AUTOCOMPACTLENGTH_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    providerId: str
    providerName: str
    modelId: str
    modelName: str
    upstream: str
    supportStreaming: bool
    supportTools: bool
    supportVision: bool
    supportReasoning: bool
    defaultMaxTokens: int
    contextLength: int
    autoCompactLength: int
    status: str
    def __init__(self, providerId: _Optional[str] = ..., providerName: _Optional[str] = ..., modelId: _Optional[str] = ..., modelName: _Optional[str] = ..., upstream: _Optional[str] = ..., supportStreaming: _Optional[bool] = ..., supportTools: _Optional[bool] = ..., supportVision: _Optional[bool] = ..., supportReasoning: _Optional[bool] = ..., defaultMaxTokens: _Optional[int] = ..., contextLength: _Optional[int] = ..., autoCompactLength: _Optional[int] = ..., status: _Optional[str] = ...) -> None: ...

class ListProviderModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[ProviderModelInfo]
    def __init__(self, models: _Optional[_Iterable[_Union[ProviderModelInfo, _Mapping]]] = ...) -> None: ...

class TestProviderModelConfigRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class TestProviderModelConfigResponse(_message.Message):
    __slots__ = ("success", "message", "statusCode", "latencyMs")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    LATENCYMS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    statusCode: int
    latencyMs: int
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., statusCode: _Optional[int] = ..., latencyMs: _Optional[int] = ...) -> None: ...

class TestProxyRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class TestProxyResponse(_message.Message):
    __slots__ = ("success", "message", "statusCode", "latencyMs")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    LATENCYMS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    statusCode: int
    latencyMs: int
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., statusCode: _Optional[int] = ..., latencyMs: _Optional[int] = ...) -> None: ...

class QueryLogsRequest(_message.Message):
    __slots__ = ("proxyId", "fromTs", "toTs", "limit", "offset")
    PROXYID_FIELD_NUMBER: _ClassVar[int]
    FROMTS_FIELD_NUMBER: _ClassVar[int]
    TOTS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    proxyId: str
    fromTs: int
    toTs: int
    limit: int
    offset: int
    def __init__(self, proxyId: _Optional[str] = ..., fromTs: _Optional[int] = ..., toTs: _Optional[int] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class LogEntry(_message.Message):
    __slots__ = ("id", "proxyId", "sourceModel", "targetModel", "upstream", "inputTokens", "outputTokens", "totalTokens", "durationMs", "timeToFirstTokenMs", "isStream", "isSuccess", "errorMessage", "createdAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROXYID_FIELD_NUMBER: _ClassVar[int]
    SOURCEMODEL_FIELD_NUMBER: _ClassVar[int]
    TARGETMODEL_FIELD_NUMBER: _ClassVar[int]
    UPSTREAM_FIELD_NUMBER: _ClassVar[int]
    INPUTTOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTTOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTALTOKENS_FIELD_NUMBER: _ClassVar[int]
    DURATIONMS_FIELD_NUMBER: _ClassVar[int]
    TIMETOFIRSTTOKENMS_FIELD_NUMBER: _ClassVar[int]
    ISSTREAM_FIELD_NUMBER: _ClassVar[int]
    ISSUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    proxyId: str
    sourceModel: str
    targetModel: str
    upstream: str
    inputTokens: int
    outputTokens: int
    totalTokens: int
    durationMs: int
    timeToFirstTokenMs: int
    isStream: bool
    isSuccess: bool
    errorMessage: str
    createdAt: int
    def __init__(self, id: _Optional[str] = ..., proxyId: _Optional[str] = ..., sourceModel: _Optional[str] = ..., targetModel: _Optional[str] = ..., upstream: _Optional[str] = ..., inputTokens: _Optional[int] = ..., outputTokens: _Optional[int] = ..., totalTokens: _Optional[int] = ..., durationMs: _Optional[int] = ..., timeToFirstTokenMs: _Optional[int] = ..., isStream: _Optional[bool] = ..., isSuccess: _Optional[bool] = ..., errorMessage: _Optional[str] = ..., createdAt: _Optional[int] = ...) -> None: ...

class QueryLogsResponse(_message.Message):
    __slots__ = ("logs", "total")
    LOGS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    logs: _containers.RepeatedCompositeFieldContainer[LogEntry]
    total: int
    def __init__(self, logs: _Optional[_Iterable[_Union[LogEntry, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class GetTokenStatsRequest(_message.Message):
    __slots__ = ("proxyId", "fromTs", "toTs")
    PROXYID_FIELD_NUMBER: _ClassVar[int]
    FROMTS_FIELD_NUMBER: _ClassVar[int]
    TOTS_FIELD_NUMBER: _ClassVar[int]
    proxyId: str
    fromTs: int
    toTs: int
    def __init__(self, proxyId: _Optional[str] = ..., fromTs: _Optional[int] = ..., toTs: _Optional[int] = ...) -> None: ...

class TokenStatsResponse(_message.Message):
    __slots__ = ("totalInputTokens", "totalOutputTokens", "totalTokens", "requestCount")
    TOTALINPUTTOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTALOUTPUTTOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTALTOKENS_FIELD_NUMBER: _ClassVar[int]
    REQUESTCOUNT_FIELD_NUMBER: _ClassVar[int]
    totalInputTokens: int
    totalOutputTokens: int
    totalTokens: int
    requestCount: int
    def __init__(self, totalInputTokens: _Optional[int] = ..., totalOutputTokens: _Optional[int] = ..., totalTokens: _Optional[int] = ..., requestCount: _Optional[int] = ...) -> None: ...
