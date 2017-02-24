import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
        
        
        

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
        
        

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