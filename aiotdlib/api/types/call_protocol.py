# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CallProtocol(BaseObject):
    """
    Specifies the supported call protocols
    
    :param udp_p2p: True, if UDP peer-to-peer connections are supported
    :type udp_p2p: :class:`bool`
    
    :param udp_reflector: True, if connection through UDP reflectors is supported
    :type udp_reflector: :class:`bool`
    
    :param min_layer: The minimum supported API layer; use 65
    :type min_layer: :class:`int`
    
    :param max_layer: The maximum supported API layer; use 65
    :type max_layer: :class:`int`
    
    :param library_versions: List of supported tgcalls versions
    :type library_versions: :class:`list[str]`
    
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
