# Generated by Django 3.0.8 on 2020-09-24 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0003_auto_20200924_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processor',
            old_name='item_model_no',
            new_name='item_model_number',
        ),
    ]
