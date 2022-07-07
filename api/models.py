from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Medicine(models.Model):
    med_name = models.CharField(max_length=120)
    med_disaese = models.CharField(max_length=120)
    med_brand = models.CharField(max_length=120)
    med_dose = models.CharField(max_length=120)
    is_syrup = models.BooleanField(default=False)

    def __str__(self):
        return self.med_name + ":" + self.med_disaese


class Doctor(models.Model):
    doc_name = models.CharField(max_length=120)
    doc_address = models.CharField(max_length=120)
    doc_mobile = models.BigIntegerField()
    doc_speciality = models.CharField(max_length=120)
    doc_experience = models.CharField(max_length=120)
    doc_degree = models.CharField(max_length=120)
    doc_location = models.CharField(max_length=120)
    is_male = models.BooleanField(default=False)

    def __str__(self):
        return self.doc_name + " - " + self.doc_speciality + " : " + self.doc_location


class Hospital(models.Model):
    h_name = models.CharField(max_length=120)
    h_address = models.CharField(max_length=120)
    h_contact = models.BigIntegerField()
    h_speciality = models.CharField(max_length=120)
    h_location = models.CharField(max_length=120)
    h_rating = models.CharField(max_length=120)
    h_noofdoctors = models.IntegerField()
    h_time = models.CharField(max_length=120)

    def __str__(self):
        return self.h_name + " : "+self.h_location + " - "+self.h_speciality



class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    is_doctor = models.BooleanField(default=False)
    tag = models.CharField(max_length=150, null=True, default=None)
    profile_picture = models.ImageField(upload_to='profiles_pictures/',default="profiles_pictures/user.png",blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Question(models.Model):
    user_name = models.CharField(max_length=120)
    query = models.CharField(max_length=200)
    doc_name = models.CharField(max_length=200, null=True, default=None)
    tag = models.CharField(max_length=120)
    answer = models.CharField(max_length=250, null=True, default=None)
    posted = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name + " : "+self.query+"-"+self.tag+"-->"+self.doc_name


class Feedback(models.Model):
    name = models.CharField(max_length=120)
    feed = models.CharField(max_length=150)

    def __str__(self):
        return self.name + " : "+self.feed



class ConsultDoctor(models.Model):
    user_name = models.CharField(max_length=120)
    password = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    speciality=models.CharField(max_length=200,blank=True)
    experience=models.CharField(blank=True,max_length=5)
    def __str__(self):
        return self.user_name+" : "+self.password


@receiver(post_save, sender=ConsultDoctor)
def create_user(sender, instance, created, **kwargs):
    if created:
        User.objects.create(username=instance.user_name,
                            first_name=instance.first_name, last_name=instance.last_name, email=instance.email)
        user=User.objects.get(username=instance.user_name)
        user.set_password(instance.password)
        user.save()
        profile=Profile.objects.get(user=user)
        profile.is_doctor=True
        profile.tag=instance.speciality
        profile.save()
class ResetLink(models.Model):
    link=models.CharField(max_length=300)
    
class UserToken(models.Model):
    user_name=models.CharField(max_length=200)
    token=models.CharField(max_length=200)