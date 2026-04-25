from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WmWorkspaceInfo(_message.Message):
    __slots__ = ("workspaceId", "volumeName", "state", "createdBySessionId", "createdAt", "workerPodName", "skillSlugs", "nixPkgs")
    WORKSPACEID_FIELD_NUMBER: _ClassVar[int]
    VOLUMENAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATEDBYSESSIONID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    WORKERPODNAME_FIELD_NUMBER: _ClassVar[int]
    SKILLSLUGS_FIELD_NUMBER: _ClassVar[int]
    NIXPKGS_FIELD_NUMBER: _ClassVar[int]
    workspaceId: str
    volumeName: str
    state: str
    createdBySessionId: str
    createdAt: int
    workerPodName: str
    skillSlugs: str
    nixPkgs: str
    def __init__(self, workspaceId: _Optional[str] = ..., volumeName: _Optional[str] = ..., state: _Optional[str] = ..., createdBySessionId: _Optional[str] = ..., createdAt: _Optional[int] = ..., workerPodName: _Optional[str] = ..., skillSlugs: _Optional[str] = ..., nixPkgs: _Optional[str] = ...) -> None: ...

class WmWorkerInfo(_message.Message):
    __slots__ = ("workerId", "sessionId", "containerName", "image", "state", "podmanId", "secret", "workspaceRoot", "filesystemUrl", "executionUrl", "createdAt", "workspaceId")
    WORKERID_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    CONTAINERNAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PODMANID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    WORKSPACEROOT_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEMURL_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONURL_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACEID_FIELD_NUMBER: _ClassVar[int]
    workerId: str
    sessionId: str
    containerName: str
    image: str
    state: str
    podmanId: str
    secret: str
    workspaceRoot: str
    filesystemUrl: str
    executionUrl: str
    createdAt: int
    workspaceId: str
    def __init__(self, workerId: _Optional[str] = ..., sessionId: _Optional[str] = ..., containerName: _Optional[str] = ..., image: _Optional[str] = ..., state: _Optional[str] = ..., podmanId: _Optional[str] = ..., secret: _Optional[str] = ..., workspaceRoot: _Optional[str] = ..., filesystemUrl: _Optional[str] = ..., executionUrl: _Optional[str] = ..., createdAt: _Optional[int] = ..., workspaceId: _Optional[str] = ...) -> None: ...

class ContainerVolume(_message.Message):
    __slots__ = ("name", "destination")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination: str
    def __init__(self, name: _Optional[str] = ..., destination: _Optional[str] = ...) -> None: ...

class CreateWorkspaceRequest(_message.Message):
    __slots__ = ("sessionId",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    def __init__(self, sessionId: _Optional[str] = ...) -> None: ...

class CreateWorkspaceResponse(_message.Message):
    __slots__ = ("workspaceId", "volumeName")
    WORKSPACEID_FIELD_NUMBER: _ClassVar[int]
    VOLUMENAME_FIELD_NUMBER: _ClassVar[int]
    workspaceId: str
    volumeName: str
    def __init__(self, workspaceId: _Optional[str] = ..., volumeName: _Optional[str] = ...) -> None: ...

class ListWorkspacesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListWorkspacesResponse(_message.Message):
    __slots__ = ("workspaces",)
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    workspaces: _containers.RepeatedCompositeFieldContainer[WmWorkspaceInfo]
    def __init__(self, workspaces: _Optional[_Iterable[_Union[WmWorkspaceInfo, _Mapping]]] = ...) -> None: ...

class GetWorkspaceRequest(_message.Message):
    __slots__ = ("workspaceId",)
    WORKSPACEID_FIELD_NUMBER: _ClassVar[int]
    workspaceId: str
    def __init__(self, workspaceId: _Optional[str] = ...) -> None: ...

class DeleteWorkspaceRequest(_message.Message):
    __slots__ = ("workspaceId",)
    WORKSPACEID_FIELD_NUMBER: _ClassVar[int]
    workspaceId: str
    def __init__(self, workspaceId: _Optional[str] = ...) -> None: ...

class DeleteWorkspaceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartWorkerRequest(_message.Message):
    __slots__ = ("sessionId", "image", "env", "volumes", "command")
    class EnvEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    image: str
    env: _containers.ScalarMap[str, str]
    volumes: _containers.RepeatedCompositeFieldContainer[ContainerVolume]
    command: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sessionId: _Optional[str] = ..., image: _Optional[str] = ..., env: _Optional[_Mapping[str, str]] = ..., volumes: _Optional[_Iterable[_Union[ContainerVolume, _Mapping]]] = ..., command: _Optional[_Iterable[str]] = ...) -> None: ...

