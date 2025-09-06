from django.urls import path
from .views import HomePage, loginPage, registerPage, logoutPage, CreateChannelView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('create/channel/', CreateChannelView.as_view(), name='create-channel'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutPage, name='logaout'),
]

