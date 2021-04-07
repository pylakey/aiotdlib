# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GroupCallPayloadFingerprint(BaseObject):
    """
    Describes a payload fingerprint for interaction with tgcalls
    
    Params:
        hash_ (:class:`str`)
            Value of the field hash
        
        setup (:class:`str`)
            Value of the field setup
        
        fingerprint (:class:`str`)
            Value of the field fingerprint
        
    """

    ID: str = Field("groupCallPayloadFingerprint", alias="@type")
    hash_: str = Field(..., alias='hash')
    setup: str
    fingerprint: str

    @staticmethod
    def read(q: dict) -> GroupCallPayloadFingerprint:
        return GroupCallPayloadFingerprint.construct(**q)
