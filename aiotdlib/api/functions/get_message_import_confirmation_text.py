# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMessageImportConfirmationText(BaseObject):
    """
    Returns a confirmation text to be shown to the user before starting message import

    :param chat_id: Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getMessageImportConfirmationText"] = "getMessageImportConfirmationText"
    chat_id: Int53
