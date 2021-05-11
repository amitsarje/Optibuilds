# Generated by Django 3.0.8 on 2020-09-24 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0005_auto_20200924_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='are_batteries_included',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='batteries',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='item_model_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='item_weight',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='product_dimensions',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='are_batteries_included',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='batteries_required',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='color_screen',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='graphics_card_interface',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='gsm_frequencies',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='hardware_interface',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='has_autofocus',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='includes_rechargable_batteries',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='item_height',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='item_model_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='item_weight',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='item_width',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='memory_storage_capacity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='model_year',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='product_dimensions',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='programmable_button',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='graphics_card',
            name='wattage',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='are_batteries_included',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='batteries',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='buffer_size',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='compatible_devices',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='connector_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='data_transfer_rate',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='digital_storage_capacity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='flash_memory_installed_size',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='form_factor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='hard_disk_rotational_speed',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='hard_drive',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='hard_drive_size',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='hardware_interface',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='hardware_platform',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='item_height',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='item_model_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='item_weight',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='item_width',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='model_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='mounting_hardware',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='product_dimensions',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='harddisk',
            name='wattage',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='liquid_cooling_system',
            name='are_batteries_included',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='liquid_cooling_system',
            name='batteries',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='liquid_cooling_system',
            name='item_height',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='liquid_cooling_system',
            name='item_model_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='liquid_cooling_system',
            name='item_weight',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='liquid_cooling_system',
            name='item_width',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='liquid_cooling_system',
            name='product_dimensions',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='liquid_cooling_system',
            name='wattage',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='batteries_required',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='connector_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='display_technology',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='display_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='hardware_interface',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='image_brightness',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='item_model_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='item_weight',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='mounting_hardware',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='mounting_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='product_dimensions',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='refresh_rate',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='resolution',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='response_time',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='special_features',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='standing_screen_display_size',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='are_batteries_included',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='batteries',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='computer_memory_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='graphics_card_interface',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='item_height',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='item_model_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='item_weight',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='item_width',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='no_of_USB',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='processor_socket',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='product_dimensions',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='series',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='wattage',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='power_supply_unit',
            name='are_batteries_included',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='power_supply_unit',
            name='batteries',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='power_supply_unit',
            name='item_height',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='power_supply_unit',
            name='item_model_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='power_supply_unit',
            name='item_weight',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='power_supply_unit',
            name='item_width',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='power_supply_unit',
            name='product_dimensions',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='power_supply_unit',
            name='wattage',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='are_batteries_included',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='computer_memory_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='hard_drive_interface',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='harddrive_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='hardware_platform',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='item_height',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='item_model_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='item_weight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='item_width',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='operating_system',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='processor_brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='processor_socket',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='processor_speed',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='processor_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='product_dimensions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='ram_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='wattage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='are_batteries_included',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='batteries',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='computer_memory_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='item_height',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='item_model_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='item_weight',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='item_width',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='product_dimensions',
            field=models.CharField(max_length=100, null=True),
        ),
    ]