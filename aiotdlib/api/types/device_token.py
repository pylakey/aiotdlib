# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

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
    
    :param device_token: Device token; may be empty to de-register a device
    :type device_token: :class:`str`
    
    :param is_app_sandbox: True, if App Sandbox is enabled
    :type is_app_sandbox: :class:`bool`
    
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
    
    :param device_token: Device token; may be empty to de-register a device
    :type device_token: :class:`str`
    
    :param is_app_sandbox: True, if App Sandbox is enabled
    :type is_app_sandbox: :class:`bool`
    
    :param encrypt: True, if push notifications should be additionally encrypted
    :type encrypt: :class:`bool`
    
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
    
    :param token: Token; may be empty to de-register a device
    :type token: :class:`str`
    
    """

    ID: str = Field("deviceTokenBlackBerryPush", alias="@type")
    token: str

    @staticmethod
    def read(q: dict) -> DeviceTokenBlackBerryPush:
        return DeviceTokenBlackBerryPush.construct(**q)


class DeviceTokenFirebaseCloudMessaging(DeviceToken):
    """
    A token for Firebase Cloud Messaging
    
    :param token: Device registration token; may be empty to de-register a device
    :type token: :class:`str`
    
    :param encrypt: True, if push notifications should be additionally encrypted
    :type encrypt: :class:`bool`
    
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
    
    :param channel_uri: Push notification channel URI; may be empty to de-register a device
    :type channel_uri: :class:`str`
    
    """

    ID: str = Field("deviceTokenMicrosoftPush", alias="@type")
    channel_uri: str

    @staticmethod
    def read(q: dict) -> DeviceTokenMicrosoftPush:
        return DeviceTokenMicrosoftPush.construct(**q)


class DeviceTokenMicrosoftPushVoIP(DeviceToken):
    """
    A token for Microsoft Push Notification Service VoIP channel
    
    :param channel_uri: Push notification channel URI; may be empty to de-register a device
    :type channel_uri: :class:`str`
    
    """

    ID: str = Field("deviceTokenMicrosoftPushVoIP", alias="@type")
    channel_uri: str

    @staticmethod
    def read(q: dict) -> DeviceTokenMicrosoftPushVoIP:
        return DeviceTokenMicrosoftPushVoIP.construct(**q)


class DeviceTokenSimplePush(DeviceToken):
    """
    A token for Simple Push API for Firefox OS
    
    :param endpoint: Absolute URL exposed by the push service where the application server can send push messages; may be empty to de-register a device
    :type endpoint: :class:`str`
    
    """

    ID: str = Field("deviceTokenSimplePush", alias="@type")
    endpoint: str

    @staticmethod
    def read(q: dict) -> DeviceTokenSimplePush:
        return DeviceTokenSimplePush.construct(**q)


class DeviceTokenTizenPush(DeviceToken):
    """
    A token for Tizen Push Service
    
    :param reg_id: Push service registration identifier; may be empty to de-register a device
    :type reg_id: :class:`str`
    
    """

    ID: str = Field("deviceTokenTizenPush", alias="@type")
    reg_id: str

    @staticmethod
    def read(q: dict) -> DeviceTokenTizenPush:
        return DeviceTokenTizenPush.construct(**q)


class DeviceTokenUbuntuPush(DeviceToken):
    """
    A token for Ubuntu Push Client service
    
    :param token: Token; may be empty to de-register a device
    :type token: :class:`str`
    
    """

    ID: str = Field("deviceTokenUbuntuPush", alias="@type")
    token: str

    @staticmethod
    def read(q: dict) -> DeviceTokenUbuntuPush:
        return DeviceTokenUbuntuPush.construct(**q)


class DeviceTokenWebPush(DeviceToken):
    """
    A token for web Push API
    
    :param endpoint: Absolute URL exposed by the push service where the application server can send push messages; may be empty to de-register a device
    :type endpoint: :class:`str`
    
    :param p256dh_base64url: Base64url-encoded P-256 elliptic curve Diffie-Hellman public key
    :type p256dh_base64url: :class:`str`
    
    :param auth_base64url: Base64url-encoded authentication secret
    :type auth_base64url: :class:`str`
    
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
    
    :param access_token: The access token that will be used to send notifications; may be empty to de-register a device
    :type access_token: :class:`str`
    
    """

    ID: str = Field("deviceTokenWindowsPush", alias="@type")
    access_token: str

    @staticmethod
    def read(q: dict) -> DeviceTokenWindowsPush:
        return DeviceTokenWindowsPush.construct(**q)
