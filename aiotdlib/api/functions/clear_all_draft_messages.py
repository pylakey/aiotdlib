# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClearAllDraftMessages(BaseObject):
    """
    Clears message drafts in all chats

    :param exclude_secret_chats: Pass true to keep local message drafts in secret chats
    :type exclude_secret_chats: :class:`Bool`
    """

    ID: typing.Literal["clearAllDraftMessages"] = "clearAllDraftMessages"
    exclude_secret_chats: Bool = False
