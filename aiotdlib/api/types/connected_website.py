# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ConnectedWebsite(BaseObject):
    """
    Contains information about one website the current user is logged in with Telegram
    
    Params:
        id (:class:`int`)
            Website identifier
        
        domain_name (:class:`str`)
            The domain name of the website
        
        bot_user_id (:class:`int`)
            User identifier of a bot linked with the website
        
        browser (:class:`str`)
            The version of a browser used to log in
        
        platform (:class:`str`)
            Operating system the browser is running on
        
        log_in_date (:class:`int`)
            Point in time (Unix timestamp) when the user was logged in
        
        last_active_date (:class:`int`)
            Point in time (Unix timestamp) when obtained authorization was last used
        
        ip (:class:`str`)
            IP address from which the user was logged in, in human-readable format
        
        location (:class:`str`)
            Human-readable description of a country and a region, from which the user was logged in, based on the IP address
        
    """

    ID: str = Field("connectedWebsite", alias="@type")
    id: int
    domain_name: str
    bot_user_id: int
    browser: str
    platform: str
    log_in_date: int
    last_active_date: int
    ip: str
    location: str

    @staticmethod
    def read(q: dict) -> ConnectedWebsite:
        return ConnectedWebsite.construct(**q)
