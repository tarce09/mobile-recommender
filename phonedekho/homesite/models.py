from django.db import models
from django.db.models import CharField

# Create your models here.
class display(models.Model):
	id = models.AutoField(primary_key=True)
	Screen_size=models.CharField(max_length=50)
	Resolution=models.CharField(max_length=50)
	
class battery(models.Model):
	id = models.AutoField(primary_key=True)
	Capacity = models.CharField(max_length=50)
	
class processor(models.Model):
	id = models.AutoField(primary_key=True)
	OS = models.CharField(max_length=50)
	freq = models.CharField(max_length=50)
	
class camera(models.Model):
	id = models.AutoField(primary_key=True)
	Primary_cam = models.CharField(max_length=50)
	Secondary_cam = models.CharField(max_length=50)
	
class RAM(models.Model):
	id = models.AutoField(primary_key=True)
	ram = models.CharField(max_length=50)
	
class mobile1(models.Model):
	id = models.AutoField(primary_key=True)
	Brand = models.CharField(max_length=50)
	ProductName = models.CharField(max_length=100)
	display = models.ForeignKey(display, on_delete=models.RESTRICT)
	camera = models.ForeignKey(camera, on_delete=models.RESTRICT)
	ram = models.ForeignKey(RAM, on_delete=models.RESTRICT)
	processor = models.ForeignKey(processor, on_delete=models.RESTRICT)
	battery = models.ForeignKey(battery, on_delete=models.RESTRICT)
	big_img0 = models.CharField(max_length=500)
	big_img1 = models.CharField(max_length=500)
	big_img2 = models.CharField(max_length=500)
	big_img3 = models.CharField(max_length=500)
	big_img4 = models.CharField(max_length=500)
	big_img5 = models.CharField(max_length=500)
	big_img6 = models.CharField(max_length=500)
	img = models.CharField(max_length=1000)
	storage_info = models.CharField(max_length=500)
	display_info = models.CharField(max_length=500)
	cam_info = models.CharField(max_length=500)
	battery_info = models.CharField(max_length=500)
	processor_info = models.CharField(max_length=500)
	display_type = models.CharField(max_length=500)
	link = models.CharField(max_length=500)
	Product_price = models.CharField(max_length=15)
	Product_rating = models.CharField(max_length=5)
	about_phone = models.CharField(max_length=1000)
