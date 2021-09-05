from os import name
from django.db import models

# Create your models here.


class Candidate(models.Model):
    Available_choices = [
    ('In Office','In Office'),
    ('Work From Home','Work From Home')
]
    Status_choices = [
        ('Showed Up','Showed Up'),
        ('Showed Not','Showed Not')
    ]
    name                    =       models.CharField(max_length=100)
    candidate_contact       =       models.CharField(max_length=10)
    candidate_mail          =       models.EmailField()
    candidate_cv            =       models.FileField(upload_to='media/')
    avialable_for           =       models.CharField(max_length=30,choices=Available_choices)
    company                 =       models.CharField(max_length=50)
    technology              =       models.CharField(max_length=50)
    post                    =       models.CharField(max_length=30)
    scheduled_date          =       models.DateField(auto_now_add=False)
    scheduled_time          =       models.TimeField(auto_now_add=False)
    scheduled_by            =       models.CharField(max_length=100)
    interviewr_name         =       models.CharField(max_length=100)
    interviewr_mail         =       models.EmailField()
    status                  =       models.CharField(max_length=30,choices=Status_choices)
    remark                  =       models.CharField(max_length=200)