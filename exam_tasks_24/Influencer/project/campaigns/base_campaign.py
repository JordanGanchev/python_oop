from abc import ABC, abstractmethod
from typing import List


class BaseCampaign(ABC):
    _unic_campaign_id = set()

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers: List = []

    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        if value < 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")
        if value in self._unic_campaign_id:
            raise ValueError(f"Campaign with ID {value} already exists. Campaign IDs must be unique.")
        self._unic_campaign_id.add(value)
        self._campaign_id = value

    @abstractmethod
    def check_eligibility(self, engagement_rate: float):
        pass