# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    InputFile,
)


class AddSavedNotificationSound(BaseObject):
    """
    Adds a new notification sound to the list of saved notification sounds. The new notification sound is added to the top of the list. If it is already in the list, its position isn't changed

    :param sound: Notification sound file to add
    :type sound: :class:`InputFile`
    """

    ID: typing.Literal["addSavedNotificationSound"] = "addSavedNotificationSound"
    sound: InputFile
