from django.db import models
import datetime

# Create your models here.

PSTATUS_CHOICES = (
    ('Employed', 'Employed'),
    ('self-employed', 'self-employed'),
)

TYPE_CHOICES = (
    ('Regular', 'Regular'),
    ('Non-Regular', 'Non-Regular'),
)

STATUS_CHOICES = (
    ('Employed', 'Employed'),
    ('Student', 'Student'),
    ('Professional', 'Professional'),
)

AREA_CHOICES = (
    ('Near_Home', 'Near_Home'),
    ('Near_Campus', 'Near_Campus'),
)

year_dropdown = []
for y in range(1920, datetime.datetime.now().year):
    year_dropdown.append((y, y))


class Residential_colony(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Seva_Residential_colony(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    year_of_birth = models.IntegerField(('year'), choices=year_dropdown,default=datetime.datetime.now().year)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    residential_colony = models.ForeignKey(Residential_colony, on_delete=models.SET_NULL, blank=True, null=True)
    residential_pincode = models.CharField(max_length=6)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='')
    seva_area = models.CharField(max_length=20, choices=AREA_CHOICES, default='',blank=True, null=True)
    seva_residential_colony = models.ForeignKey(Seva_Residential_colony, on_delete=models.SET_NULL, blank=True,null=True)
    seva_residential_pincode = models.CharField(max_length=6, blank=True, null=True)
    type= models.CharField(max_length=20, choices=TYPE_CHOICES, default='')
    degree = models.CharField(max_length=100, blank=True, null=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, blank=True, null=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, blank=True, null=True)

    highest_qualification = models.CharField(max_length=12 , blank=True, null=True)

    complition_year = models.IntegerField(('com_year'), choices=year_dropdown, default=datetime.datetime.now().year,blank=True, null=True)
    pstatus = models.CharField(max_length=20, choices=PSTATUS_CHOICES, default='',blank=True, null=True,)
    nature = models.CharField(max_length=100, blank=True, null=True)



    def __str__(self):
        return f'{self.name}'
