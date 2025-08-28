from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import mixins, authenticate, login, logout
from .models import CustomUser, Video, Channel, PersonSaved, Playlist, Comment

# Create your views here.
class HomePage(mixins.LoginRequiredMixin, generic.ListView):
    model = Video
    template_name = "index.html"
    context_object_name = 'videos'
    login_url = '/login'


def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'error': 'Username yoki parol xato'})
        else:
            return render(request, 'login.html', {'error': 'Please enter both username and password'})
    
    return render(request, 'login.html')

def registerPage(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        new_password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if new_password == confirm_password:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=new_password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            user = authenticate(request, username=username, password=new_password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'register.html', {'error': 'Username yoki parol xato'})
        else:
            return render(request, 'register.html', {'error': 'Parollar mos emas'})
    
    return render(request, 'register.html')


def logoutPage(request):
    logout(request)
    return redirect('/login')