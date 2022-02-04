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
    
    :param code: The authentication code
    :type code: :class:`str`
    
    """

    ID: str = Field("internalLinkTypeAuthenticationCode", alias="@type")
    code: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeAuthenticationCode:
        return InternalLinkTypeAuthenticationCode.construct(**q)


class InternalLinkTypeBackground(InternalLinkType):
    """
    The link is a link to a background. Call searchBackground with the given background name to process the link
    
    :param background_name: Name of the background
    :type background_name: :class:`str`
    
    """

    ID: str = Field("internalLinkTypeBackground", alias="@type")
    background_name: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeBackground:
        return InternalLinkTypeBackground.construct(**q)


class InternalLinkTypeBotStart(InternalLinkType):
    """
    The link is a link to a chat with a Telegram bot. Call searchPublicChat with the given bot username, check that the user is a bot, show START button in the chat with the bot, and then call sendBotStartMessage with the given start parameter after the button is pressed
    
    :param bot_username: Username of the bot
    :type bot_username: :class:`str`
    
    :param start_parameter: The parameter to be passed to sendBotStartMessage
    :type start_parameter: :class:`str`
    
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
    
    :param bot_username: Username of the bot
    :type bot_username: :class:`str`
    
    :param start_parameter: The parameter to be passed to sendBotStartMessage
    :type start_parameter: :class:`str`
    
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
    The link is a chat invite link. Call checkChatInviteLink with the given invite link to process the link
    
    :param invite_link: Internal representation of the invite link
    :type invite_link: :class:`str`
    
    """

    ID: str = Field("internalLinkTypeChatInvite", alias="@type")
    invite_link: str

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
    The link is a link to a game. Call searchPublicChat with the given bot username, check that the user is a bot, ask the current user to select a chat to send the game, and then call sendMessage with inputMessageGame
    
    :param bot_username: Username of the bot that owns the game
    :type bot_username: :class:`str`
    
    :param game_short_name: Short name of the game
    :type game_short_name: :class:`str`
    
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
    
    :param language_pack_id: Language pack identifier
    :type language_pack_id: :class:`str`
    
    """

    ID: str = Field("internalLinkTypeLanguagePack", alias="@type")
    language_pack_id: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeLanguagePack:
        return InternalLinkTypeLanguagePack.construct(**q)


class InternalLinkTypeMessage(InternalLinkType):
    """
    The link is a link to a Telegram message. Call getMessageLinkInfo with the given URL to process the link
    
    :param url: URL to be passed to getMessageLinkInfo
    :type url: :class:`str`
    
    """

    ID: str = Field("internalLinkTypeMessage", alias="@type")
    url: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeMessage:
        return InternalLinkTypeMessage.construct(**q)


class InternalLinkTypeMessageDraft(InternalLinkType):
    """
    The link contains a message draft text. A share screen needs to be shown to the user, then the chosen chat must be opened and the text is added to the input field
    
    :param text: Message draft text
    :type text: :class:`FormattedText`
    
    :param contains_link: True, if the first line of the text contains a link. If true, the input field needs to be focused and the text after the link must be selected
    :type contains_link: :class:`bool`
    
    """

    ID: str = Field("internalLinkTypeMessageDraft", alias="@type")
    text: FormattedText
    contains_link: bool

    @staticmethod
    def read(q: dict) -> InternalLinkTypeMessageDraft:
        return InternalLinkTypeMessageDraft.construct(**q)


class InternalLinkTypePassportDataRequest(InternalLinkType):
    """
    The link contains a request of Telegram passport data. Call getPassportAuthorizationForm with the given parameters to process the link if the link was received from outside of the app, otherwise ignore it
    
    :param bot_user_id: User identifier of the service's bot
    :type bot_user_id: :class:`int`
    
    :param scope: Telegram Passport element types requested by the service
    :type scope: :class:`str`
    
    :param public_key: Service's public key
    :type public_key: :class:`str`
    
    :param nonce: Unique request identifier provided by the service
    :type nonce: :class:`str`
    
    :param callback_url: An HTTP URL to open once the request is finished or canceled with the parameter tg_passport=success or tg_passport=cancel respectively. If empty, then the link tgbot{bot_user_id}://passport/success or tgbot{bot_user_id}://passport/cancel needs to be opened instead
    :type callback_url: :class:`str`
    
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
    
    :param hash_: Hash value from the link
    :type hash_: :class:`str`
    
    :param phone_number: Phone number value from the link
    :type phone_number: :class:`str`
    
    """

    ID: str = Field("internalLinkTypePhoneNumberConfirmation", alias="@type")
    hash_: str = Field(..., alias='hash')
    phone_number: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypePhoneNumberConfirmation:
        return InternalLinkTypePhoneNumberConfirmation.construct(**q)


class InternalLinkTypeProxy(InternalLinkType):
    """
    The link is a link to a proxy. Call addProxy with the given parameters to process the link and add the proxy
    
    :param server: Proxy server IP address
    :type server: :class:`str`
    
    :param port: Proxy server port
    :type port: :class:`int`
    
    :param type_: Type of the proxy
    :type type_: :class:`ProxyType`
    
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
    
    :param chat_username: Username of the chat
    :type chat_username: :class:`str`
    
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
    
    :param sticker_set_name: Name of the sticker set
    :type sticker_set_name: :class:`str`
    
    """

    ID: str = Field("internalLinkTypeStickerSet", alias="@type")
    sticker_set_name: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeStickerSet:
        return InternalLinkTypeStickerSet.construct(**q)


class InternalLinkTypeTheme(InternalLinkType):
    """
    The link is a link to a theme. TDLib has no theme support yet
    
    :param theme_name: Name of the theme
    :type theme_name: :class:`str`
    
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
    
    :param link: Link to be passed to getDeepLinkInfo
    :type link: :class:`str`
    
    """

    ID: str = Field("internalLinkTypeUnknownDeepLink", alias="@type")
    link: str

    @staticmethod
    def read(q: dict) -> InternalLinkTypeUnknownDeepLink:
        return InternalLinkTypeUnknownDeepLink.construct(**q)


class InternalLinkTypeUnsupportedProxy(InternalLinkType):
    """
    The link is a link to an unsupported proxy. An alert can be shown to the user
    
    """

    ID: str = Field("internalLinkTypeUnsupportedProxy", alias="@type")

    @staticmethod
    def read(q: dict) -> InternalLinkTypeUnsupportedProxy:
        return InternalLinkTypeUnsupportedProxy.construct(**q)


class InternalLinkTypeVideoChat(InternalLinkType):
    """
    The link is a link to a video chat. Call searchPublicChat with the given chat username, and then joinGroupCall with the given invite hash to process the link
    
    :param chat_username: Username of the chat with the video chat
    :type chat_username: :class:`str`
    
    :param invite_hash: If non-empty, invite hash to be used to join the video chat without being muted by administrators
    :type invite_hash: :class:`str`
    
    :param is_live_stream: True, if the video chat is expected to be a live stream in a channel or a broadcast group
    :type is_live_stream: :class:`bool`
    
    """

    ID: str = Field("internalLinkTypeVideoChat", alias="@type")
    chat_username: str
    invite_hash: str
    is_live_stream: bool

    @staticmethod
    def read(q: dict) -> InternalLinkTypeVideoChat:
        return InternalLinkTypeVideoChat.construct(**q)
