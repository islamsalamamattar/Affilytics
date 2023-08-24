from django.contrib import admin
from .models import Affiliate, Partner, Post, Campaign, Promocode, Invoice

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'contact_name', 'conatct_position', 'email', 'phone_number')
    list_filter = ('type',)
    search_fields = ('brand_name', 'contact_name', 'email', 'phone_number')

@admin.register(Affiliate)
class AffiliateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number',
                    'facebook_followers', 'twitter_followers',
                    'instagram_followers', 'youtube_subscribers')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('affiliate', 'campaign', 'content', 'platform',
                    'type', 'views', 'likes', 'shares', 'money_paid_per_post',
                    'spending')
    list_filter = ('affiliate', 'campaign', 'platform', 'type')
    search_fields = ('content',)

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'budget',
                    'spending', 'effectiveness')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'customer')

@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'affiliate', 'type', 'start_date',
                    'end_date')
    list_filter = ('campaign', 'affiliate', 'type')
    search_fields = ('campaign__name', 'affiliate__first_name', 'affiliate__last_name')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('partner', 'affiliate', 'campaign', 'amount',
                    'payment_status', 'payment_method', 'payment_date')
    list_filter = ('partner', 'affiliate', 'campaign', 'payment_status', 'payment_method', 'invoice_month')
    search_fields = ('partner__brand_name', 'affiliate__first_name', 'affiliate__last_name', 'campaign__name')
    ordering = ('-created_at',)
