from django.db import models
from django.contrib.auth.models import User
# from djangotoolbox.fields import DictField

# Create your models here.





class Processor(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True , blank=True )
    name = models.TextField(blank=True)
    price = models.FloatField(null=True,blank=True)
    manufacturer = models.TextField(blank=True)
    brand = models.CharField(max_length = 100, null=True,blank=True)
    item_height = models.CharField(max_length = 100 , null=True,blank=True)
    item_width = models.CharField(max_length = 100 , null=True,blank=True)
    product_dimensions = models.CharField(max_length = 100 , null=True,blank=True)
    item_model_number = models.CharField(max_length = 100 , null=True,blank=True)
    processor_brand = models.CharField(max_length = 100 , null=True,blank=True)
    processor_type = models.CharField(max_length = 100 , null=True,blank=True)
    processor_speed = models.CharField(max_length = 100 , null=True,blank=True)
    processor_socket = models.CharField(max_length = 100 , null=True,blank=True)
    processor_count = models.IntegerField(null=True ,blank=True)
    ram_size = models.CharField(max_length = 100 , null=True,blank=True)
    computer_memory_type = models.CharField(max_length = 100 , null=True,blank=True)
    harddrive_size = models.CharField(max_length = 100 , null=True,blank=True)
    hard_drive_interface = models.CharField(max_length = 100 , null=True,blank=True)
    wattage = models.CharField(max_length = 100 , null=True,blank=True)
    hardware_platform = models.CharField(max_length = 100 , null=True,blank=True)
    operating_system = models.CharField(max_length = 100 , null=True,blank=True)
    are_batteries_included = models.CharField(max_length = 100 , null=True,blank=True)
    item_weight = models.CharField(max_length = 100 , null=True,blank=True)

    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    
    class Meta:
        ordering = ['-price']

    

