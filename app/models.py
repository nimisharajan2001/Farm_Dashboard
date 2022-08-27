from ast import Mod
from django.db import models

# Create your models here.
class designation(models.Model):
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.designation

class register(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
        related_name='registerdesignation',null=True,blank=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    team = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    cpassword = models.CharField(max_length=200, null=True, blank=True)
    pin = models.CharField(max_length=200, null=True, blank=True)
    district = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
       return self.name

class plantdetails(models.Model):
    user = models.ForeignKey(register, on_delete=models.DO_NOTHING,null=True, blank=True)
    plant_name = models.CharField(max_length=200)
    flowering_date= models.CharField(max_length=200,null=True, blank=True)
    fruiting_date= models.CharField(max_length=200,null=True, blank=True)
    fertilization_date= models.CharField(max_length=200,null=True, blank=True)
    harvesting_date= models.CharField(max_length=200,null=True, blank=True)
    harvested_data= models.CharField(max_length=200,null=True, blank=True)
    planting_date = models.DateField(max_length=200,null=True, blank=True)
    pest_control_date = models.CharField(max_length=200,null=True, blank=True)
    location = models.CharField(max_length=200,null=True, blank=True)
    number = models.CharField(max_length=200,null=True, blank=True)
    
class farm_weather(models.Model):
    user = models.ForeignKey(register, on_delete=models.DO_NOTHING,null=True, blank=True)
    parameters = models.CharField(max_length=200)
    date = models.DateField(max_length=200)
    morning = models.CharField(max_length=200)
    evening = models.CharField(max_length=200)
    average = models.CharField(max_length=200)

class soil_sample_test(models.Model):
    user = models.ForeignKey(register, on_delete=models.DO_NOTHING,null=True, blank=True)
    tests = models.CharField(max_length=200)
    place = models.CharField(max_length=200,null=True, blank=True)
    date = models.DateField(max_length=200)
    result = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    level = models.CharField(max_length=200)

class fertilizer_applications(models.Model):
    user = models.ForeignKey(register, on_delete=models.DO_NOTHING,null=True, blank=True)
    fertilizer = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=200,null=True, blank=True)
    applied_quantity = models.CharField(max_length=200)
    applied_date = models.DateField(max_length=200)
    place = models.CharField(max_length=200,null=True, blank=True)
    plant_name = models.CharField(max_length=200,null=True, blank=True)
    unit = models.CharField(max_length=200,null=True, blank=True)

class periodic_tests(models.Model):
    user = models.ForeignKey(register, on_delete=models.DO_NOTHING,null=True, blank=True)
    tests = models.CharField(max_length=200)
    place = models.CharField(max_length=200,null=True, blank=True)
    date = models.DateField(max_length=200)
    measurement = models.CharField(max_length=200)

class farm_machineries(models.Model):
    user = models.ForeignKey(register, on_delete=models.DO_NOTHING,null=True, blank=True)
    machine_name = models.CharField(max_length=200)
    machine_id = models.CharField(max_length=200,null=True, blank=True)
    place = models.CharField(max_length=200,null=True, blank=True)
    date = models.DateField(max_length=200,null=True, blank=True)
    number_of_machines = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200)
    total = models.CharField(max_length=200,null=True,blank=True)

class man_power_usage(models.Model):
    user = models.ForeignKey(register, on_delete=models.DO_NOTHING,null=True, blank=True)
    job = models.CharField(max_length=200)
    place = models.CharField(max_length=200,null=True, blank=True)
    date = models.DateField(max_length=200,null=True, blank=True)
    number_of_peoples = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200)
    total = models.CharField(max_length=200,null=True,blank=True)

class farm_expenses(models.Model):
    user = models.ForeignKey(register, on_delete=models.DO_NOTHING,null=True, blank=True)
    expenditure = models.CharField(max_length=200,null=True,blank=True)
    expense = models.CharField(max_length=200,null=True,blank=True)
    type_description = models.CharField(max_length=200,null=True,blank=True)
    item = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    total_cost = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateField(max_length=200,null=True, blank=True)

class farm_revenue(models.Model):
    user = models.ForeignKey(register, on_delete=models.DO_NOTHING,null=True, blank=True)
    revenue_type = models.CharField(max_length=200,null=True,blank=True)
    type_description = models.CharField(max_length=200,null=True,blank=True)
    quantity = models.CharField(max_length=200,null=True,blank=True)
    revenue = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateField(max_length=200,null=True, blank=True)