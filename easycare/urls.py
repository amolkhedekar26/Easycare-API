"""easycare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('medicines/<disease>/', MedicineAPIView.as_view()),
    path('get_disease_names/',DiseaseNames.as_view()),

    path('doctors/', DoctorAPIView.as_view()),
    path('doctors/<id>', DoctorDetailAPIView.as_view()),

    path('hospitals/', HospitalAPIView.as_view()),
    path('hospitals/<id>', HospitalDetailAPIView.as_view()),

    path('signup/', SignUpAPIView.as_view()),
    path('login/', LogInAPIView.as_view()),

    path('feedbacks/', FeedbackAPIView.as_view()),

    path('profile/', ProfileAPIView.as_view()),

    path('consult_doctors/', ConsultDoctorAPIView.as_view()),
    path('patient_questions/<doc_name>', PatientQuestionAPIView.as_view()),
    path('get_consulted_doctors/', GetConsultedDoctorsAPIView.as_view()),
    path('patient_questions/', PatientQuestionAPIView.as_view()),

    path('doctor_questions/<user_name>', DoctorQuestionAPIView.as_view()),
    path('get_asked_patients/', GetAskedPatientsAPIView.as_view()),
    path('doc_questions/<id>', PostAnswerAPIView.as_view()),

    path('questions/<id>', QuestionDetailAPIView.as_view()),

    path('obtain_auth_token/', obtain_auth_token),

    path('verify_email/', verify_email),
    path('reset_password/', reset_password),
    path('verify_email_view/', verify_email_view),
    path('redirect_to_pass/', redirect_to_pass),
    path('reset_password_view/', reset_password_view),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
