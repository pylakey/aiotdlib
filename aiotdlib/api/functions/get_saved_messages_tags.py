# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSavedMessagesTags(BaseObject):
    """
    Returns tags used in Saved Messages or a Saved Messages topic

    :param saved_messages_topic_id: Identifier of Saved Messages topic which tags will be returned; pass 0 to get all Saved Messages tags
    :type saved_messages_topic_id: :class:`Int53`
    """

    ID: typing.Literal["getSavedMessagesTags"] = Field("getSavedMessagesTags", validation_alias="@type", alias="@type")
    saved_messages_topic_id: Int53
