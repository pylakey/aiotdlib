# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatPermissions(BaseObject):
    """
    Describes actions that a user is allowed to take in a chat
    
    Params:
        can_send_messages (:class:`bool`)
            True, if the user can send text messages, contacts, locations, and venues
        
        can_send_media_messages (:class:`bool`)
            True, if the user can send audio files, documents, photos, videos, video notes, and voice notes. Implies can_send_messages permissions
        
        can_send_polls (:class:`bool`)
            True, if the user can send polls. Implies can_send_messages permissions
        
        can_send_other_messages (:class:`bool`)
            True, if the user can send animations, games, stickers, and dice and use inline bots. Implies can_send_messages permissions
        
        can_add_web_page_previews (:class:`bool`)
            True, if the user may add a web page preview to their messages. Implies can_send_messages permissions
        
        can_change_info (:class:`bool`)
            True, if the user can change the chat title, photo, and other settings
        
        can_invite_users (:class:`bool`)
            True, if the user can invite new users to the chat
        
        can_pin_messages (:class:`bool`)
            True, if the user can pin messages
        
    """

    ID: str = Field("chatPermissions", alias="@type")
    can_send_messages: bool
    can_send_media_messages: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool

    @staticmethod
    def read(q: dict) -> ChatPermissions:
        return ChatPermissions.construct(**q)
