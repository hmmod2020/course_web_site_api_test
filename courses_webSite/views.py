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
from django.contrib.auth import authenticate
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
    fName = request.data['fristName']
    lName = request.data['lastName']
    education = request.data['education']
    email = request.data['email']
    image = request.data['image']
    description = request.data['description']
    user = User.objects.create_user(username=usre_name, password=password)

    if user is not None:
        user.save()
        Wallet(by_user=user, amount=0)

    info_user = userInfo(by_user=user,
                         fName=fName, lName=lName,
                         education=education,
                         email=email, image=image,
                         description=description)
    if info_user:
        info_user.save()
    Token.objects.create(user=user)

    return Response(request.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def create_new_course(request):
    currentUser = request.user.id
    select_categorie_id = request.data["categorie"]
    cate = categorie.objects.get(id=select_categorie_id)
    title = request.data["title"]
    price = request.data['price']
    date = datetime.date.today()
    description = request.data["description"]
    descriptionOfRequerment = request.data["descriptionOfRequerment"]
    afterThisCourse = request.data["afterThisCourse"]
    categorie_in = cate
    new_course = courses(
        title=title,
        by_user_id=currentUser,
        date=date,
        price=price,
        afterThisCourse=afterThisCourse,
        description=description,
        descriptionOfRequerment=descriptionOfRequerment,
        categorie=categorie_in
    )

    new_course.save()
    ser = course_ser(new_course)
    return Response(ser.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_token(request):
    usre_name = request.data['username']
    password = request.data['password']
    user = authenticate(username=usre_name, password=password)
    if user is not None:
        currentUser = User.objects.get(username=user)
        token_ob = Token.objects.get(user_id=currentUser)
        data = {
            "token": token_ob.key
        }
    else:
        data = {
            "details": "user or password is wrong"
        }

    return Response(data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def show_my_make(request):
    currentUser = request.user.id
    myCourse = courses.objects.filter(by_user=currentUser)
    ser = course_ser(myCourse)
    if ser:
        return Response(ser.data)
    else:
        return Response("not have any course")


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def show_my_wallet(request):
    currentUser = request.user.id
    wallet = Wallet.objects.get(by_user=currentUser)
    ser = wallet_ser(wallet)
    if ser:
        data2 = ser.data
    else:
        data2 = {
            "ditails": "you don't have a wallet"
        }
    return Response(data2)


@api_view(['PUT', 'GET'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def buy_course(request,id):
    global data
    currentCourse = courses.objects.get(pk=id)
    currentUser = request.user.id
    my_wallet = Wallet.objects.get(by_user=currentUser)
    currentAmount = my_wallet.amount
    price_course = currentCourse.price
    if currentAmount >= price_course:
        amount_after_buy = currentAmount - price_course
        if request.method == 'GET':
            ser = course_ser(currentCourse)
            return Response(ser.data)

        if request.method == 'PUT':
            transactionType2 = request.data['transactionType']
            data = {
                "id":my_wallet.pk,
                "amount": amount_after_buy,
                "by_user":my_wallet.by_user.id
            }
        ser = wallet_ser(my_wallet,data=data)
        valid_rep=userBoughtCourse.objects.filter(Q(by_user=request.user)&Q(course=currentCourse))
        if valid_rep :
            return Response("you bougt this course")
        if ser.is_valid():
            ser.save()
        else:
            return Response(ser.errors)
        buoted_course = userBoughtCourse(by_user=request.user, course=currentCourse, price=price_course)
        buoted_course.save()
        if buoted_course:
            tend= transaction(by_wallet=my_wallet, amount=price_course,create_at=datetime.date.today(),transactionType=transactionType2)
            tend.save()
            tsre=transaction_ser(tend)

            return Response(tsre.data)
        else:
            return Response("there is wrong")

    else:
        return Response("not have enough amount ")


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def getCourses(request):
    courses_query=courses.objects.all()
    ser =course_ser(courses_query,many=True)

    return Response(ser.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def show_my_bought_cousres(request):
    currentUser = request.user.id
    myCourse = userBoughtCourse.objects.filter(by_user=currentUser)
    ser = course_ser(myCourse)
    if ser:
        return Response(ser.data)
    else:
        return Response("not have any course")

@api_view(['PUT'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def recharge_the_balance(request):
    currentUser = request.user.id
    my_wallet = Wallet.objects.filter(by_user=currentUser)
    amount=request.data['amount']
    sum=amount+my_wallet.amount

    if request.method =='PUT':
        data = {
            "id": my_wallet.pk,
            "amount": sum,
            "by_user": my_wallet.by_user.id
        }
        ser = wallet_ser(my_wallet, data=data)
        if ser.is_valid():
            return Response(ser.data)
        else:
            return Response("an error occurred")



