from django.contrib import admin
from django.urls import path, include

from user import views

app_name = 'usr'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('user/',include('user.urls')),
    path('regist/',views.regist,name='redist'),
    path('registerlogic/',views.register_logic,name='rl'),
    path('login/',views.login,name='login'),
    path('loginlogic/',views.login_logic,name='ll'),
    path('index/',views.index,name='index'),
    path('chek_username/',views.check_username,name='cu'),
    path('getcap/',views.get_captcha,name='gc'),
]