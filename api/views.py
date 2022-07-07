from django.shortcuts import render
from rest_framework.views import APIView, status
from .models import *
from .serializers import *
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import *
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.decorators import *
from .constant import constant
from django.http import HttpResponse
from datetime import *
import secrets


class MedicineAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, disease):
        medicines = Medicine.objects.filter(med_disaese__iexact=disease)
        serializer = MedicineSerializer(medicines, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

class DiseaseNames(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        diseases = []
        new_quest = Medicine.objects.all()
        for i in new_quest:
            if i.med_disaese not in diseases:
                diseases.append(i.med_disaese)
        return Response(diseases, status=200)


class DoctorAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if request.GET:
            doctors = Doctor.objects.all()
            output = output1 = output2 = Doctor.objects.none()
            li = [item for item in request.GET.keys()]
            print(len(li))
            if len(li) == 1:
                for el in li:
                    var_column = "doc_" + el
                    search_type = "__iexact"
                    filter_var = var_column + search_type
                    splitted = request.GET[el].split(',')
                    for i in splitted:
                        print(i)
                        filter_doctors = doctors.filter(**{filter_var: i})
                        output = output | filter_doctors
            elif len(li) == 2:
                el = li[0]
                var_column = "doc_" + el
                search_type = "__iexact"
                filter_var = var_column + search_type
                splitted = request.GET[el].split(',')
                print(splitted)
                for i in splitted:
                    print(i)
                    filter_doctors = doctors.filter(**{filter_var: i})
                    print(filter_doctors)
                    output1 = output1 | filter_doctors
                el = li[1]
                var_column = "doc_" + el
                search_type = "__iexact"
                filter_var = var_column + search_type
                splitted = request.GET[el].split(',')
                print(splitted)
                for i in splitted:
                    print(i)
                    filter_doctorss = output1.filter(**{filter_var: i})
                    print(filter_doctorss)
                    output2 = output2 | filter_doctorss
                output = output1 & output2
            # serialize final queryset
            serializer = DoctorSerializer(output, many=True)
            return Response(serializer.data, status=HTTP_200_OK)

        else:
            doctors = Doctor.objects.all()
            serializer = DoctorSerializer(doctors, many=True)
            return Response(serializer.data, status=HTTP_200_OK)


class DoctorDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        doctor = Doctor.objects.get(id=id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=HTTP_200_OK)


class HospitalAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if request.GET:
            hospitals = Hospital.objects.all()
            output = output1 = output2 = Hospital.objects.none()
            li = [item for item in request.GET.keys()]
            print(len(li))
            if len(li) == 1:
                for el in li:
                    var_column = "h_" + el
                    search_type = "__iexact"
                    filter_var = var_column + search_type
                    splitted = request.GET[el].split(',')
                    for i in splitted:
                        print(i)
                        filter_hospitals = hospitals.filter(**{filter_var: i})
                        output = output | filter_hospitals
            elif len(li) == 2:
                el = li[0]
                var_column = "h_" + el
                search_type = "__iexact"
                filter_var = var_column + search_type
                splitted = request.GET[el].split(',')
                print(splitted)
                for i in splitted:
                    print(i)
                    filter_hospitals = hospitals.filter(**{filter_var: i})
                    output1 = output1 | filter_hospitals
                el = li[1]
                var_column = "h_" + el
                search_type = "__iexact"
                filter_var = var_column + search_type
                splitted = request.GET[el].split(',')
                print(splitted)
                for i in splitted:
                    print(i)
                    filter_hospitalss = output1.filter(**{filter_var: i})
                    output2 = output2 | filter_hospitalss
                output = output1 & output2
            # serialize final queryset
            serializer = HospitalSerializer(output, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            hospitals = Hospital.objects.all()
            serializer = HospitalSerializer(hospitals, many=True)
            return Response(serializer.data, status=HTTP_200_OK)


class HospitalDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        hospital = Hospital.objects.get(id=id)
        serializer = HospitalSerializer(hospital)
        return Response(serializer.data, status=HTTP_200_OK)


class SignUpAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        email = request.data["email"]
        if User.objects.filter(username=username).exists():
            return Response({"Result": "User already exits"})
        user = User.objects.create_user(username, email, password)
        user.save()
        return Response({"Result": "Success"}, status=status.HTTP_201_CREATED)


class LogInAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"Result": "Success"})
        else:
            return Response({"Result": "Username/Password are incorrect"})


class FeedbackAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        feedback = Feedback.objects.create()
        feedback.name = request.data["name"]
        feedback.feed = request.data["feedback"]
        feedback.save()
        return Response({"Result": "Success"}, status=status.HTTP_201_CREATED)


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, context={"request": request})
        return Response(serializer.data, status=HTTP_200_OK)


class PatientQuestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, doc_name):
        questions = Question.objects.filter(user_name=request.user)
        questions = questions.filter(doc_name=doc_name)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        question = Question.objects.create()
        question.user_name = str(request.user)
        question.query = request.data["query"]
        question.tag = request.data["tag"]
        question.doc_name = request.data["doc_name"]
        question.save()
        return Response({"Result": "Success"}, status=200)


class GetConsultedDoctorsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doctors = []
        new_quest = Question.objects.filter(user_name=request.user)
        for i in new_quest:
            if i.doc_name not in doctors:
                doctors.append(i.doc_name)
        consulted_doctors = ConsultDoctor.objects.none()
        for i in doctors:
            doctor = ConsultDoctor.objects.filter(user_name=i)
            consulted_doctors = consulted_doctors | doctor
        serializer = ConsultDoctorSerializer(consulted_doctors, many=True)
        return Response(serializer.data, status=200)


class DoctorQuestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_name):
        questions = Question.objects.filter(doc_name=request.user)
        questions = questions.filter(user_name=user_name)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        question = Question.objects.create()
        question.user_name = str(request.user)
        question.query = request.data["query"]
        question.tag = request.data["tag"]
        question.doc_name = request.data["doc_name"]
        question.save()
        return Response({"Result": "Success"}, status=200)


class PostAnswerAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        question = Question.objects.get(id=int(id))
        question.posted = True
        question.answer = request.data["answer"]
        print(request.data["answer"])
        question.save()
        return Response({"Result": "Success"}, status=200)


class GetAskedPatientsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patients = []
        new_quest = Question.objects.filter(doc_name=request.user)
        for i in new_quest:
            if i.doc_name not in patients:
                patients.append(i.user_name)
        aksed_patients = User.objects.none()
        for i in patients:
            patient = User.objects.filter(username=i)
            aksed_patients = aksed_patients | patient
        serializer = UserSerializer(aksed_patients, many=True)
        return Response(serializer.data, status=200)


class QuestionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        question = Question.objects.get(id=id)
        question.posted = True
        question.answer = request.data["answer"]
        question.save()
        return Response({"Result": "Success"}, status=200)


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_email(request):
    user = request.data["username"]
    if User.objects.filter(username=user).exists():
        email = request.data["email"]
        user_existed = User.objects.get(username=user)
        if (email == user_existed.email):
            token = generate_token()
            reset_token=UserToken(user_name=user,token=token)
            reset_token.save()
            resetlink = ResetLink(link=token)
            resetlink.save()
            import smtplib
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            # Next, log in to the server
            server.login("amlu9421@gmail.com", constant)
            # Send the mail
            # The /n separates the message from the headers

            msg = "Welcome " + user + ",\n"
            msg += "Your reset token is given below\n"+"Use thsi token to reset password.\n"
            msg += "Caution: Please do not share this token \n"
            the_link =token
            the_link+="\n"+"http://192.168.43.50:8000/reset_password/"
            the_link+=token
            # msg +="http://192.168.43.50:8000/redirect_to_pass/"
            msg += the_link
            server.sendmail("amlu9421@gmail.com", email, msg)
            return Response({"Result": "Verified"}, status=200)
        else:
            return Response({"Result": "Not Verified"}, status=200)
    else:
        return Response({"Result": "Username does not exist"}, status=200)


@api_view(['PUT'])
@permission_classes([AllowAny])
def reset_password(request):
    token = request.data.get("token")
    if ResetLink.objects.filter(link=token).exists():
        if UserToken.objects.filter(token=token).exists():
            user = UserToken.objects.get(token=token)
            user_name=user.user_name
            u=User.objects.get(username=user_name)
            u.set_password(request.data["password"])
            u.save()
            reset_link = ResetLink.objects.filter(link=token)
            reset_link.delete()
            user.delete()
            return Response({"Result": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Result": "Fail"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Result": "Expired"}, status=status.HTTP_400_BAD_REQUEST)


def redirect_to_pass(request):
    request.session["expiry"] = True
    request.session.set_expiry(300)
    user = request.GET["user"]
    reset_ur = request.build_absolute_uri
    return render(request, 'reset_password.html', {"user": user, "reset": reset_ur})


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_email_view(request):
    user = request.data["username"]
    if User.objects.filter(username=user).exists():
        email = request.data["email"]
        user_existed = User.objects.get(username=user)
        if (email == user_existed.email):
            """ import smtplib
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            # Next, log in to the server
            server.login("amlu9421@gmail.com", constant)
            # Send the mail
            # The /n separates the message from the headers

            msg = "Welcome "+user+",\n"
            msg += "Click on link below to reset your password\n"
            msg += "Caution: Please do not share this link \n"
            the_link = "http://192.168.43.50:8000/redirect_to_pass/"
            the_link += "?user="+user
            #msg +="http://192.168.43.50:8000/redirect_to_pass/"
            msg += the_link
            resetlink = ResetLink(link=the_link)
            resetlink.save()
            server.sendmail("amlu9421@gmail.com", email, msg) """
            token = generate_token()
            serializer = UserTokenSerializer(token)
            return Response(serializer.data, status=200)
        else:
            return Response({"Result": "Not Verified"}, status=200)
    else:
        return Response({"Result": "Username does not exist"}, status=200)


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password_view(request):
    reset_url = request.data["reset"]
    print(reset_url)
    if ResetLink.objects.filter(link=reset_url).exists():
        user = request.data.get("user")
        print(user)
        if User.objects.filter(username=user).exists():
            user = User.objects.get(username=user)
            user.set_password(request.data["password"])
            user.save()
            reset_link = ResetLink.objects.filter(link=reset_url)
            reset_link.delete()
            return HttpResponse("<center><h1>Your password is changed successfully</h1></center>")
        else:
            return Response({"Result": "User does not exist"})
    else:
        return HttpResponse("<center><h1>The link has expired.</h1></center>")



class ConsultDoctorAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        consult_doctors = ConsultDoctor.objects.all()
        serializer = ConsultDoctorSerializer(consult_doctors, many=True)
        return Response(serializer.data, status=200)


def generate_token():
    token = secrets.token_hex(20)
    return token
