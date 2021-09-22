# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ConnectedWebsite(BaseObject):
    """
    Contains information about one website the current user is logged in with Telegram
    
    :param id: Website identifier
    :type id: :class:`int`
    
    :param domain_name: The domain name of the website
    :type domain_name: :class:`str`
    
    :param bot_user_id: User identifier of a bot linked with the website
    :type bot_user_id: :class:`int`
    
    :param browser: The version of a browser used to log in
    :type browser: :class:`str`
    
    :param platform: Operating system the browser is running on
    :type platform: :class:`str`
    
    :param log_in_date: Point in time (Unix timestamp) when the user was logged in
    :type log_in_date: :class:`int`
    
    :param last_active_date: Point in time (Unix timestamp) when obtained authorization was last used
    :type last_active_date: :class:`int`
    
    :param ip: IP address from which the user was logged in, in human-readable format
    :type ip: :class:`str`
    
    :param location: Human-readable description of a country and a region, from which the user was logged in, based on the IP address
    :type location: :class:`str`
    
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
