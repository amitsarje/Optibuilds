# Generated by Django 3.0.8 on 2020-09-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0004_auto_20200924_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processor',
            name='are_batteries_included',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='brand',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='computer_memory_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='hard_drive_interface',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='harddrive_size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='hardware_platform',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='item_height',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='item_model_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='item_weight',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='item_width',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='manufacturer',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='operating_system',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='processor_brand',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='processor_count',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='processor_socket',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='processor_speed',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='processor_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='product_dimensions',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='ram_size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='wattage',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
