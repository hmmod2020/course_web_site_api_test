from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.contrib import auth
from django.http import *
from rest_framework.decorators import *
from rest_framework.permissions import *
from .models import *
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework.response import Response
from rest_framework.authentication import *
from django.db.models import Q
import datetime
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def create_new_user(request):
    usre_name = request.data['username']
    password = request.data['password']
    fName=request.data['fristName']
    lName=request.data['lastName']
    education=request.data['education']
    email=request.data['email']
    image=request.data['image']
    description=request.data['description']
    user = User.objects.create_user(username=usre_name, password=password)
    user.save()
    info_user=userInfo(by_user=user,
                       fName=fName,lName=lName,
                       education=education,
                       email=email,image=image,
                       description=description)
    info_user.save()
    Token.objects.create(user=user)

    return Response(request.data)




@api_view(['POST'])
@authentication_classes([TokenAuthentication,BaseAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
def create_new_course(request):
    currentUser=request.user.id
    select_categorie_id=request.data["categorie"]
    cate=categorie.objects.get(id=select_categorie_id)
    title=request.data["title"]
    date=datetime.date.today()
    description=request.data["description"]
    descriptionOfRequerment = request.data["descriptionOfRequerment"]
    afterThisCourse = request.data["afterThisCourse"]
    categorie_in = cate
    new_course = courses(
        title=title,
        by_user_id=currentUser,
        date=date,
        afterThisCourse=afterThisCourse,
        description=description,
        descriptionOfRequerment=descriptionOfRequerment,
        categorie=categorie_in
    )
    new_course.save()
    ser = course_ser(new_course)
    return Response(ser.data)












