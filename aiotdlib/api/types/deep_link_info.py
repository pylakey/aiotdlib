# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .formatted_text import FormattedText
from ..base_object import BaseObject


class DeepLinkInfo(BaseObject):
    """
    Contains information about a tg:// deep link
    
    Params:
        text (:class:`FormattedText`)
            Text to be shown to the user
        
        need_update_application (:class:`bool`)
            True, if user should be asked to update the application
        
    """

    ID: str = Field("deepLinkInfo", alias="@type")
    text: FormattedText
    need_update_application: bool

    @staticmethod
    def read(q: dict) -> DeepLinkInfo:
        return DeepLinkInfo.construct(**q)
