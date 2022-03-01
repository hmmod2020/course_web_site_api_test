from rest_framework import serializers
from .models import *


class user_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=userInfo
        fields='__all__'

class course_ser(serializers.ModelSerializer):
    class Meta:
        model=courses
        fields='__all__'

class categorie_ser(serializers.ModelSerializer):
    class Meta:
        model=categorie
        fields='__all__'

class lessons_ser(serializers.ModelSerializer):
    class Meta:
        model=lessons
        fields='__all__'


class files_ser(serializers.ModelSerializer):
    class Meta:
        model = files
        fields = '__all__'

class userBoughtCourse_ser(serializers.ModelSerializer):
    class Meta:
        model = userBoughtCourse
        fields = '__all__'

class rateCourse_ser(serializers.ModelSerializer):
    class Meta:
        model = rateCourse
        fields = '__all__'

class earnings_ser(serializers.ModelSerializer):
    class Meta:
        model = earnings
        fields = '__all__'

class commentOnCourse_ser(serializers.ModelSerializer):
    class Meta:
        model = commentOnCourse
        fields = '__all__'


class courseUserWatch_ser(serializers.ModelSerializer):
    class Meta:
        model = courseUserWatch
        fields = '__all__'