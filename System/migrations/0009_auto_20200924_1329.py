# Generated by Django 3.0.8 on 2020-09-24 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0008_auto_20200924_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processor',
            options={'ordering': ['-price']},
        ),
    ]
