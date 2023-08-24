from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Affiliate, Post, Campaign
from .forms import AffiliateForm, PostForm, CampaignForm


def index(request):
    """The home page for the affiliate marketing app."""
    top_campaigns = Campaign.objects.filter(
        status='active').order_by('-start_date')[:3]
    top_posts = Post.objects.filter(
        status='published').order_by('-views')[:3]
    top_affiliates = Affiliate.objects.filter(
        status='active').order_by('-facebook_followers')[:3]

    context = {
        'top_campaigns': top_campaigns,
        'top_posts': top_posts,
        'top_affiliates': top_affiliates,
    }

    return render(request, 'affiliates/index.html', context)


class CampaignsListView(ListView):
    """A view for listing all campaigns."""

    model = Campaign


class CampaignDetailsView(DetailView):
    """A view for displaying a single campaign and its posts."""

    model = Campaign

    def get_context_data(self, **kwargs):
        """Gets the context data for the view."""
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.filter(
            status='published').order_by('-views')

        return context


class CreateCampaignView(CreateView):
    """A view for creating a new campaign."""

    model = Campaign
    form_class = CampaignForm


class PostDetailsView(DetailView):
    """A view for displaying a single post."""

    model = Post


class CreatePostView(CreateView):
    """A view for creating a new post."""

    model = Post
    form_class = PostForm


def AffiliatesListView(request):
    """A view for listing all affiliates."""
    context={}
    context['affiliates'] = Affiliate.objects.all()
    return render(request, 'affiliate_list.html', context)


class AffiliateDetailsView(DetailView):
    """A view for displaying a single affiliate and their posts."""

    model = Affiliate

    def get_context_data(self, **kwargs):
        """Gets the context data for the view."""
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.filter(
            status='published').order_by('-views')

        return context


class CreateAffiliateView(CreateView):
    """A view for creating a new affiliate."""

    model = Affiliate
    form_class = AffiliateForm

