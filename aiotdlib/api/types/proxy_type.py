# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ProxyType(BaseObject):
    """
    Describes the type of a proxy server
    
    """

    ID: str = Field("proxyType", alias="@type")


class ProxyTypeHttp(ProxyType):
    """
    A HTTP transparent proxy server
    
    Params:
        username (:class:`str`)
            Username for logging in; may be empty
        
        password (:class:`str`)
            Password for logging in; may be empty
        
        http_only (:class:`bool`)
            Pass true if the proxy supports only HTTP requests and doesn't support transparent TCP connections via HTTP CONNECT method
        
    """

    ID: str = Field("proxyTypeHttp", alias="@type")
    username: str
    password: str
    http_only: bool

    @staticmethod
    def read(q: dict) -> ProxyTypeHttp:
        return ProxyTypeHttp.construct(**q)


class ProxyTypeMtproto(ProxyType):
    """
    An MTProto proxy server
    
    Params:
        secret (:class:`str`)
            The proxy's secret in hexadecimal encoding
        
    """

    ID: str = Field("proxyTypeMtproto", alias="@type")
    secret: str

    @staticmethod
    def read(q: dict) -> ProxyTypeMtproto:
        return ProxyTypeMtproto.construct(**q)


class ProxyTypeSocks5(ProxyType):
    """
    A SOCKS5 proxy server
    
    Params:
        username (:class:`str`)
            Username for logging in; may be empty
        
        password (:class:`str`)
            Password for logging in; may be empty
        
    """

    ID: str = Field("proxyTypeSocks5", alias="@type")
    username: str
    password: str

    @staticmethod
    def read(q: dict) -> ProxyTypeSocks5:
        return ProxyTypeSocks5.construct(**q)
