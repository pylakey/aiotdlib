# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class LoadSavedMessagesTopics(BaseObject):
    """
    Loads more Saved Messages topics. The loaded topics will be sent through updateSavedMessagesTopic. Topics are sorted by their topic.order in descending order. Returns a 404 error if all topics have been loaded

    :param limit: The maximum number of topics to be loaded. For optimal performance, the number of loaded topics is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["loadSavedMessagesTopics"] = Field(
        "loadSavedMessagesTopics", validation_alias="@type", alias="@type"
    )
    limit: Int32
