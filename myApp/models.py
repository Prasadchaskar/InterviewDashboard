from os import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class User(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)


class Candidate(models.Model):
    Available_choices = [
    ('In Office','In Office'),
    ('Work From Home','Work From Home')
]
    Status_choices = [
        ('Showed Up','Showed Up'),
        ('Showed Not','Showed Not')
    ]
    Company_choices =[
        ('Uptricks','Uptricks'),
        ('Kukbit','Kukbit'),
        ('Skillbit','Skillbit'),
        ('Learntricks','Learntricks'),
        ('Challengekatta','Challengekatta'),
        ('Happieloop','Happieloop'),
        ('Internshipmela','Internshipmela')
    ]
    Technology_choices = [
        ('Video Editor Animation','Video Editor Animation'),
        ('Android Development','Android Development'),
        ('Game Development','Game Development'),
        ('Graphics Designing','Graphics Designing'),
        ('Software Testing','Software Testing'),
        ('Manual Testing','Manual Testing'),
        ('Full-stack Development','Full-stack Development'),
        ('Human Resource','Human Resource'),
        ('Digital Marketing','Digital Marketing'),
        ('Wordpress Development','Wordpress Development'),
        ('Web Auditor','Web Auditor'),
        ('Web developer','Web developer'),
        ('Business development executive','Business development executive'),
        ('Machine learning','Machine learning'),
        ('Machine learning','Machine learning'),
        ('AWS','AWS')
    ]
    Post_choices = [ 
        ('Internship','Internship'),
        ('Job','Job')
    ]
    name                    =       models.CharField(max_length=100)
    candidate_contact       =       models.CharField(max_length=10)
    candidate_mail          =       models.EmailField()
    candidate_cv            =       models.FileField(upload_to='media/')
    avialable_for           =       models.CharField(max_length=80,choices=Available_choices)
    company                 =       models.CharField(max_length=50,choices=Company_choices)
    technology              =       models.CharField(max_length=50,choices=Technology_choices)
    post                    =       models.CharField(max_length=50,choices=Post_choices)
    scheduled_date          =       models.DateField(auto_now_add=False)
    scheduled_time          =       models.TimeField(auto_now_add=False)
    scheduled_by            =       models.CharField(max_length=100)
    interviewr_name         =       models.CharField(max_length=100)
    interviewr_mail         =       models.EmailField()
    status                  =       models.CharField(max_length=30,choices=Status_choices,blank=True)
    remark                  =       models.CharField(max_length=200,blank=True)