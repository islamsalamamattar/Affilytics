# Generated by Django 4.1.7 on 2023-08-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0002_campaign_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='customer',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]