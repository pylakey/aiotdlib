# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .formatted_text import FormattedText
from .proxy_type import ProxyType
from ..base_object import BaseObject


class InternalLinkType(BaseObject):
    """
    Describes an internal https://t.me or tg: link, which must be processed by the app in a special way
    
    """

    ID: str = Field("internalLinkType", alias="@type")


class InternalLinkTypeActiveSessions(InternalLinkType):
    """
    The link is a link to the active sessions section of the app. Use getActiveSessions to handle the link
    
    """

    ID: str = Field("internalLinkTypeActiveSessions", alias="@type")

    @staticmethod
    def read(q: dict) -> InternalLinkTypeActiveSessions:
        return InternalLinkTypeActiveSessions.construct(**q)


class InternalLinkTypeAuthenticationCode(InternalLinkType):
    """
    The link contains an authentication code. Call checkAuthenticationCode with the code if the current authorization state is authorizationStateWaitCode
    
    Params:
        code (:class:`str`)
            The authentication code
        
    """

    ID: str = Field("internalLinkTypeAuthenticationCode", alias="@type")
    code: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeAuthenticationCode:
        return InternalLinkTypeAuthenticationCode.construct(**q)


class InternalLinkTypeBackground(InternalLinkType):
    """
    The link is a link to a background. Call searchBackground with the given background name to process the link
    
    Params:
        background_name (:class:`str`)
            Name of the background
        
    """

    ID: str = Field("internalLinkTypeBackground", alias="@type")
    background_name: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeBackground:
        return InternalLinkTypeBackground.construct(**q)


class InternalLinkTypeBotStart(InternalLinkType):
    """
    The link is a link to a chat with a Telegram bot. Call searchPublicChat with the given bot username, check that the user is a bot, show START button in the chat with the bot, and then call sendBotStartMessage with the given start parameter after the button is pressed
    
    Params:
        bot_username (:class:`str`)
            Username of the bot
        
        start_parameter (:class:`str`)
            The parameter to be passed to sendBotStartMessage
        
    """

    ID: str = Field("internalLinkTypeBotStart", alias="@type")
    bot_username: str
    start_parameter: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeBotStart:
        return InternalLinkTypeBotStart.construct(**q)


class InternalLinkTypeBotStartInGroup(InternalLinkType):
    """
    The link is a link to a Telegram bot, which is supposed to be added to a group chat. Call searchPublicChat with the given bot username, check that the user is a bot and can be added to groups, ask the current user to select a group to add the bot to, and then call sendBotStartMessage with the given start parameter and the chosen group chat. Bots can be added to a public group only by administrators of the group
    
    Params:
        bot_username (:class:`str`)
            Username of the bot
        
        start_parameter (:class:`str`)
            The parameter to be passed to sendBotStartMessage
        
    """

    ID: str = Field("internalLinkTypeBotStartInGroup", alias="@type")
    bot_username: str
    start_parameter: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeBotStartInGroup:
        return InternalLinkTypeBotStartInGroup.construct(**q)


class InternalLinkTypeChangePhoneNumber(InternalLinkType):
    """
    The link is a link to the change phone number section of the app
    
    """

    ID: str = Field("internalLinkTypeChangePhoneNumber", alias="@type")

    @staticmethod
    def read(q: dict) -> InternalLinkTypeChangePhoneNumber:
        return InternalLinkTypeChangePhoneNumber.construct(**q)


class InternalLinkTypeChatInvite(InternalLinkType):
    """
    The link is a chat invite link. Call checkChatInviteLink to process the link
    
    """

    ID: str = Field("internalLinkTypeChatInvite", alias="@type")

    @staticmethod
    def read(q: dict) -> InternalLinkTypeChatInvite:
        return InternalLinkTypeChatInvite.construct(**q)


class InternalLinkTypeFilterSettings(InternalLinkType):
    """
    The link is a link to the filter settings section of the app
    
    """

    ID: str = Field("internalLinkTypeFilterSettings", alias="@type")

    @staticmethod
    def read(q: dict) -> InternalLinkTypeFilterSettings:
        return InternalLinkTypeFilterSettings.construct(**q)


