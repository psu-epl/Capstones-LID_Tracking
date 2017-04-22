import datetime,uuid
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.

#***********************************************************************************************************************
class Profile(models.Model):
    sex_choices = ( #Human Rights Campaign suggested list
        ('NS','Rather not say'),
        ('ML','Male'),
        ('FL','Female'),
        ('NB','Non-Binay'),
        ('TS','Transgender'),
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,11}$', message="Please use the format 9999999999. Max 10 numbers.")

    class Meta:
        ordering = [ #attr1,
                     #attr2,
                     #attrn,
        ]

    user_pkey       = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rfid            = models.BigIntegerField(blank=False, unique=True)
    phone_number    = models.CharField(max_length=11, validators=[phone_regex], blank=False)
    sex             = models.CharField(max_length=64, choices=sex_choices, default='NS', blank=False)
    current_waiver  = models.BooleanField(default=False)
    ec_first_name   = models.CharField(max_length=64, blank=True)
    ec_last_name    = models.CharField(max_length=64, blank=True)
    ec_phone_number = models.CharField(max_length=11, validators=[phone_regex], blank=True)
    ec_relation     = models.CharField(max_length=64, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()


#***********************************************************************************************************************
class ModuleList(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smid = models.BigIntegerField(blank=False, unique=True)
    name = models.CharField(max_length=64, blank=False)

#***********************************************************************************************************************
class AuthUser(models.Model):
    #Primary Key Generated
    user_pkey = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=False)
    smid_pkey = models.ForeignKey(ModuleList, on_delete=models.CASCADE, primary_key=False)

#***********************************************************************************************************************
class UsageLog(models.Model):
    #Primary Key generated
    user_pkey = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=False)
    smid_pkey = models.ForeignKey(ModuleList, on_delete=models.CASCADE, primary_key=False)
    TimeIn    = models.DateTimeField(auto_now_add=True)
    TimeOut   = models.DateTimeField(editable=True)

#***********************************************************************************************************************
class SpecialUser(models.Model):
    user_pkey  = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_manager = models.BooleanField(default=False)
    is_admin   = models.BooleanField(default=False)
