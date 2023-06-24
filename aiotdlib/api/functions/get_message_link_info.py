# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMessageLinkInfo(BaseObject):
    """
    Returns information about a public or private message link. Can be called for any internal link of the type internalLinkTypeMessage

    :param url: The message link
    :type url: :class:`String`
    """

    ID: typing.Literal["getMessageLinkInfo"] = "getMessageLinkInfo"
    url: String
