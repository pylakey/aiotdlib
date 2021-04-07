# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CallProtocol(BaseObject):
    """
    Specifies the supported call protocols
    
    Params:
        udp_p2p (:class:`bool`)
            True, if UDP peer-to-peer connections are supported
        
        udp_reflector (:class:`bool`)
            True, if connection through UDP reflectors is supported
        
        min_layer (:class:`int`)
            The minimum supported API layer; use 65
        
        max_layer (:class:`int`)
            The maximum supported API layer; use 65
        
        library_versions (:obj:`list[str]`)
            List of supported tgcalls versions
        
    """

    ID: str = Field("callProtocol", alias="@type")
    udp_p2p: bool
    udp_reflector: bool
    min_layer: int
    max_layer: int
    library_versions: list[str]

    @staticmethod
    def read(q: dict) -> CallProtocol:
        return CallProtocol.construct(**q)
