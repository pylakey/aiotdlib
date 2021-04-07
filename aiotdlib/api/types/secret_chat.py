# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .secret_chat_state import SecretChatState
from ..base_object import BaseObject


class SecretChat(BaseObject):
    """
    Represents a secret chat
    
    Params:
        id (:class:`int`)
            Secret chat identifier
        
        user_id (:class:`int`)
            Identifier of the chat partner
        
        state (:class:`SecretChatState`)
            State of the secret chat
        
        is_outbound (:class:`bool`)
            True, if the chat was created by the current user; otherwise false
        
        key_hash (:class:`str`)
            Hash of the currently used key for comparison with the hash of the chat partner's key. This is a string of 36 little-endian bytes, which must be split into groups of 2 bits, each denoting a pixel of one of 4 colors FFFFFF, D5E6F3, 2D5775, and 2F99C9. The pixels must be used to make a 12x12 square image filled from left to right, top to bottom. Alternatively, the first 32 bytes of the hash can be converted to the hexadecimal format and printed as 32 2-digit hex numbers
        
        layer (:class:`int`)
            Secret chat layer; determines features supported by the chat partner's application. Video notes are supported if the layer >= 66; nested text entities and underline and strikethrough entities are supported if the layer >= 101
        
    """

    ID: str = Field("secretChat", alias="@type")
    id: int
    user_id: int
    state: SecretChatState
    is_outbound: bool
    key_hash: str
    layer: int

    @staticmethod
    def read(q: dict) -> SecretChat:
        return SecretChat.construct(**q)
