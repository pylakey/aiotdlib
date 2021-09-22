# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetMessageLinkInfo(BaseObject):
    """
    Returns information about a public or private message link. Can be called for any internal link of the type internalLinkTypeMessage
    
    :param url: The message link
    :type url: :class:`str`
    
    """

    ID: str = Field("getMessageLinkInfo", alias="@type")
    url: str

    @staticmethod
    def read(q: dict) -> GetMessageLinkInfo:
        return GetMessageLinkInfo.construct(**q)
