# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .group_call_payload_fingerprint import GroupCallPayloadFingerprint
from ..base_object import BaseObject


class GroupCallPayload(BaseObject):
    """
    Describes a payload for interaction with tgcalls
    
    Params:
        ufrag (:class:`str`)
            Value of the field ufrag
        
        pwd (:class:`str`)
            Value of the field pwd
        
        fingerprints (:obj:`list[GroupCallPayloadFingerprint]`)
            The list of fingerprints
        
    """

    ID: str = Field("groupCallPayload", alias="@type")
    ufrag: str
    pwd: str
    fingerprints: list[GroupCallPayloadFingerprint]

    @staticmethod
    def read(q: dict) -> GroupCallPayload:
        return GroupCallPayload.construct(**q)
