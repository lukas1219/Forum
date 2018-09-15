from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import UserProfile


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    userprofile = user.user
    return render(request, 'accounts/user_detail.html', {'userprofile': userprofile})
