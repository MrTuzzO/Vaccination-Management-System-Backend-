# Generated by Django 5.1.4 on 2024-12-14 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0006_vaccinecampaign_dose_interval_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccinecampaign',
            name='schedule',
        ),
    ]
