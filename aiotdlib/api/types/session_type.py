# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SessionType(BaseObject):
    """
    Represents the type of a session
    
    """

    ID: str = Field("sessionType", alias="@type")


class SessionTypeAndroid(SessionType):
    """
    The session is running on an Android device
    
    """

    ID: str = Field("sessionTypeAndroid", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeAndroid:
        return SessionTypeAndroid.construct(**q)


class SessionTypeApple(SessionType):
    """
    The session is running on a generic Apple device
    
    """

    ID: str = Field("sessionTypeApple", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeApple:
        return SessionTypeApple.construct(**q)


class SessionTypeBrave(SessionType):
    """
    The session is running on the Brave browser
    
    """

    ID: str = Field("sessionTypeBrave", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeBrave:
        return SessionTypeBrave.construct(**q)


class SessionTypeChrome(SessionType):
    """
    The session is running on the Chrome browser
    
    """

    ID: str = Field("sessionTypeChrome", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeChrome:
        return SessionTypeChrome.construct(**q)


class SessionTypeEdge(SessionType):
    """
    The session is running on the Edge browser
    
    """

    ID: str = Field("sessionTypeEdge", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeEdge:
        return SessionTypeEdge.construct(**q)


class SessionTypeFirefox(SessionType):
    """
    The session is running on the Firefox browser
    
    """

    ID: str = Field("sessionTypeFirefox", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeFirefox:
        return SessionTypeFirefox.construct(**q)


class SessionTypeIpad(SessionType):
    """
    The session is running on an iPad device
    
    """

    ID: str = Field("sessionTypeIpad", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeIpad:
        return SessionTypeIpad.construct(**q)


class SessionTypeIphone(SessionType):
    """
    The session is running on an iPhone device
    
    """

    ID: str = Field("sessionTypeIphone", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeIphone:
        return SessionTypeIphone.construct(**q)


class SessionTypeLinux(SessionType):
    """
    The session is running on a Linux device
    
    """

    ID: str = Field("sessionTypeLinux", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeLinux:
        return SessionTypeLinux.construct(**q)


class SessionTypeMac(SessionType):
    """
    The session is running on a Mac device
    
    """

    ID: str = Field("sessionTypeMac", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeMac:
        return SessionTypeMac.construct(**q)


class SessionTypeOpera(SessionType):
    """
    The session is running on the Opera browser
    
    """

    ID: str = Field("sessionTypeOpera", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeOpera:
        return SessionTypeOpera.construct(**q)


class SessionTypeSafari(SessionType):
    """
    The session is running on the Safari browser
    
    """

    ID: str = Field("sessionTypeSafari", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeSafari:
        return SessionTypeSafari.construct(**q)


class SessionTypeUbuntu(SessionType):
    """
    The session is running on an Ubuntu device
    
    """

    ID: str = Field("sessionTypeUbuntu", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeUbuntu:
        return SessionTypeUbuntu.construct(**q)


class SessionTypeUnknown(SessionType):
    """
    The session is running on an unknown type of device
    
    """

    ID: str = Field("sessionTypeUnknown", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeUnknown:
        return SessionTypeUnknown.construct(**q)


class SessionTypeVivaldi(SessionType):
    """
    The session is running on the Vivaldi browser
    
    """

    ID: str = Field("sessionTypeVivaldi", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeVivaldi:
        return SessionTypeVivaldi.construct(**q)


class SessionTypeWindows(SessionType):
    """
    The session is running on a Windows device
    
    """

    ID: str = Field("sessionTypeWindows", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeWindows:
        return SessionTypeWindows.construct(**q)


class SessionTypeXbox(SessionType):
    """
    The session is running on an Xbox console
    
    """

    ID: str = Field("sessionTypeXbox", alias="@type")

    @staticmethod
    def read(q: dict) -> SessionTypeXbox:
        return SessionTypeXbox.construct(**q)
