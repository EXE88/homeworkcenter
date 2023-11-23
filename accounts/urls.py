from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register_page'),
    path('login/',views.UserLoginView.as_view(),name='login_page'),
    path('logout/',views.UserLogoutView.as_view(),name='logout_page'),
    path('verify/',views.VerifyEmailView.as_view(),name='verifyemail_page')
]
