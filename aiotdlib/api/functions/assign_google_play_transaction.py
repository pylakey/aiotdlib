# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AssignGooglePlayTransaction(BaseObject):
    """
    Informs server about a Telegram Premium purchase through Google Play. For official applications only
    
    :param purchase_token: Google Play purchase token
    :type purchase_token: :class:`str`
    
    """

    ID: str = Field("assignGooglePlayTransaction", alias="@type")
    purchase_token: str

    @staticmethod
    def read(q: dict) -> AssignGooglePlayTransaction:
        return AssignGooglePlayTransaction.construct(**q)
