# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ProcessPushNotification(BaseObject):
    """
    Handles a push notification. Returns error with code 406 if the push notification is not supported and connection to the server is required to fetch new data. Can be called before authorization
    
    Params:
        payload (:class:`str`)
            JSON-encoded push notification payload with all fields sent by the server, and "google.sent_time" and "google.notification.sound" fields added
        
    """

    ID: str = Field("processPushNotification", alias="@type")
    payload: str

    @staticmethod
    def read(q: dict) -> ProcessPushNotification:
        return ProcessPushNotification.construct(**q)