class InternalLinkTypeGame(InternalLinkType):
    """
    The link is a link to a game. Call searchPublicChat with the given bot username, check that the user is a bot, ask the current user to select a group to send the game, and then call sendMessage with inputMessageGame
    
    Params:
        bot_username (:class:`str`)
            Username of the bot that owns the game
        
        game_short_name (:class:`str`)
            Short name of the game
        
    """

    ID: str = Field("internalLinkTypeGame", alias="@type")
    bot_username: str
    game_short_name: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeGame:
        return InternalLinkTypeGame.construct(**q)


class InternalLinkTypeLanguagePack(InternalLinkType):
    """
    The link is a link to a language pack. Call getLanguagePackInfo with the given language pack identifier to process the link
    
    Params:
        language_pack_id (:class:`str`)
            Language pack identifier
        
    """

    ID: str = Field("internalLinkTypeLanguagePack", alias="@type")
    language_pack_id: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeLanguagePack:
        return InternalLinkTypeLanguagePack.construct(**q)


class InternalLinkTypeMessage(InternalLinkType):
    """
    The link is a link to a Telegram message. Call getMessageLinkInfo to process the link
    
    """

    ID: str = Field("internalLinkTypeMessage", alias="@type")

    @staticmethod
    def read(q: dict) -> InternalLinkTypeMessage:
        return InternalLinkTypeMessage.construct(**q)


class InternalLinkTypeMessageDraft(InternalLinkType):
    """
    The link contains a message draft text. A share screen needs to be shown to the user, then the chosen chat should be open and the text should be added to the input field
    
    Params:
        text (:class:`FormattedText`)
            Message draft text
        
        contains_link (:class:`bool`)
            True, if the first line of the text contains a link. If true, the input field needs to be focused and the text after the link should be selected
        
    """

    ID: str = Field("internalLinkTypeMessageDraft", alias="@type")
    text: FormattedText
    contains_link: bool

    @staticmethod
    def read(q: dict) -> InternalLinkTypeMessageDraft:
        return InternalLinkTypeMessageDraft.construct(**q)


class InternalLinkTypePassportDataRequest(InternalLinkType):
    """
    The link contains a request of Telegram passport data. Call getPassportAuthorizationForm to process the link if the link was received outside of the app, otherwise ignore it
    
    Params:
        bot_user_id (:class:`int`)
            User identifier of the service's bot
        
        scope (:class:`str`)
            Telegram Passport element types requested by the service
        
        public_key (:class:`str`)
            Service's public key
        
        nonce (:class:`str`)
            Unique request identifier provided by the service
        
        callback_url (:class:`str`)
            An HTTP URL to open once the request is finished or canceled with the parameter tg_passport=success or tg_passport=cancel respectively. If empty, then the link tgbot{bot_user_id}://passport/success or tgbot{bot_user_id}://passport/cancel needs to be opened instead
        
    """

    ID: str = Field("internalLinkTypePassportDataRequest", alias="@type")
    bot_user_id: int
    scope: str
    public_key: str
    nonce: str
    callback_url: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypePassportDataRequest:
        return InternalLinkTypePassportDataRequest.construct(**q)


class InternalLinkTypePhoneNumberConfirmation(InternalLinkType):
    """
    The link can be used to confirm ownership of a phone number to prevent account deletion. Call sendPhoneNumberConfirmationCode with the given hash and phone number to process the link
    
    Params:
        hash_ (:class:`str`)
            Hash value from the link
        
        phone_number (:class:`str`)
            Phone number value from the link
        
    """

    ID: str = Field("internalLinkTypePhoneNumberConfirmation", alias="@type")
    hash_: str = Field(..., alias='hash')
    phone_number: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypePhoneNumberConfirmation:
        return InternalLinkTypePhoneNumberConfirmation.construct(**q)


