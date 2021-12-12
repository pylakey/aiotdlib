# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetInactiveSessionTtl(BaseObject):
    """
    Changes the period of inactivity after which sessions will automatically be terminated
    
    :param inactive_session_ttl_days: New number of days of inactivity before sessions will be automatically terminated; 1-366 days
    :type inactive_session_ttl_days: :class:`int`
    
    """

    ID: str = Field("setInactiveSessionTtl", alias="@type")
    inactive_session_ttl_days: int

    @staticmethod
    def read(q: dict) -> SetInactiveSessionTtl:
        return SetInactiveSessionTtl.construct(**q)
