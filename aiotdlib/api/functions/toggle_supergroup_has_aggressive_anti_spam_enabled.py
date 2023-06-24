# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleSupergroupHasAggressiveAntiSpamEnabled(BaseObject):
    """
    Toggles whether aggressive anti-spam checks are enabled in the supergroup. Can be called only if supergroupFullInfo.can_toggle_aggressive_anti_spam == true

    :param supergroup_id: The identifier of the supergroup, which isn't a broadcast group
    :type supergroup_id: :class:`Int53`
    :param has_aggressive_anti_spam_enabled: The new value of has_aggressive_anti_spam_enabled
    :type has_aggressive_anti_spam_enabled: :class:`Bool`
    """

    ID: typing.Literal["toggleSupergroupHasAggressiveAntiSpamEnabled"] = "toggleSupergroupHasAggressiveAntiSpamEnabled"
    supergroup_id: Int53
    has_aggressive_anti_spam_enabled: Bool
