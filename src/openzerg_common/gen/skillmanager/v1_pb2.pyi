from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterSkillRequest(_message.Message):
    __slots__ = ("slug", "gitUrl")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    GITURL_FIELD_NUMBER: _ClassVar[int]
    slug: str
    gitUrl: str
    def __init__(self, slug: _Optional[str] = ..., gitUrl: _Optional[str] = ...) -> None: ...

class SkillInfo(_message.Message):
    __slots__ = ("id", "slug", "name", "description", "gitUrl", "localPath", "commitHash", "pkgs", "createdAt", "updatedAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GITURL_FIELD_NUMBER: _ClassVar[int]
    LOCALPATH_FIELD_NUMBER: _ClassVar[int]
    COMMITHASH_FIELD_NUMBER: _ClassVar[int]
    PKGS_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    slug: str
    name: str
    description: str
    gitUrl: str
    localPath: str
    commitHash: str
    pkgs: str
    createdAt: int
    updatedAt: int
    def __init__(self, id: _Optional[str] = ..., slug: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., gitUrl: _Optional[str] = ..., localPath: _Optional[str] = ..., commitHash: _Optional[str] = ..., pkgs: _Optional[str] = ..., createdAt: _Optional[int] = ..., updatedAt: _Optional[int] = ...) -> None: ...

class RegisterSkillResponse(_message.Message):
    __slots__ = ("skill",)
    SKILL_FIELD_NUMBER: _ClassVar[int]
    skill: SkillInfo
    def __init__(self, skill: _Optional[_Union[SkillInfo, _Mapping]] = ...) -> None: ...

class UpdateSkillRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class UpdateSkillResponse(_message.Message):
    __slots__ = ("skill",)
    SKILL_FIELD_NUMBER: _ClassVar[int]
    skill: SkillInfo
    def __init__(self, skill: _Optional[_Union[SkillInfo, _Mapping]] = ...) -> None: ...

class DeleteSkillRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class DeleteSkillResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSkillsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSkillsResponse(_message.Message):
    __slots__ = ("skills",)
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedCompositeFieldContainer[SkillInfo]
    def __init__(self, skills: _Optional[_Iterable[_Union[SkillInfo, _Mapping]]] = ...) -> None: ...

class GetSkillRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...
