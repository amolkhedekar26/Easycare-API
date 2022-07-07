from rest_framework import serializers
from django.contrib.auth.models import *
from api.models import *

class MedicineSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    med_name = serializers.CharField(required=True)
    med_brand = serializers.CharField(required=True)
    med_disaese = serializers.CharField(required=True)
    med_dose = serializers.CharField(required=True)
    is_syrup = serializers.BooleanField(default=False)


class HospitalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    h_name = serializers.CharField(required=True)
    h_address = serializers.CharField(required=True)
    h_contact = serializers.IntegerField(required=True)
    h_speciality =serializers.CharField(required=True)
    h_location = serializers.CharField(required=True)
    h_rating = serializers.CharField(required=True)
    h_noofdoctors = serializers.IntegerField(required=True)
    h_time = serializers.CharField(required=True)

class DoctorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    doc_name = serializers.CharField(required=True)
    doc_address = serializers.CharField(required=True)
    doc_mobile = serializers.IntegerField(required=True)
    doc_speciality = serializers.CharField(required=True)
    doc_experience = serializers.CharField(required=True)
    doc_degree = serializers.CharField(required=True)
    doc_location = serializers.CharField(required=True)
    is_male = serializers.BooleanField(default=False)

class FeedbackSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name =serializers.CharField(required=True)
    feed = serializers.CharField(required=True)

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False)
    first_name=serializers.CharField(required=False)
    last_name=serializers.CharField(required=False)
    #email = serializers.CharField(required=False)

class ProfileSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only=True)
    is_doctor = serializers.BooleanField(default=False)
    tag=serializers.CharField()
    #profile_picture = serializers.ImageField(default=None,required=False,allow_null=True)
    photo_url = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    
    def get_photo_url(self,profile):
        request = self.context.get('request')
        photo_url = profile.profile_picture.url
        return request.build_absolute_uri(photo_url)

class QuestionSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    user_name = serializers.CharField(required=True)
    query = serializers.CharField(required=True)
    doc_name = serializers.CharField(required=True)
    tag =serializers.CharField(required=False)
    answer =serializers.CharField(required=False)
    posted =serializers.BooleanField(default=False)


class ConsultDoctorSerializer(serializers.Serializer):
    user_name = serializers.CharField(required=True)
    #password = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    #email =serializers.CharField(required=False)
    speciality=serializers.CharField(required=False)
    experience=serializers.CharField(required=False)

class UserTokenSerializer(serializers.Serializer):
    user_name=serializers.CharField(required=True)
    token=serializers.CharField(required=True)