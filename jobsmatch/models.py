from django.db import models

class Profile(models.Model):
    summary = models.TextField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True, auto_now_add = False)
    skills = models.TextField()
    certifications = models.TextField()  
    
class Career(models.Model):
    user_id = models.IntegerField()
    company = models.CharField(max_length = 100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    months = models.IntegerField()
    description = models.TextField()
 
#the Job model
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    certificates = models.TextField()
    skills = models.TextField()
    
class Criteria(models.Model):
    certifications = models.TextField()
    skills = models.TextField()
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True)