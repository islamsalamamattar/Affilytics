from django import forms
from .models import Affiliate, Post, Campaign


class AffiliateForm(forms.ModelForm):
    """A form for creating and editing affiliates."""

    class Meta:
        model = Affiliate
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'facebook',
            'twitter',
            'instagram',
            'youtube',
            'profile_pic',
        )


class PostForm(forms.ModelForm):
    """A form for creating and editing posts."""

    class Meta:
        model = Post
        fields = (
            'affiliate',
            'campaign',
            'content',
            'platform',
            'type',
            'views',
            'likes',
            'shares',
            'money_paid_per_post',
        )


class CampaignForm(forms.ModelForm):
    """A form for creating and editing campaigns."""

    class Meta:
        model = Campaign
        fields = (
            'name',
            'customer',
            'start_date',
            'end_date',
            'budget',
        )

