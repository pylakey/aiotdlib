# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import NetworkType


class SetNetworkType(BaseObject):
    """
    Sets the current network type. Can be called before authorization. Calling this method forces all network connections to reopen, mitigating the delay in switching between different networks, so it should be called whenever the network is changed, even if the network type remains the same. Network type is used to check whether the library can use the network at all and also for collecting detailed network data usage statistics
    
    Params:
        type_ (:class:`NetworkType`)
            The new network type. By default, networkTypeOther
        
    """

    ID: str = Field("setNetworkType", alias="@type")
    type_: NetworkType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> SetNetworkType:
        return SetNetworkType.construct(**q)
