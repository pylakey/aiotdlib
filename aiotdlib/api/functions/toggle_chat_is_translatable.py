# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleChatIsTranslatable(BaseObject):
    """
    Changes the translatable state of a chat; for Telegram Premium users only

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param is_translatable: New value of is_translatable
    :type is_translatable: :class:`Bool`
    """

    ID: typing.Literal["toggleChatIsTranslatable"] = "toggleChatIsTranslatable"
    chat_id: Int53
    is_translatable: Bool
