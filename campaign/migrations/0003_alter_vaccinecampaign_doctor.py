# Generated by Django 5.1.4 on 2024-12-13 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_doctor_patient'),
        ('campaign', '0002_remove_vaccinecampaign_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccinecampaign',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_campaigns', to='accounts.doctor'),
        ),
    ]
