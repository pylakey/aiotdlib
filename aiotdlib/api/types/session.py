# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Session(BaseObject):
    """
    Contains information about one session in a Telegram application used by the current user. Sessions should be shown to the user in the returned order
    
    Params:
        id (:class:`int`)
            Session identifier
        
        is_current (:class:`bool`)
            True, if this session is the current session
        
        is_password_pending (:class:`bool`)
            True, if a password is needed to complete authorization of the session
        
        api_id (:class:`int`)
            Telegram API identifier, as provided by the application
        
        application_name (:class:`str`)
            Name of the application, as provided by the application
        
        application_version (:class:`str`)
            The version of the application, as provided by the application
        
        is_official_application (:class:`bool`)
            True, if the application is an official application or uses the api_id of an official application
        
        device_model (:class:`str`)
            Model of the device the application has been run or is running on, as provided by the application
        
        platform (:class:`str`)
            Operating system the application has been run or is running on, as provided by the application
        
        system_version (:class:`str`)
            Version of the operating system the application has been run or is running on, as provided by the application
        
        log_in_date (:class:`int`)
            Point in time (Unix timestamp) when the user has logged in
        
        last_active_date (:class:`int`)
            Point in time (Unix timestamp) when the session was last used
        
        ip (:class:`str`)
            IP address from which the session was created, in human-readable format
        
        country (:class:`str`)
            A two-letter country code for the country from which the session was created, based on the IP address
        
        region (:class:`str`)
            Region code from which the session was created, based on the IP address
        
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
