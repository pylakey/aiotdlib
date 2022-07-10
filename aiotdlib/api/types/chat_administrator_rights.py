# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatAdministratorRights(BaseObject):
    """
    Describes rights of the administrator
    
    :param can_manage_chat: True, if the administrator can get chat event log, get chat statistics, get message statistics in channels, get channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other privilege; applicable to supergroups and channels only
    :type can_manage_chat: :class:`bool`
    
    :param can_change_info: True, if the administrator can change the chat title, photo, and other settings
    :type can_change_info: :class:`bool`
    
    :param can_post_messages: True, if the administrator can create channel posts; applicable to channels only
    :type can_post_messages: :class:`bool`
    
    :param can_edit_messages: True, if the administrator can edit messages of other users and pin messages; applicable to channels only
    :type can_edit_messages: :class:`bool`
    
    :param can_delete_messages: True, if the administrator can delete messages of other users
    :type can_delete_messages: :class:`bool`
    
    :param can_invite_users: True, if the administrator can invite new users to the chat
    :type can_invite_users: :class:`bool`
    
    :param can_restrict_members: True, if the administrator can restrict, ban, or unban chat members; always true for channels
    :type can_restrict_members: :class:`bool`
    
    :param can_pin_messages: True, if the administrator can pin messages; applicable to basic groups and supergroups only
    :type can_pin_messages: :class:`bool`
    
    :param can_promote_members: True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that were directly or indirectly promoted by them
    :type can_promote_members: :class:`bool`
    
    :param can_manage_video_chats: True, if the administrator can manage video chats
    :type can_manage_video_chats: :class:`bool`
    
    :param is_anonymous: True, if the administrator isn't shown in the chat member list and sends messages anonymously; applicable to supergroups only
    :type is_anonymous: :class:`bool`
    
    """

    ID: str = Field("chatAdministratorRights", alias="@type")
    can_manage_chat: bool
    can_change_info: bool
    can_post_messages: bool
    can_edit_messages: bool
    can_delete_messages: bool
    can_invite_users: bool
    can_restrict_members: bool
    can_pin_messages: bool
    can_promote_members: bool
    can_manage_video_chats: bool
    is_anonymous: bool

    @staticmethod
    def read(q: dict) -> ChatAdministratorRights:
        return ChatAdministratorRights.construct(**q)
