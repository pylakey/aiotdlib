# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchMessagesFilter(BaseObject):
    """
    Represents a filter for message search results
    
    """

    ID: str = Field("searchMessagesFilter", alias="@type")


class SearchMessagesFilterAnimation(SearchMessagesFilter):
    """
    Returns only animation messages
    
    """

    ID: str = Field("searchMessagesFilterAnimation", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterAnimation:
        return SearchMessagesFilterAnimation.construct(**q)


class SearchMessagesFilterAudio(SearchMessagesFilter):
    """
    Returns only audio messages
    
    """

    ID: str = Field("searchMessagesFilterAudio", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterAudio:
        return SearchMessagesFilterAudio.construct(**q)


class SearchMessagesFilterCall(SearchMessagesFilter):
    """
    Returns only call messages
    
    """

    ID: str = Field("searchMessagesFilterCall", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterCall:
        return SearchMessagesFilterCall.construct(**q)


class SearchMessagesFilterChatPhoto(SearchMessagesFilter):
    """
    Returns only messages containing chat photos
    
    """

    ID: str = Field("searchMessagesFilterChatPhoto", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterChatPhoto:
        return SearchMessagesFilterChatPhoto.construct(**q)


class SearchMessagesFilterDocument(SearchMessagesFilter):
    """
    Returns only document messages
    
    """

    ID: str = Field("searchMessagesFilterDocument", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterDocument:
        return SearchMessagesFilterDocument.construct(**q)


class SearchMessagesFilterEmpty(SearchMessagesFilter):
    """
    Returns all found messages, no filter is applied
    
    """

    ID: str = Field("searchMessagesFilterEmpty", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterEmpty:
        return SearchMessagesFilterEmpty.construct(**q)


class SearchMessagesFilterFailedToSend(SearchMessagesFilter):
    """
    Returns only failed to send messages. This filter can be used only if the message database is used
    
    """

    ID: str = Field("searchMessagesFilterFailedToSend", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterFailedToSend:
        return SearchMessagesFilterFailedToSend.construct(**q)


class SearchMessagesFilterMention(SearchMessagesFilter):
    """
    Returns only messages with mentions of the current user, or messages that are replies to their messages
    
    """

    ID: str = Field("searchMessagesFilterMention", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterMention:
        return SearchMessagesFilterMention.construct(**q)


class SearchMessagesFilterMissedCall(SearchMessagesFilter):
    """
    Returns only incoming call messages with missed/declined discard reasons
    
    """

    ID: str = Field("searchMessagesFilterMissedCall", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterMissedCall:
        return SearchMessagesFilterMissedCall.construct(**q)


class SearchMessagesFilterPhoto(SearchMessagesFilter):
    """
    Returns only photo messages
    
    """

    ID: str = Field("searchMessagesFilterPhoto", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterPhoto:
        return SearchMessagesFilterPhoto.construct(**q)


class SearchMessagesFilterPhotoAndVideo(SearchMessagesFilter):
    """
    Returns only photo and video messages
    
    """

    ID: str = Field("searchMessagesFilterPhotoAndVideo", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterPhotoAndVideo:
        return SearchMessagesFilterPhotoAndVideo.construct(**q)


class SearchMessagesFilterPinned(SearchMessagesFilter):
    """
    Returns only pinned messages
    
    """

    ID: str = Field("searchMessagesFilterPinned", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterPinned:
        return SearchMessagesFilterPinned.construct(**q)


class SearchMessagesFilterUnreadMention(SearchMessagesFilter):
    """
    Returns only messages with unread mentions of the current user, or messages that are replies to their messages. When using this filter the results can't be additionally filtered by a query, a message thread or by the sending user
    
    """

    ID: str = Field("searchMessagesFilterUnreadMention", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterUnreadMention:
        return SearchMessagesFilterUnreadMention.construct(**q)


class SearchMessagesFilterUrl(SearchMessagesFilter):
    """
    Returns only messages containing URLs
    
    """

    ID: str = Field("searchMessagesFilterUrl", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterUrl:
        return SearchMessagesFilterUrl.construct(**q)


class SearchMessagesFilterVideo(SearchMessagesFilter):
    """
    Returns only video messages
    
    """

    ID: str = Field("searchMessagesFilterVideo", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterVideo:
        return SearchMessagesFilterVideo.construct(**q)


class SearchMessagesFilterVideoNote(SearchMessagesFilter):
    """
    Returns only video note messages
    
    """

    ID: str = Field("searchMessagesFilterVideoNote", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterVideoNote:
        return SearchMessagesFilterVideoNote.construct(**q)


class SearchMessagesFilterVoiceAndVideoNote(SearchMessagesFilter):
    """
    Returns only voice and video note messages
    
    """

    ID: str = Field("searchMessagesFilterVoiceAndVideoNote", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterVoiceAndVideoNote:
        return SearchMessagesFilterVoiceAndVideoNote.construct(**q)


class SearchMessagesFilterVoiceNote(SearchMessagesFilter):
    """
    Returns only voice note messages
    
    """

    ID: str = Field("searchMessagesFilterVoiceNote", alias="@type")

    @staticmethod
    def read(q: dict) -> SearchMessagesFilterVoiceNote:
        return SearchMessagesFilterVoiceNote.construct(**q)
