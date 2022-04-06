"""settings_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path
from courses_webSite import views as vs
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signUp/',vs.create_new_user,name='singUp'),
    path('api-token-auth/', views.obtain_auth_token),
    path('createCourse/',vs.create_new_course,name='createCourse'),
    path('showMyCousre',vs.show_my_make),
    path('showToken/',vs.get_token,name='tok'),
    path('user_wallet/',vs.show_my_wallet,name='wallet'),
    path('buy_course/<int:id>/',vs.buy_course,name='wallet'),
    path('course/',vs.getCourses,name="Course"),
    path('course/my_cousrses/',vs.show_my_bought_cousres,'Courses2'),
    path('user_wallet/add_amount/',vs.recharge_the_balance,'add_amount'),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