class Motherboard(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True,blank=True)
    name = models.TextField(blank=True)
    price = models.FloatField(null=True,blank=True)
    manufacturer = models.TextField(blank=True)
    brand = models.CharField(max_length = 100, null=True,blank=True)
    item_height = models.CharField(max_length = 100 , null=True,blank=True)
    item_width = models.CharField(max_length = 100 , null=True,blank=True)
    product_dimensions = models.CharField(max_length = 100 , null=True,blank=True)
    item_model_no = models.CharField(max_length = 100 , null=True,blank=True)
    series = models.CharField(max_length=100 , null=True,blank=True)
    computer_memory_type = models.CharField(max_length = 100 , null=True,blank=True)
    batteries = models.CharField(max_length = 100 , null=True,blank=True)
    processor_socket = models.CharField(max_length = 100 , null=True,blank=True)
    graphics_card_interface = models.CharField(max_length = 100 , null=True,blank=True)
    no_of_USB = models.CharField(max_length = 100 , null=True,blank=True)
    are_batteries_included = models.CharField(max_length = 100 , null=True,blank=True)
    item_weight = models.CharField(max_length = 100 , null=True,blank=True)
    wattage = models.CharField(max_length = 100 , null=True,blank=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']



class RAM(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True,blank=True)
    name = models.TextField(blank=True)
    price = models.FloatField(null=True,blank=True)
    manufacturer = models.TextField(blank=True)
    brand = models.CharField(max_length = 100, null=True,blank=True)
    item_height = models.CharField(max_length = 100 , null=True,blank=True)
    item_width = models.CharField(max_length = 100 , null=True,blank=True)
    product_dimensions = models.CharField(max_length = 100 , null=True,blank=True)
    item_model_no = models.CharField(max_length = 100 , null=True,blank=True)
    form_factor = models.CharField(max_length = 100, null=True,blank=True)
    memory_technology = models.CharField(max_length = 100, null=True,blank=True)
    memory_clock_speed = models.CharField(max_length = 100, null=True,blank=True)
    voltage = models.CharField(max_length = 100, null=True,blank=True)
    included_components = models.CharField(max_length = 100, null=True,blank=True)
    computer_memory_type = models.CharField(max_length = 100 , null=True,blank=True)
    batteries = models.CharField(max_length = 100 , null=True,blank=True)
    are_batteries_included = models.CharField(max_length = 100 , null=True,blank=True)
    item_weight = models.CharField(max_length = 100 , null=True,blank=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']

class Graphics_Card(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True,blank=True)
    memory_storage_capacity = models.CharField(max_length = 100 , null=True,blank=True)
    hardware_interface= models.CharField(max_length = 100 , null=True,blank=True)
    graphics_card_interface= models.CharField(max_length = 100 , null=True,blank=True)
    color_screen= models.CharField(max_length = 100 , null=True,blank=True)
    batteries_required = models.CharField(max_length = 100 , null=True,blank=True)
    gsm_frequencies = models.CharField(max_length = 100 , null=True,blank=True)
    are_batteries_included = models.CharField(max_length = 100 , null=True,blank=True)
    has_autofocus= models.CharField(max_length = 100 , null=True,blank=True)
    includes_rechargable_batteries = models.CharField(max_length = 100 , null=True,blank=True)
    programmable_button= models.CharField(max_length = 100 , null=True,blank=True)
    model_year= models.CharField(max_length = 100 , null=True,blank=True)
    name = models.TextField(blank=True)
    price = models.FloatField(null=True,blank=True)
    manufacturer = models.TextField(blank=True)
    brand = models.CharField(max_length = 100, null=True,blank=True)
    item_height = models.CharField(max_length = 100 , null=True,blank=True)
    item_width = models.CharField(max_length = 100 , null=True,blank=True)
    product_dimensions = models.CharField(max_length = 100 , null=True,blank=True)
    item_model_no = models.CharField(max_length = 100 , null=True,blank=True)
    wattage = models.CharField(max_length = 100 , null=True,blank=True)
    item_weight = models.CharField(max_length = 100 , null=True,blank=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']

class Harddisk(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True,blank=True)
    name = models.TextField()
    price = models.FloatField(null=True,blank=True)
    manufacturer = models.TextField()
    brand = models.CharField(max_length = 100, null=True,blank=True)
    item_height = models.CharField(max_length = 100 , null=True,blank=True)
    item_width = models.CharField(max_length = 100 , null=True,blank=True)
    product_dimensions = models.CharField(max_length = 100 , null=True,blank=True)
    item_model_no = models.CharField(max_length = 100 , null=True,blank=True)
    hard_drive = models.CharField(max_length = 100 , null=True,blank=True)
    model_name = models.CharField(max_length = 100 , null=True,blank=True)
    flash_memory_installed_size = models.CharField(max_length = 100 , null=True,blank=True)
    digital_storage_capacity = models.CharField(max_length = 100 , null=True,blank=True)
    hard_drive_size = models.CharField(max_length = 100 , null=True,blank=True)
    hard_disk_rotational_speed = models.CharField(max_length = 100 , null=True,blank=True)
    hardware_platform = models.CharField(max_length = 100 , null=True,blank=True)
    hardware_interface = models.CharField(max_length = 100 , null=True,blank=True)
    compatible_devices = models.CharField(max_length = 100 , null=True,blank=True)
    buffer_size = models.CharField(max_length = 100 , null=True,blank=True)
    mounting_hardware= models.CharField(max_length = 100 , null=True,blank=True)
    data_transfer_rate = models.CharField(max_length = 100 , null=True,blank=True)
    mounting_hardware= models.CharField(max_length = 100 , null=True,blank=True)
    connector_type = models.CharField(max_length = 100 , null=True,blank=True)
    form_factor= models.CharField(max_length = 100 , null=True,blank=True)
    wattage = models.CharField(max_length = 100 , null=True,blank=True)
    item_weight = models.CharField(max_length = 100 , null=True,blank=True)
    batteries = models.CharField(max_length = 100 , null=True,blank=True)
    are_batteries_included = models.CharField(max_length = 100 , null=True,blank=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']
    

class Power_Supply_Unit(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True)
    name = models.TextField()
    price = models.FloatField(null=True)
    manufacturer = models.TextField()
    brand = models.CharField(max_length = 100, null=True)
    item_height = models.CharField(max_length = 100 , null=True)
    item_width = models.CharField(max_length = 100 , null=True)
    product_dimensions = models.CharField(max_length = 100 , null=True)
    item_model_no = models.CharField(max_length = 100 , null=True)
    wattage = models.CharField(max_length = 100 , null=True)
    item_weight = models.CharField(max_length = 100 , null=True)
    batteries = models.CharField(max_length = 100 , null=True)
    are_batteries_included = models.CharField(max_length = 100 , null=True)
    processor_count = models.CharField(max_length=100, null=True)
    voltage = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']

class Liquid_Cooling_System(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True)
    name = models.TextField()
    price = models.FloatField(null=True)
    manufacturer = models.TextField()
    brand = models.CharField(max_length = 100, null=True)
    item_height = models.CharField(max_length = 100 , null=True)
    item_width = models.CharField(max_length = 100 , null=True)
    product_dimensions = models.CharField(max_length = 100 , null=True)
    item_model_no = models.CharField(max_length = 100 , null=True)
    wattage = models.CharField(max_length = 100 , null=True)
    item_weight = models.CharField(max_length = 100 , null=True)
    batteries = models.CharField(max_length = 100 , null=True)
    are_batteries_included = models.CharField(max_length = 100 , null=True)
    processor_count = models.CharField(max_length=100, null=True)
    voltage = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']



class Monitor(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True)
    name = models.TextField()
    price = models.FloatField(null=True)
    manufacturer = models.TextField()
    brand = models.CharField(max_length = 100, null=True)
    product_dimensions = models.CharField(max_length = 100 , null=True)
    item_model_no = models.CharField(max_length = 100 , null=True)
    hardware_interface=  models.CharField(max_length = 100 , null=True)
    response_time =  models.CharField(max_length = 100 , null=True)
    resolution= models.CharField(max_length = 100 , null=True)
    special_features= models.CharField(max_length = 100 , null=True)
    mounting_hardware= models.CharField(max_length = 100 , null=True)
    display_technology= models.CharField(max_length = 100 , null=True)
    standing_screen_display_size= models.CharField(max_length = 100 , null=True)
    display_type= models.CharField(max_length = 100 , null=True)
    image_brightness= models.CharField(max_length = 100 , null=True)
    batteries_required= models.CharField(max_length = 100 , null=True)
    refresh_rate= models.CharField(max_length = 100 , null=True)
    connector_type= models.CharField(max_length = 100 , null=True)
    mounting_type= models.CharField(max_length = 100 , null=True)
    item_weight= models.CharField(max_length = 100 , null=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']


    

class Case(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True)
    name = models.TextField()
    price = models.FloatField(null=True)
    manufacturer = models.TextField()
    brand = models.CharField(max_length = 100, null=True)
    product_dimensions = models.CharField(max_length = 100 , null=True)
    item_model_no = models.CharField(max_length = 100 , null=True)
    item_weight = models.CharField(max_length = 100 , null=True)
    batteries = models.CharField(max_length = 100 , null=True)
    are_batteries_included = models.CharField(max_length = 100 , null=True)
    material = models.CharField(max_length=100,null=True)
    usb_ports = models.CharField(max_length=100, null=True)
    mounting_hardware = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']

    


class Keyboard(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True)
    name = models.TextField()
    price = models.FloatField(null=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']


class Mouse(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True)
    name = models.TextField()
    price = models.FloatField(null=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']



class OS(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True)
    name = models.TextField()
    price = models.FloatField(null=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']



class Speaker(models.Model):
    img = models.URLField(null=True , blank= True)
    url = models.URLField(null=True)
    name = models.TextField()
    price = models.FloatField(null=True)
    def __str__(self):
        return str(self.name) + ' , price :' + str(self.price)
    class Meta:
        ordering = ['-price']

class Build(models.Model):
    user  = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    Processor = models.ForeignKey(Processor , on_delete=models.CASCADE , null=True)
    Motherboard = models.ForeignKey(Motherboard , on_delete=models.CASCADE , null=True)
    Ram = models.ForeignKey(RAM , on_delete=models.CASCADE , null=True)
    Graphics_Card = models.ForeignKey(Graphics_Card , on_delete=models.CASCADE , null=True)
    Power_Supply_Unit = models.ForeignKey(Power_Supply_Unit , on_delete=models.CASCADE , null=True)
    Case = models.ForeignKey(Case, on_delete=models.CASCADE , null=True)
    Monitor = models.ForeignKey(Monitor , on_delete=models.CASCADE , null=True)
    Liquid_Cooling_System = models.ForeignKey(Liquid_Cooling_System , on_delete=models.CASCADE , null=True)
    Keyboard = models.ForeignKey(Keyboard , on_delete=models.CASCADE , null=True)
    Mouse = models.ForeignKey(Mouse , on_delete=models.CASCADE , null=True)
    Speaker = models.ForeignKey(Speaker , on_delete=models.CASCADE , null=True)
    Harddisk = models.ForeignKey(Harddisk , on_delete=models.CASCADE , null=True)
    total_price = models.IntegerField(null=True)



class Favourites(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    Build = models.ForeignKey(Build , on_delete=models.CASCADE , null=True)

class Referrals(models.Model):
    From = models.CharField(max_length=20 , null=True)
    To = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    Build = models.ForeignKey(Build , on_delete=models.CASCADE , null=True)










