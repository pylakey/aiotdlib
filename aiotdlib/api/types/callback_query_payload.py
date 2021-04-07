# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CallbackQueryPayload(BaseObject):
    """
    Represents a payload of a callback query
    
    """

    ID: str = Field("callbackQueryPayload", alias="@type")


class CallbackQueryPayloadData(CallbackQueryPayload):
    """
    The payload for a general callback button
    
    Params:
        data (:class:`str`)
            Data that was attached to the callback button
        
    """

    ID: str = Field("callbackQueryPayloadData", alias="@type")
    data: str

    @staticmethod
    def read(q: dict) -> CallbackQueryPayloadData:
        return CallbackQueryPayloadData.construct(**q)


class CallbackQueryPayloadDataWithPassword(CallbackQueryPayload):
    """
    The payload for a callback button requiring password
    
    Params:
        password (:class:`str`)
            The password for the current user
        
        data (:class:`str`)
            Data that was attached to the callback button
        
    """

    ID: str = Field("callbackQueryPayloadDataWithPassword", alias="@type")
    password: str
    data: str

    @staticmethod
    def read(q: dict) -> CallbackQueryPayloadDataWithPassword:
        return CallbackQueryPayloadDataWithPassword.construct(**q)


class CallbackQueryPayloadGame(CallbackQueryPayload):
    """
    The payload for a game callback button
    
    Params:
        game_short_name (:class:`str`)
            A short name of the game that was attached to the callback button
        
    """

    ID: str = Field("callbackQueryPayloadGame", alias="@type")
    game_short_name: str

    @staticmethod
    def read(q: dict) -> CallbackQueryPayloadGame:
        return CallbackQueryPayloadGame.construct(**q)
