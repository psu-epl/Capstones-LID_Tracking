#from django.db import models <-- Auto-generated, but listed below.

# Create your models here.
import datetime, uuid, re
from .managers import AumUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


#***********************************************************************************************************************
class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        app_label = 'aumwi'
        db_table  = 'user'
        ordering  = [ #attr1,
                      #attr2,
                      #atrrn,
        ]

    objects = AumUserManager()

    sex_choices = ( #Human Rights Campaign suggested list
        ('NS','Rather not say'),
        ('ML','Male'),
        ('FL','Female'),
        ('NB','Non-Binary'),
        ('TS','Transgender'),
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,11}$', message="Please use the format 9999999999. Max 10 numbers.")

    id              = models.UUIDField(_('unique user id'), primary_key=True, default=uuid.uuid4, editable=False)
    username        = models.CharField(_('username'), max_length=96, unique=True,
                                       help_text=_('Required. 64 Characters or fewer. Letters, numbers, and @/./+/-/_ characters'),
                                       validators=[RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username'), 'invalid')])
    full_name       = models.CharField(_('full name'), max_length=128)
    short_name      = models.CharField(_('short name'), max_length=32, blank=True)
    email           = models.CharField(_('email address'), max_length=256, unique=True)
    rfid            = models.BigIntegerField(_('RFID'), unique=True)
    phone_number    = models.CharField(_('phone number'), max_length=11, validators=[phone_regex], blank=True)
    sex             = models.CharField(_('sex'), max_length=64, choices=sex_choices, default='NS')
    current_waiver  = models.BooleanField(_('signed waiver'), default=False,
                                          help_text=_('Designates if a user has a current and signed waiver'))
    ec_name         = models.CharField(_('emergency contact'), max_length=128, blank=True)
    ec_phone_number = models.CharField(_('ec phone number'), max_length=11, validators=[phone_regex], blank=True)
    ec_relation     = models.CharField(_('ec relations'), max_length=64, blank=True)
    is_staff        = models.BooleanField(_('staff status'), default=False,
                                          help_text=_('Designates whether the user can log into this admin site'))
    is_active       = models.BooleanField(_('active user'), default=True,
                                          help_text=_('Deactivate a user instead of deleting.'))
    is_manager      = models.BooleanField(_('is manager'), default=False,
                                          help_text=_('This sets a users Manager status.'))
    is_admin        = models.BooleanField(_('is admin'), default=False,
                                          help_text=_('This sets a users Admin status.'))
    date_joined     = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email','rfid']

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.short_name

    def get_phone_number(self):
        return self.phone_number

    def get_current_waiver(self):
        return self.current_waiver

    def get_is_manager(self):
        return self.is_manager

    def get_is_admin(self):
        return self.is_admin

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.full_name
#***********************************************************************************************************************
class ModuleList(models.Model):
    id   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smid = models.BigIntegerField(blank=False, unique=True)
    name = models.CharField(max_length=64, blank=False)

    def get_id(self):
        return self.id

    def get_smid(self):
        return self.smid

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

#***********************************************************************************************************************
class AuthUser(models.Model):
    #Primary Key Generated
    user_id = models.UUIDField(primary_key=False, editable=False)
    smid_id = models.UUIDField(primary_key=False, editable=False)

    def get_user_id(self):
        return self.user_id

    def get_smid_id(self):
        return self.smid_id

    def __str__(self):
        user = User.objects.get(id=self.user_id)
        user_name = user.full_name
        tool = ModuleList.objects.get(id=self.smid_id)
        tool_name = tool.name
        return "%s --- %s" % (user,tool)

#***********************************************************************************************************************
class UsageLog(models.Model):
    #Primary Key generated
    user_id   = models.UUIDField(primary_key=False, editable=False)
    smid_id   = models.UUIDField(primary_key=False, editable=False)
    TimeIn    = models.DateTimeField(auto_now_add=True, editable=False)
    TimeOut   = models.DateTimeField(blank=True, editable=True)

    def get_user_id(self):
        return self.user_id

    def get_smid_id(self):
        return self.smid_id

    def get_time_in(self):
        return self.TimeIn

    def get_time_out(self):
        return self.TimeOut

    def set_time_out(self,TimeOut):
        self.TimeOut = TimeOut
        return self.TimeOut


#***********************************************************************************************************************
