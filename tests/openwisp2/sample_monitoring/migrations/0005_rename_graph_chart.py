# Generated by Django 3.0.3 on 2020-06-01 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample_monitoring', '0004_alert_settings_contenttype_registration'),
    ]

    operations = [
        migrations.RenameModel(old_name='Graph', new_name='Chart',),
    ]