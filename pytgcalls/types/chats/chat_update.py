from enum import auto
from enum import Flag
from typing import Any

from ..update import Update


class ChatUpdate(Update):
    class Status(Flag):
        KICKED = auto()
        LEFT_GROUP = auto()
        CLOSED_VOICE_CHAT = auto()
        INVITED_VOICE_CHAT = auto()
        DISCARDED_CALL = auto()
        INCOMING_CALL = auto()
        LEFT_CALL = KICKED | LEFT_GROUP | CLOSED_VOICE_CHAT | DISCARDED_CALL

        def __repr__(self):
            cls_name = self.__class__.__name__
            return f'{cls_name}.{self.name}'

    def __init__(
        self,
        chat_id: int,
        status: Status,
        action: Any = None,
    ):
        super().__init__(chat_id)
        self.status = status
        self.action = action
