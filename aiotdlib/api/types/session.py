# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Session(BaseObject):
    """
    Contains information about one session in a Telegram application used by the current user. Sessions should be shown to the user in the returned order
    
    :param id: Session identifier
    :type id: :class:`int`
    
    :param is_current: True, if this session is the current session
    :type is_current: :class:`bool`
    
    :param is_password_pending: True, if a password is needed to complete authorization of the session
    :type is_password_pending: :class:`bool`
    
    :param api_id: Telegram API identifier, as provided by the application
    :type api_id: :class:`int`
    
    :param application_name: Name of the application, as provided by the application
    :type application_name: :class:`str`
    
    :param application_version: The version of the application, as provided by the application
    :type application_version: :class:`str`
    
    :param is_official_application: True, if the application is an official application or uses the api_id of an official application
    :type is_official_application: :class:`bool`
    
    :param device_model: Model of the device the application has been run or is running on, as provided by the application
    :type device_model: :class:`str`
    
    :param platform: Operating system the application has been run or is running on, as provided by the application
    :type platform: :class:`str`
    
    :param system_version: Version of the operating system the application has been run or is running on, as provided by the application
    :type system_version: :class:`str`
    
    :param log_in_date: Point in time (Unix timestamp) when the user has logged in
    :type log_in_date: :class:`int`
    
    :param last_active_date: Point in time (Unix timestamp) when the session was last used
    :type last_active_date: :class:`int`
    
    :param ip: IP address from which the session was created, in human-readable format
    :type ip: :class:`str`
    
    :param country: A two-letter country code for the country from which the session was created, based on the IP address
    :type country: :class:`str`
    
    :param region: Region code from which the session was created, based on the IP address
    :type region: :class:`str`
    
    """

    ID: str = Field("session", alias="@type")
    id: int
    is_current: bool
    is_password_pending: bool
    api_id: int
    application_name: str
    application_version: str
    is_official_application: bool
    device_model: str
    platform: str
    system_version: str
    log_in_date: int
    last_active_date: int
    ip: str
    country: str
    region: str

    @staticmethod
    def read(q: dict) -> Session:
        return Session.construct(**q)
