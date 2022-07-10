# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AttachmentMenuBotColor(BaseObject):
    """
    Describes a color to highlight a bot added to attachment menu
    
    :param light_color: Color in the RGB24 format for light themes
    :type light_color: :class:`int`
    
    :param dark_color: Color in the RGB24 format for dark themes
    :type dark_color: :class:`int`
    
    """

    ID: str = Field("attachmentMenuBotColor", alias="@type")
    light_color: int
    dark_color: int

    @staticmethod
    def read(q: dict) -> AttachmentMenuBotColor:
        return AttachmentMenuBotColor.construct(**q)
