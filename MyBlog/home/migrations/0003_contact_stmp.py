# Generated by Django 3.0.2 on 2020-01-07 11:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Stmp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]