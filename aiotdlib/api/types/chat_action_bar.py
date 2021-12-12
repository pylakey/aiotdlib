# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatActionBar(BaseObject):
    """
    Describes actions which must be possible to do through a chat action bar
    
    """

    ID: str = Field("chatActionBar", alias="@type")


class ChatActionBarAddContact(ChatActionBar):
    """
    The chat is a private or secret chat and the other user can be added to the contact list using the method addContact
    
    """

    ID: str = Field("chatActionBarAddContact", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatActionBarAddContact:
        return ChatActionBarAddContact.construct(**q)


class ChatActionBarInviteMembers(ChatActionBar):
    """
    The chat is a recently created group chat to which new members can be invited
    
    """

    ID: str = Field("chatActionBarInviteMembers", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatActionBarInviteMembers:
        return ChatActionBarInviteMembers.construct(**q)


class ChatActionBarJoinRequest(ChatActionBar):
    """
    The chat is a private chat with an administrator of a chat to which the user sent join request
    
    :param title: Title of the chat to which the join request was sent
    :type title: :class:`str`
    
    :param is_channel: True, if the join request was sent to a channel chat
    :type is_channel: :class:`bool`
    
    :param request_date: Point in time (Unix timestamp) when the join request was sent
    :type request_date: :class:`int`
    
    """

    ID: str = Field("chatActionBarJoinRequest", alias="@type")
    title: str
    is_channel: bool
    request_date: int

    @staticmethod
    def read(q: dict) -> ChatActionBarJoinRequest:
        return ChatActionBarJoinRequest.construct(**q)


class ChatActionBarReportAddBlock(ChatActionBar):
    """
    The chat is a private or secret chat, which can be reported using the method reportChat, or the other user can be blocked using the method toggleMessageSenderIsBlocked, or the other user can be added to the contact list using the method addContact
    
    :param can_unarchive: If true, the chat was automatically archived and can be moved back to the main chat list using addChatToList simultaneously with setting chat notification settings to default using setChatNotificationSettings
    :type can_unarchive: :class:`bool`
    
    :param distance: If non-negative, the current user was found by the peer through searchChatsNearby and this is the distance between the users
    :type distance: :class:`int`
    
    """

    ID: str = Field("chatActionBarReportAddBlock", alias="@type")
    can_unarchive: bool
    distance: int

    @staticmethod
    def read(q: dict) -> ChatActionBarReportAddBlock:
        return ChatActionBarReportAddBlock.construct(**q)


class ChatActionBarReportSpam(ChatActionBar):
    """
    The chat can be reported as spam using the method reportChat with the reason chatReportReasonSpam
    
    :param can_unarchive: If true, the chat was automatically archived and can be moved back to the main chat list using addChatToList simultaneously with setting chat notification settings to default using setChatNotificationSettings
    :type can_unarchive: :class:`bool`
    
    """

    ID: str = Field("chatActionBarReportSpam", alias="@type")
    can_unarchive: bool

    @staticmethod
    def read(q: dict) -> ChatActionBarReportSpam:
        return ChatActionBarReportSpam.construct(**q)


class ChatActionBarReportUnrelatedLocation(ChatActionBar):
    """
    The chat is a location-based supergroup, which can be reported as having unrelated location using the method reportChat with the reason chatReportReasonUnrelatedLocation
    
    """

    ID: str = Field("chatActionBarReportUnrelatedLocation", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatActionBarReportUnrelatedLocation:
        return ChatActionBarReportUnrelatedLocation.construct(**q)


class ChatActionBarSharePhoneNumber(ChatActionBar):
    """
    The chat is a private or secret chat with a mutual contact and the user's phone number can be shared with the other user using the method sharePhoneNumber
    
    """

    ID: str = Field("chatActionBarSharePhoneNumber", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatActionBarSharePhoneNumber:
        return ChatActionBarSharePhoneNumber.construct(**q)
