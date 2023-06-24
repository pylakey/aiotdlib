# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class UpgradeBasicGroupChatToSupergroupChat(BaseObject):
    """
    Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires creator privileges. Deactivates the original basic group

    :param chat_id: Identifier of the chat to upgrade
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["upgradeBasicGroupChatToSupergroupChat"] = "upgradeBasicGroupChatToSupergroupChat"
    chat_id: Int53
