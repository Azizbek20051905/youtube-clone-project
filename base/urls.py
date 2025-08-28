from django.urls import path
from .views import HomePage, loginPage, registerPage, logoutPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutPage, name='logaout'),
]