class InternalLinkTypeProxy(InternalLinkType):
    """
    The link is a link to a proxy. Call addProxy to process the link and add the proxy
    
    Params:
        server (:class:`str`)
            Proxy server IP address
        
        port (:class:`int`)
            Proxy server port
        
        type_ (:class:`ProxyType`)
            Type of the proxy
        
    """

    ID: str = Field("internalLinkTypeProxy", alias="@type")
    server: str
    port: int
    type_: ProxyType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> InternalLinkTypeProxy:
        return InternalLinkTypeProxy.construct(**q)


class InternalLinkTypePublicChat(InternalLinkType):
    """
    The link is a link to a chat by its username. Call searchPublicChat with the given chat username to process the link
    
    Params:
        chat_username (:class:`str`)
            Username of the chat
        
    """

    ID: str = Field("internalLinkTypePublicChat", alias="@type")
    chat_username: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypePublicChat:
        return InternalLinkTypePublicChat.construct(**q)


class InternalLinkTypeQrCodeAuthentication(InternalLinkType):
    """
    The link can be used to login the current user on another device, but it must be scanned from QR-code using in-app camera. An alert similar to "This code can be used to allow someone to log in to your Telegram account. To confirm Telegram login, please go to Settings > Devices > Scan QR and scan the code" needs to be shown
    
    """

    ID: str = Field("internalLinkTypeQrCodeAuthentication", alias="@type")

    @staticmethod
    def read(q: dict) -> InternalLinkTypeQrCodeAuthentication:
        return InternalLinkTypeQrCodeAuthentication.construct(**q)


class InternalLinkTypeSettings(InternalLinkType):
    """
    The link is a link to app settings
    
    """

    ID: str = Field("internalLinkTypeSettings", alias="@type")

    @staticmethod
    def read(q: dict) -> InternalLinkTypeSettings:
        return InternalLinkTypeSettings.construct(**q)


class InternalLinkTypeStickerSet(InternalLinkType):
    """
    The link is a link to a sticker set. Call searchStickerSet with the given sticker set name to process the link and show the sticker set
    
    Params:
        sticker_set_name (:class:`str`)
            Name of the sticker set
        
    """

    ID: str = Field("internalLinkTypeStickerSet", alias="@type")
    sticker_set_name: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeStickerSet:
        return InternalLinkTypeStickerSet.construct(**q)


class InternalLinkTypeTheme(InternalLinkType):
    """
    The link is a link to a theme. TDLib has no theme support yet
    
    Params:
        theme_name (:class:`str`)
            Name of the theme
        
    """

    ID: str = Field("internalLinkTypeTheme", alias="@type")
    theme_name: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeTheme:
        return InternalLinkTypeTheme.construct(**q)


class InternalLinkTypeThemeSettings(InternalLinkType):
    """
    The link is a link to the theme settings section of the app
    
    """

    ID: str = Field("internalLinkTypeThemeSettings", alias="@type")

    @staticmethod
    def read(q: dict) -> InternalLinkTypeThemeSettings:
        return InternalLinkTypeThemeSettings.construct(**q)


class InternalLinkTypeUnknownDeepLink(InternalLinkType):
    """
    The link is an unknown tg: link. Call getDeepLinkInfo to process the link
    
    """

    ID: str = Field("internalLinkTypeUnknownDeepLink", alias="@type")

    @staticmethod
    def read(q: dict) -> InternalLinkTypeUnknownDeepLink:
        return InternalLinkTypeUnknownDeepLink.construct(**q)


class InternalLinkTypeVoiceChat(InternalLinkType):
    """
    The link is a link to a voice chat. Call searchPublicChat with the given chat username, and then joinGoupCall with the given invite hash to process the link
    
    Params:
        chat_username (:class:`str`)
            Username of the chat with the voice chat
        
        invite_hash (:class:`str`)
            If non-empty, invite hash to be used to join the voice chat without being muted by administrators
        
    """

    ID: str = Field("internalLinkTypeVoiceChat", alias="@type")
    chat_username: str
    invite_hash: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeVoiceChat:
        return InternalLinkTypeVoiceChat.construct(**q)
