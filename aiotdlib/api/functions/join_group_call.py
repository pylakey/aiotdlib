# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    MessageSender,
)


class JoinGroupCall(BaseObject):
    """
    Joins an active group call. Returns join response payload for tgcalls

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param audio_source_id: Caller audio channel synchronization source identifier; received from tgcalls
    :type audio_source_id: :class:`Int32`
    :param payload: Group call join payload; received from tgcalls
    :type payload: :class:`String`
    :param is_muted: Pass true to join the call with muted microphone
    :type is_muted: :class:`Bool`
    :param is_my_video_enabled: Pass true if the user's video is enabled
    :type is_my_video_enabled: :class:`Bool`
    :param invite_hash: If non-empty, invite hash to be used to join the group call without being muted by administrators
    :type invite_hash: :class:`String`
    :param key_fingerprint: Fingerprint of the encryption key for E2E group calls not bound to a chat; pass 0 for voice chats
    :type key_fingerprint: :class:`Int64`
    :param participant_id: Identifier of a group call participant, which will be used to join the call; pass null to join as self; video chats only, defaults to None
    :type participant_id: :class:`MessageSender`, optional
    """

    ID: typing.Literal["joinGroupCall"] = Field("joinGroupCall", validation_alias="@type", alias="@type")
    group_call_id: Int32
    audio_source_id: Int32
    payload: String
    is_muted: Bool = False
    is_my_video_enabled: Bool = False
    invite_hash: String = ""
    key_fingerprint: Int64 = 0
    participant_id: typing.Optional[MessageSender] = None
