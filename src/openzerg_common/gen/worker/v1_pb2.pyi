from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExecRequest(_message.Message):
    __slots__ = ("command", "workdir", "env", "timeoutMs")
    class EnvEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKDIR_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    TIMEOUTMS_FIELD_NUMBER: _ClassVar[int]
    command: str
    workdir: str
    env: _containers.ScalarMap[str, str]
    timeoutMs: int
    def __init__(self, command: _Optional[str] = ..., workdir: _Optional[str] = ..., env: _Optional[_Mapping[str, str]] = ..., timeoutMs: _Optional[int] = ...) -> None: ...

class ExecResponse(_message.Message):
    __slots__ = ("exitCode", "stdout", "stderr", "timedOut")
    EXITCODE_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    TIMEDOUT_FIELD_NUMBER: _ClassVar[int]
    exitCode: int
    stdout: bytes
    stderr: bytes
    timedOut: bool
    def __init__(self, exitCode: _Optional[int] = ..., stdout: _Optional[bytes] = ..., stderr: _Optional[bytes] = ..., timedOut: _Optional[bool] = ...) -> None: ...

class SpawnRequest(_message.Message):
    __slots__ = ("jobId", "command", "workdir", "env")
    class EnvEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    JOBID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKDIR_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    jobId: str
    command: str
    workdir: str
    env: _containers.ScalarMap[str, str]
    def __init__(self, jobId: _Optional[str] = ..., command: _Optional[str] = ..., workdir: _Optional[str] = ..., env: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SpawnResponse(_message.Message):
    __slots__ = ("started", "error")
    STARTED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    started: bool
    error: str
    def __init__(self, started: _Optional[bool] = ..., error: _Optional[str] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("content", "mtimeMs")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MTIMEMS_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    mtimeMs: int
    def __init__(self, content: _Optional[bytes] = ..., mtimeMs: _Optional[int] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("path", "content", "expectedMtimeMs")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXPECTEDMTIMEMS_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: bytes
    expectedMtimeMs: int
    def __init__(self, path: _Optional[str] = ..., content: _Optional[bytes] = ..., expectedMtimeMs: _Optional[int] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("actualMtimeMs",)
    ACTUALMTIMEMS_FIELD_NUMBER: _ClassVar[int]
    actualMtimeMs: int
    def __init__(self, actualMtimeMs: _Optional[int] = ...) -> None: ...

class StatRequest(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class StatResponse(_message.Message):
    __slots__ = ("exists", "isFile", "isDir", "size", "mtimeMs")
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    ISFILE_FIELD_NUMBER: _ClassVar[int]
    ISDIR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MTIMEMS_FIELD_NUMBER: _ClassVar[int]
    exists: bool
    isFile: bool
    isDir: bool
    size: int
    mtimeMs: int
    def __init__(self, exists: _Optional[bool] = ..., isFile: _Optional[bool] = ..., isDir: _Optional[bool] = ..., size: _Optional[int] = ..., mtimeMs: _Optional[int] = ...) -> None: ...

class InstallPackagesRequest(_message.Message):
    __slots__ = ("packages",)
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    packages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, packages: _Optional[_Iterable[str]] = ...) -> None: ...

class InstallPackagesResponse(_message.Message):
    __slots__ = ("installed", "failed", "envShPath")
    INSTALLED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    ENVSHPATH_FIELD_NUMBER: _ClassVar[int]
    installed: _containers.RepeatedScalarFieldContainer[str]
    failed: _containers.RepeatedScalarFieldContainer[str]
    envShPath: str
    def __init__(self, installed: _Optional[_Iterable[str]] = ..., failed: _Optional[_Iterable[str]] = ..., envShPath: _Optional[str] = ...) -> None: ...

class HealthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HealthResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
