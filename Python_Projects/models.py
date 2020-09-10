from django.db import models

# Create your models here.

class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.IntegerField
    instructor_name = models.CharField(max_length=60)
    duration = models.FloatField(max_length=60)

    objects = models.Manager()

class graphicDesign(models.Model):
    description = models.CharField(max_length=100)
    schedule = models.CharField(max_length=60)

class cyberSecurity(models.Model):
    description = models.CharField(max_length=100)
    schedule = models.CharField(max_length=60)

class helpDesk(models.Model):
    description = models.CharField(max_length=100)
    schedule = models.CharField(max_length=60)
