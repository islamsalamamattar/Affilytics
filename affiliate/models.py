from django.db import models


class Affiliate(models.Model):
    """A model for representing affiliates (influencers)."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)

    # Social media handles
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)

    profile_pic = models.ImageField(upload_to='affiliates/profile_pics')

    # Social media numbers
    facebook_followers = models.IntegerField(default=0)
    twitter_followers = models.IntegerField(default=0)
    instagram_followers = models.IntegerField(default=0)
    youtube_subscribers = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of the affiliate."""
        return f'{self.first_name} {self.last_name}'
    
class Partner(models.Model):
    """A model for representing Partners (Brands)."""

    brand_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    conatct_position = models.CharField(max_length=255) 
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    type = models.CharField(max_length=25, choices=(('agency','agency'), ('brand','brand'), ('seller','seller')))

    # Social media handles
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    # Brand logo
    logo = models.ImageField(upload_to='Partner/logo')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of the partner."""
        return f'{self.brand_name} {self.contact_name}'

class Post(models.Model):
    """A model for representing posts by affiliates for marketing campaigns."""

    affiliate = models.ForeignKey('Affiliate', on_delete=models.CASCADE, related_name='posts_affiliate')
    campaign = models.ForeignKey('Campaign', on_delete=models.CASCADE, related_name='posts_campaign')
    content = models.TextField()

    platform = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    money_paid_per_post = models.IntegerField(default=0)
    spending = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of the post."""
        return f'{self.affiliate}: {self.content} ({self.platform}, {self.type})'

class Campaign(models.Model):
    """A model for representing marketing campaigns."""

    name = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    budget = models.IntegerField()
    spending = models.IntegerField(default=0)
    effectiveness = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of the campaign."""
        return f'{self.name} ({self.start_date} - {self.end_date})'


class Promocode(models.Model):
    """A model for representing Promocodes for affiliates for marketing campaigns."""

    campaign = models.ForeignKey('Campaign', on_delete=models.CASCADE, related_name='posts')
    affiliate = models.ForeignKey('Affiliate', on_delete=models.CASCADE, related_name='posts')
    type = models.CharField(max_length=25, choices=(('promo_code', 'Promotional Code'), ('dynamic_link', 'Dynamic Link')))
    promo_code = models.CharField(max_length=25, null=True)
    dynamic_link = models.URLField(max_length=300, null=True)
    commission_type = models.CharField(max_length=25, choices=(('percentage','percentage'), ('fixed_fee','fixed_fee')))
    commission_rate = models.IntegerField(default=0)

    start_date = models.DateField()
    end_date = models.DateField()

    promo_code_conv = models.IntegerField(default=0)
    dynamic_link_conv = models.IntegerField(default=0)

    shares = models.IntegerField(default=0)
    money_paid_per_post = models.IntegerField(default=0)
    spending = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of the post."""
        return f'{self.campaign}: {self.affiliate} - {self.type})'

class Invoice(models.Model):
    """A model for recording payments from partners to affiliates."""

    partner = models.ForeignKey('Partner', on_delete=models.CASCADE, related_name='invoices_sent')
    affiliate = models.ForeignKey('Affiliate', on_delete=models.CASCADE, related_name='invoices_received')
    campaign = models.ForeignKey('Campaign', on_delete=models.CASCADE, related_name='invoices')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_month = models.DateField()
    payment_status = models.CharField(max_length=25, choices=(('open','Open'), ('not_paid','Not Piad'), ('paid','Paid')))
    payment_method = models.CharField(max_length=25, choices=(('wallet','Wallet'), ('bank_transfer','Bank Transfer'), ('cash','Cash')))
    payment_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of the invoice."""
        return f'Invoice from {self.partner.brand_name} to {self.affiliate.first_name} {self.affiliate.last_name} - {self.amount}'
