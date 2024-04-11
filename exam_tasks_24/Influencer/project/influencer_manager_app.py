from typing import List

from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:

    VALID_TYPE_INFLUENCER = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGN = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}
    
    def __init__(self):
        self.influencers: List = []
        self.campaigns: List = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_TYPE_INFLUENCER:
            return f"{influencer_type} is not an allowed influencer type."
        if self._find_inluencer_name(username):
            return f"{username} is already registered."
        new_influencer = self.VALID_TYPE_INFLUENCER[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN:
            return f"{campaign_type} is not a valid campaign type."
        if self._find_id_compaign(campaign_id):
            return f"Campaign ID {campaign_id} has already been created."
        new_compaign = self.VALID_CAMPAIGN[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_compaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        if self._find_inluencer_name(influencer_username) is None:
            return f"Influencer '{influencer_username}' not found."
        if self._find_id_compaign(campaign_id):
            return f"Campaign with ID {campaign_id} not found."

    def calculate_total_reached_followers(self):
        pass

    def influencer_campaign_report(self, username: str):
        pass

    def campaign_statistics(self):
        pass

    def _find_inluencer_name(self, name):
        return next((n for n in self.influencers if n.username == name), None)

    def _find_id_compaign(self, camp_id):
        return next((i for i in self.campaigns if i.campaign_id == camp_id ), None)
