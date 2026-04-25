from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChatRequest(_message.Message):
    __slots__ = ("sessionId", "content")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    content: str
    def __init__(self, sessionId: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class ChatResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InterruptRequest(_message.Message):
    __slots__ = ("sessionId",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    def __init__(self, sessionId: _Optional[str] = ...) -> None: ...

class InterruptResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class DeleteMessagesFromRequest(_message.Message):
    __slots__ = ("sessionId", "messageId")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    messageId: str
    def __init__(self, sessionId: _Optional[str] = ..., messageId: _Optional[str] = ...) -> None: ...

class DeleteMessagesFromResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: int
    def __init__(self, deleted: _Optional[int] = ...) -> None: ...

class SubscribeEventsRequest(_message.Message):
    __slots__ = ("sessionId",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    def __init__(self, sessionId: _Optional[str] = ...) -> None: ...

class SessionEvent(_message.Message):
    __slots__ = ("type", "data", "sessionId")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    type: str
    data: str
    sessionId: str
    def __init__(self, type: _Optional[str] = ..., data: _Optional[str] = ..., sessionId: _Optional[str] = ...) -> None: ...

class HealthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HealthResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
