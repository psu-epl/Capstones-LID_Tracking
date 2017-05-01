import datetime

from django.db import models
from django.utils import timezone
#Commenting this section out for now, but am leaving it here just in case things go sideways
#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#    def __str__(self):
#        return self.question_text
#    def was_published_recently(self):
#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#        
#        
#        
#        
#
#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
#    def __str__(self):
#        return self.choice_text
#        
        

# This is a class of users to store their personal info
# When a new user is created the system automatically gives them an "id" number
#which is the primary key for referenceing them
#added 2.22.17
class User(models.Model):
    rfid          = models.BigIntegerField()
    first_name    = models.CharField(max_length=100)
    last_name     = models.CharField(max_length=100)
    phone_number  = models.BigIntegerField()
    email         = models.EmailField(max_length=100)
    current_waiver= models.BooleanField()
    ec_first_name = models.CharField(max_length=100)
    ec_last_name  = models.CharField(max_length=100)
    ec_phone_number = models.BigIntegerField()
    username        = models.CharField(max_length=100, unique=True, default='abcd')
    password        = models.CharField(max_length=100, default = '222')
    MALE='Male' ; FEMALE='Female'; NOTIDENTIFY='Not Identified'
    gender_choices= ((MALE,'Male'),(FEMALE,'Female'),(NOTIDENTIFY,'NotIdentify'))
    gender = models.CharField(max_length = 100, choices =gender_choices, default = NOTIDENTIFY)
    def __str__(self):
        return self.first_name

# This is  a table for the tools. Each tool will have a Station Module ID (smid) 
#associated with it for records.
#added 2.23.17
class Tool(models.Model):
    name = models.CharField(max_length=100)
    smid = models.BigIntegerField()
    def __str__(self):
        return self.name
#This is a class of users that can use this tool. This user will be created by referencing
#an already existing User.
#added 2.23.17         
class Tool_User(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    user_id = models.BigIntegerField()          #id of the user
    #this is for matching user to tool...
    def __str__(self):
        c = User.objects.get(id=self.user_id)
        return c.first_name

#Create a table of people considered managers.
#This should just contain a list of RFIDs
class Manager(models.Model):
    rfid = models.BigIntegerField()
    
    def __str__(self):
        return self.rfid
        



#create a table of people considered admin
#This should just contain a list of RFIDs

class Admin(models.Model):
    rfid = models.BigIntegerField()
    
    def __str__(self):
        return self.rfid

#COMMENTED THIS OUT FOR CHANGES. LEAVING IN FOR NOW IN CASE THINGS GO SIDEWAYS.

#create a table of punch ins 
#this contains a user, a station module id, and a timestamp
#class PunchIn(models.Model):
#    rfid = models.BigIntegerField()
#    smid = models.BigIntegerField()
#    time = models.DateTimeField('punch in time')
#
#    def __str__(self):
#        return self.time  #THIS NEEDS TO BE CHANGED LATER!!!!!!!!!!!!
##create a table of punch outs
##this contains just tool and punch outs.
#class PunchOut(models.Model):
#    smid = models.BigIntegerField()
#    time = models.DateTimeField('punch out time')
#
#    def __str__(self):
#        return self.time   #THIS NEEDS TO BE CHANGED LATER!!!!!!!!!!!!
        
class Punches(models.Model):
    tool = models.ForeignKey(Tool , null = True)
    time_in = models.DateTimeField('punch in time')
    time_out = models.DateTimeField('punch out time', blank=True)
    rfid = rfid = models.BigIntegerField()