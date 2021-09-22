# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import TdlibParameters
from ..base_object import BaseObject


class SetTdlibParameters(BaseObject):
    """
    Sets the parameters for TDLib initialization. Works only when the current authorization state is authorizationStateWaitTdlibParameters
    
    :param parameters: Parameters
    :type parameters: :class:`TdlibParameters`
    
    """

    ID: str = Field("setTdlibParameters", alias="@type")
    parameters: TdlibParameters

    @staticmethod
    def read(q: dict) -> SetTdlibParameters:
        return SetTdlibParameters.construct(**q)
