# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_statistics_administrator_actions_info import ChatStatisticsAdministratorActionsInfo
from .chat_statistics_inviter_info import ChatStatisticsInviterInfo
from .chat_statistics_message_interaction_info import ChatStatisticsMessageInteractionInfo
from .chat_statistics_message_sender_info import ChatStatisticsMessageSenderInfo
from .date_range import DateRange
from .statistical_graph import StatisticalGraph
from .statistical_value import StatisticalValue
from ..base_object import BaseObject


class ChatStatistics(BaseObject):
    """
    Contains a detailed statistics about a chat
    
    """

    ID: str = Field("chatStatistics", alias="@type")


class ChatStatisticsChannel(ChatStatistics):
    """
    A detailed statistics about a channel chat
    
    Params:
        period (:class:`DateRange`)
            A period to which the statistics applies
        
        member_count (:class:`StatisticalValue`)
            Number of members in the chat
        
        mean_view_count (:class:`StatisticalValue`)
            Mean number of times the recently sent messages was viewed
        
        mean_share_count (:class:`StatisticalValue`)
            Mean number of times the recently sent messages was shared
        
        enabled_notifications_percentage (:class:`float`)
            A percentage of users with enabled notifications for the chat
        
        member_count_graph (:class:`StatisticalGraph`)
            A graph containing number of members in the chat
        
        join_graph (:class:`StatisticalGraph`)
            A graph containing number of members joined and left the chat
        
        mute_graph (:class:`StatisticalGraph`)
            A graph containing number of members muted and unmuted the chat
        
        view_count_by_hour_graph (:class:`StatisticalGraph`)
            A graph containing number of message views in a given hour in the last two weeks
        
        view_count_by_source_graph (:class:`StatisticalGraph`)
            A graph containing number of message views per source
        
        join_by_source_graph (:class:`StatisticalGraph`)
            A graph containing number of new member joins per source
        
        language_graph (:class:`StatisticalGraph`)
            A graph containing number of users viewed chat messages per language
        
        message_interaction_graph (:class:`StatisticalGraph`)
            A graph containing number of chat message views and shares
        
        instant_view_interaction_graph (:class:`StatisticalGraph`)
            A graph containing number of views of associated with the chat instant views
        
        recent_message_interactions (:obj:`list[ChatStatisticsMessageInteractionInfo]`)
            Detailed statistics about number of views and shares of recently sent messages
        
    """

    ID: str = Field("chatStatisticsChannel", alias="@type")
    period: DateRange
    member_count: StatisticalValue
    mean_view_count: StatisticalValue
    mean_share_count: StatisticalValue
    enabled_notifications_percentage: float
    member_count_graph: StatisticalGraph
    join_graph: StatisticalGraph
    mute_graph: StatisticalGraph
    view_count_by_hour_graph: StatisticalGraph
    view_count_by_source_graph: StatisticalGraph
    join_by_source_graph: StatisticalGraph
    language_graph: StatisticalGraph
    message_interaction_graph: StatisticalGraph
    instant_view_interaction_graph: StatisticalGraph
    recent_message_interactions: list[ChatStatisticsMessageInteractionInfo]

    @staticmethod
    def read(q: dict) -> ChatStatisticsChannel:
        return ChatStatisticsChannel.construct(**q)


class ChatStatisticsSupergroup(ChatStatistics):
    """
    A detailed statistics about a supergroup chat
    
    Params:
        period (:class:`DateRange`)
            A period to which the statistics applies
        
        member_count (:class:`StatisticalValue`)
            Number of members in the chat
        
        message_count (:class:`StatisticalValue`)
            Number of messages sent to the chat
        
        viewer_count (:class:`StatisticalValue`)
            Number of users who viewed messages in the chat
        
        sender_count (:class:`StatisticalValue`)
            Number of users who sent messages to the chat
        
        member_count_graph (:class:`StatisticalGraph`)
            A graph containing number of members in the chat
        
        join_graph (:class:`StatisticalGraph`)
            A graph containing number of members joined and left the chat
        
        join_by_source_graph (:class:`StatisticalGraph`)
            A graph containing number of new member joins per source
        
        language_graph (:class:`StatisticalGraph`)
            A graph containing distribution of active users per language
        
        message_content_graph (:class:`StatisticalGraph`)
            A graph containing distribution of sent messages by content type
        
        action_graph (:class:`StatisticalGraph`)
            A graph containing number of different actions in the chat
        
        day_graph (:class:`StatisticalGraph`)
            A graph containing distribution of message views per hour
        
        week_graph (:class:`StatisticalGraph`)
            A graph containing distribution of message views per day of week
        
        top_senders (:obj:`list[ChatStatisticsMessageSenderInfo]`)
            List of users sent most messages in the last week
        
        top_administrators (:obj:`list[ChatStatisticsAdministratorActionsInfo]`)
            List of most active administrators in the last week
        
        top_inviters (:obj:`list[ChatStatisticsInviterInfo]`)
            List of most active inviters of new members in the last week
        
    """

    ID: str = Field("chatStatisticsSupergroup", alias="@type")
    period: DateRange
    member_count: StatisticalValue
    message_count: StatisticalValue
    viewer_count: StatisticalValue
    sender_count: StatisticalValue
    member_count_graph: StatisticalGraph
    join_graph: StatisticalGraph
    join_by_source_graph: StatisticalGraph
    language_graph: StatisticalGraph
    message_content_graph: StatisticalGraph
    action_graph: StatisticalGraph
    day_graph: StatisticalGraph
    week_graph: StatisticalGraph
    top_senders: list[ChatStatisticsMessageSenderInfo]
    top_administrators: list[ChatStatisticsAdministratorActionsInfo]
    top_inviters: list[ChatStatisticsInviterInfo]

    @staticmethod
    def read(q: dict) -> ChatStatisticsSupergroup:
        return ChatStatisticsSupergroup.construct(**q)
