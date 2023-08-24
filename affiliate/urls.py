from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('campaigns/', views.CampaignsListView.as_view(), name='campaigns'),
    path('campaigns/<int:pk>', views.CampaignDetailsView.as_view(), name='campaign_details'),
    path('campaigns/create/', views.CreateCampaignView.as_view(), name='create_campaign'),
    path('posts/<int:pk>', views.PostDetailsView.as_view(), name='post_details'),
    path('posts/create/', views.CreatePostView.as_view(), name='create_post'),
    path('affiliates/', views.AffiliatesListView, name='affiliates'),
    path('affiliates/<int:pk>', views.AffiliateDetailsView.as_view(), name='affiliate_details'),
    path('affiliates/create/', views.CreateAffiliateView.as_view(), name='create_affiliate'),
]

