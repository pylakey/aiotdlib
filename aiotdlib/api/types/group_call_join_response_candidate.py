# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GroupCallJoinResponseCandidate(BaseObject):
    """
    Describes a join response candidate for interaction with tgcalls
    
    Params:
        port (:class:`str`)
            Value of the field port
        
        protocol (:class:`str`)
            Value of the field protocol
        
        network (:class:`str`)
            Value of the field network
        
        generation (:class:`str`)
            Value of the field generation
        
        id (:class:`str`)
            Value of the field id
        
        component (:class:`str`)
            Value of the field component
        
        foundation (:class:`str`)
            Value of the field foundation
        
        priority (:class:`str`)
            Value of the field priority
        
        ip (:class:`str`)
            Value of the field ip
        
        type_ (:class:`str`)
            Value of the field type
        
        tcp_type (:class:`str`)
            Value of the field tcp_type
        
        rel_addr (:class:`str`)
            Value of the field rel_addr
        
        rel_port (:class:`str`)
            Value of the field rel_port
        
    """

    ID: str = Field("groupCallJoinResponseCandidate", alias="@type")
    port: str
    protocol: str
    network: str
    generation: str
    id: str
    component: str
    foundation: str
    priority: str
    ip: str
    type_: str = Field(..., alias='type')
    tcp_type: str
    rel_addr: str
    rel_port: str

    @staticmethod
    def read(q: dict) -> GroupCallJoinResponseCandidate:
        return GroupCallJoinResponseCandidate.construct(**q)
