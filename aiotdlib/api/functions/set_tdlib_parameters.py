# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import TdlibParameters


class SetTdlibParameters(BaseObject):
    """
    Sets the parameters for TDLib initialization. Works only when the current authorization state is authorizationStateWaitTdlibParameters
    
    Params:
        parameters (:class:`TdlibParameters`)
            Parameters
        
    """

    ID: str = Field("setTdlibParameters", alias="@type")
    parameters: TdlibParameters

    @staticmethod
    def read(q: dict) -> SetTdlibParameters:
        return SetTdlibParameters.construct(**q)
