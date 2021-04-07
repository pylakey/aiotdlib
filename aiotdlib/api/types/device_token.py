# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeviceToken(BaseObject):
    """
    Represents a data needed to subscribe for push notifications through registerDevice method. To use specific push notification service, the correct application platform must be specified and a valid server authentication data must be uploaded at https://my.telegram.org
    
    """

    ID: str = Field("deviceToken", alias="@type")


class DeviceTokenApplePush(DeviceToken):
    """
    A token for Apple Push Notification service
    
    Params:
        device_token (:class:`str`)
            Device token; may be empty to de-register a device
        
        is_app_sandbox (:class:`bool`)
            True, if App Sandbox is enabled
        
    """

    ID: str = Field("deviceTokenApplePush", alias="@type")
    device_token: str
    is_app_sandbox: bool

    @staticmethod
    def read(q: dict) -> DeviceTokenApplePush:
        return DeviceTokenApplePush.construct(**q)


class DeviceTokenApplePushVoIP(DeviceToken):
    """
    A token for Apple Push Notification service VoIP notifications
    
    Params:
        device_token (:class:`str`)
            Device token; may be empty to de-register a device
        
        is_app_sandbox (:class:`bool`)
            True, if App Sandbox is enabled
        
        encrypt (:class:`bool`)
            True, if push notifications should be additionally encrypted
        
    """

    ID: str = Field("deviceTokenApplePushVoIP", alias="@type")
    device_token: str
    is_app_sandbox: bool
    encrypt: bool

    @staticmethod
    def read(q: dict) -> DeviceTokenApplePushVoIP:
        return DeviceTokenApplePushVoIP.construct(**q)


class DeviceTokenBlackBerryPush(DeviceToken):
    """
    A token for BlackBerry Push Service
    
    Params:
        token (:class:`str`)
            Token; may be empty to de-register a device
        
    """

    ID: str = Field("deviceTokenBlackBerryPush", alias="@type")
    token: str

    @staticmethod
    def read(q: dict) -> DeviceTokenBlackBerryPush:
        return DeviceTokenBlackBerryPush.construct(**q)


class DeviceTokenFirebaseCloudMessaging(DeviceToken):
    """
    A token for Firebase Cloud Messaging
    
    Params:
        token (:class:`str`)
            Device registration token; may be empty to de-register a device
        
        encrypt (:class:`bool`)
            True, if push notifications should be additionally encrypted
        
    """

    ID: str = Field("deviceTokenFirebaseCloudMessaging", alias="@type")
    token: str
    encrypt: bool

    @staticmethod
    def read(q: dict) -> DeviceTokenFirebaseCloudMessaging:
        return DeviceTokenFirebaseCloudMessaging.construct(**q)


class DeviceTokenMicrosoftPush(DeviceToken):
    """
    A token for Microsoft Push Notification Service
    
    Params:
        channel_uri (:class:`str`)
            Push notification channel URI; may be empty to de-register a device
        
    """

    ID: str = Field("deviceTokenMicrosoftPush", alias="@type")
    channel_uri: str

    @staticmethod
    def read(q: dict) -> DeviceTokenMicrosoftPush:
        return DeviceTokenMicrosoftPush.construct(**q)


class DeviceTokenMicrosoftPushVoIP(DeviceToken):
    """
    A token for Microsoft Push Notification Service VoIP channel
    
    Params:
        channel_uri (:class:`str`)
            Push notification channel URI; may be empty to de-register a device
        
    """

    ID: str = Field("deviceTokenMicrosoftPushVoIP", alias="@type")
    channel_uri: str

    @staticmethod
    def read(q: dict) -> DeviceTokenMicrosoftPushVoIP:
        return DeviceTokenMicrosoftPushVoIP.construct(**q)


class DeviceTokenSimplePush(DeviceToken):
    """
    A token for Simple Push API for Firefox OS
    
    Params:
        endpoint (:class:`str`)
            Absolute URL exposed by the push service where the application server can send push messages; may be empty to de-register a device
        
    """

    ID: str = Field("deviceTokenSimplePush", alias="@type")
    endpoint: str

    @staticmethod
    def read(q: dict) -> DeviceTokenSimplePush:
        return DeviceTokenSimplePush.construct(**q)


class DeviceTokenTizenPush(DeviceToken):
    """
    A token for Tizen Push Service
    
    Params:
        reg_id (:class:`str`)
            Push service registration identifier; may be empty to de-register a device
        
    """

    ID: str = Field("deviceTokenTizenPush", alias="@type")
    reg_id: str

    @staticmethod
    def read(q: dict) -> DeviceTokenTizenPush:
        return DeviceTokenTizenPush.construct(**q)


class DeviceTokenUbuntuPush(DeviceToken):
    """
    A token for Ubuntu Push Client service
    
    Params:
        token (:class:`str`)
            Token; may be empty to de-register a device
        
    """

    ID: str = Field("deviceTokenUbuntuPush", alias="@type")
    token: str

    @staticmethod
    def read(q: dict) -> DeviceTokenUbuntuPush:
        return DeviceTokenUbuntuPush.construct(**q)


class DeviceTokenWebPush(DeviceToken):
    """
    A token for web Push API
    
    Params:
        endpoint (:class:`str`)
            Absolute URL exposed by the push service where the application server can send push messages; may be empty to de-register a device
        
        p256dh_base64url (:class:`str`)
            Base64url-encoded P-256 elliptic curve Diffie-Hellman public key
        
        auth_base64url (:class:`str`)
            Base64url-encoded authentication secret
        
    """

    ID: str = Field("deviceTokenWebPush", alias="@type")
    endpoint: str
    p256dh_base64url: str
    auth_base64url: str

    @staticmethod
    def read(q: dict) -> DeviceTokenWebPush:
        return DeviceTokenWebPush.construct(**q)


class DeviceTokenWindowsPush(DeviceToken):
    """
    A token for Windows Push Notification Services
    
    Params:
        access_token (:class:`str`)
            The access token that will be used to send notifications; may be empty to de-register a device
        
    """

    ID: str = Field("deviceTokenWindowsPush", alias="@type")
    access_token: str

    @staticmethod
    def read(q: dict) -> DeviceTokenWindowsPush:
        return DeviceTokenWindowsPush.construct(**q)
