from django.db import models
from solo.models import SingletonModel
from django.contrib.auth.models import User
# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='upload/')
    def __str__(self):
        return f"{self.name}"
class Slider(models.Model):
    name = models.CharField(max_length=50)
    slider_image = models.ManyToManyField(Image)
    def __str__(self):
        return f"{self.name}"
class HomeSlider(SingletonModel):
    name = models.CharField(max_length=50)
    slider = models.ForeignKey(Slider,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"{self.name}"
class Club(models.Model):
    name = models.CharField(max_length=50)
    club_slider = models.ForeignKey(Slider,on_delete=models.CASCADE,null=True,blank=True)
    activities = models.ManyToManyField(Image)
    reg_fee = models.IntegerField()
    members = models.ManyToManyField(User)
    def __str__(self):
        return f"{self.name}"
    

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    club = models.ForeignKey(Club,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ManyToManyField(Image)
    date = models.DateField()
    time = models.TimeField()
    details = models.URLField()
    def __str__(self):
        return f"{self.event_name}"
    
class Registrations(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    club = models.ManyToManyField(Club)
    amount = models.IntegerField(null=True,blank=True)
    payment_number = models.CharField(max_length=50,null=True,blank=True)
    trx_id = models.CharField(max_length=50,null=True,blank=True)
    CHOICE_OPTION1 = 'Bkash'
    CHOICE_OPTION2 = 'Nagad'
    

    CHOICES = [
        (CHOICE_OPTION1, 'Bkash'),
        (CHOICE_OPTION2, 'Nagad'),
        
    ]
    payment_method =  models.CharField(max_length=20, choices=CHOICES,null=True,blank=True)

    CHOICE_OPTION3 = 'Pending'
    CHOICE_OPTION4 = 'Completed'
    

    CHOICES2 = [
        (CHOICE_OPTION3, 'Pending'),
        (CHOICE_OPTION4, 'Completed'),
        
    ]
    payment_status =  models.CharField(max_length=20, choices=CHOICES2,null=True,blank=True)

    def __str__(self):
        return f"{self.user.username}"