class StartWorkerResponse(_message.Message):
    __slots__ = ("workerId", "containerName", "secret")
    WORKERID_FIELD_NUMBER: _ClassVar[int]
    CONTAINERNAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    workerId: str
    containerName: str
    secret: str
    def __init__(self, workerId: _Optional[str] = ..., containerName: _Optional[str] = ..., secret: _Optional[str] = ...) -> None: ...

class StopWorkerRequest(_message.Message):
    __slots__ = ("workerId",)
    WORKERID_FIELD_NUMBER: _ClassVar[int]
    workerId: str
    def __init__(self, workerId: _Optional[str] = ...) -> None: ...

class StopWorkerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetWorkerStatusRequest(_message.Message):
    __slots__ = ("workerId",)
    WORKERID_FIELD_NUMBER: _ClassVar[int]
    workerId: str
    def __init__(self, workerId: _Optional[str] = ...) -> None: ...

class GetWorkerStatusResponse(_message.Message):
    __slots__ = ("state", "containerId")
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONTAINERID_FIELD_NUMBER: _ClassVar[int]
    state: str
    containerId: str
    def __init__(self, state: _Optional[str] = ..., containerId: _Optional[str] = ...) -> None: ...

class ListWorkersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListWorkersResponse(_message.Message):
    __slots__ = ("workers",)
    WORKERS_FIELD_NUMBER: _ClassVar[int]
    workers: _containers.RepeatedCompositeFieldContainer[WmWorkerInfo]
    def __init__(self, workers: _Optional[_Iterable[_Union[WmWorkerInfo, _Mapping]]] = ...) -> None: ...

class EnsureWorkspaceWorkerRequest(_message.Message):
    __slots__ = ("workspaceId", "image", "env")
    class EnvEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    WORKSPACEID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    workspaceId: str
    image: str
    env: _containers.ScalarMap[str, str]
    def __init__(self, workspaceId: _Optional[str] = ..., image: _Optional[str] = ..., env: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EnsureWorkspaceWorkerResponse(_message.Message):
    __slots__ = ("workerId", "containerName", "secret", "volumeName")
    WORKERID_FIELD_NUMBER: _ClassVar[int]
    CONTAINERNAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    VOLUMENAME_FIELD_NUMBER: _ClassVar[int]
    workerId: str
    containerName: str
    secret: str
    volumeName: str
    def __init__(self, workerId: _Optional[str] = ..., containerName: _Optional[str] = ..., secret: _Optional[str] = ..., volumeName: _Optional[str] = ...) -> None: ...

class UpdateWorkspaceConfigRequest(_message.Message):
    __slots__ = ("workspaceId", "skillSlugs", "nixPkgs")
    WORKSPACEID_FIELD_NUMBER: _ClassVar[int]
    SKILLSLUGS_FIELD_NUMBER: _ClassVar[int]
    NIXPKGS_FIELD_NUMBER: _ClassVar[int]
    workspaceId: str
    skillSlugs: str
    nixPkgs: str
    def __init__(self, workspaceId: _Optional[str] = ..., skillSlugs: _Optional[str] = ..., nixPkgs: _Optional[str] = ...) -> None: ...

class UpdateWorkspaceConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HealthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HealthResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
