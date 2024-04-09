from abc import ABC, abstractmethod
from typing import List

from project.campaigns.base_campaign import BaseCampaign


class BaseInfluencer(ABC):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated: List = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if value.strip() == '':
            raise ValueError("Username cannot be empty or consist only of whitespace!")
        self._username = value

    @property
    def followers(self):
        return self._followers

    @followers.setter
    def followers(self, value):
        if value < 0:
            raise ValueError("Followers must be a non-negative integer!")
        self._followers = value

    @property
    def engagement_rate(self):
        return self._engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, value):
        if value < 0.0 or value > 5.0:
            raise ValueError("Engagement rate should be between 0 and 5.")
        self._engagement_rate = value

    @abstractmethod
    def calculate_payment(self, campaign: BaseCampaign):
        pass

    @abstractmethod
    def eached_followers(self, campaign_type: str):
        pass

    def display_campaigns_participated(self):
        pass