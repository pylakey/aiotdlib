# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleChatFolderTags(BaseObject):
    """
    Toggles whether chat folder tags are enabled

    :param are_tags_enabled: Pass true to enable folder tags; pass false to disable them
    :type are_tags_enabled: :class:`Bool`
    """

    ID: typing.Literal["toggleChatFolderTags"] = Field("toggleChatFolderTags", validation_alias="@type", alias="@type")
    are_tags_enabled: Bool = False
