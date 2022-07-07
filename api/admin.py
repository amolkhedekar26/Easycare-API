from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Doctor)
admin.site.register(models.Medicine)
admin.site.register(models.Hospital)
admin.site.register(models.Profile)
admin.site.register(models.Question)
admin.site.register(models.Feedback)
admin.site.register(models.ConsultDoctor)
admin.site.register(models.ResetLink)
admin.site.register(models.UserToken)