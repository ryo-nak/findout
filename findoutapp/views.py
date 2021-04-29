from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from findoutapp.models import FindoutModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      try:
        user = User.objects.create_user(username, '', password)
        return render(request, 'signup.html', {})
      except IntegrityError:
        return render(request, 'signup.html', {'error':'このユーザーは既に登録されています。'})
    return render(request, 'signup.html', {})


def loginfunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('list')
    else:
        return render(request, 'login.html', {'context':'not logged in'})
  return render(request, 'login.html', {})

@login_required
def listfunc(request):
    object_list = FindoutModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):
    objects = get_object_or_404(FindoutModel, pk=pk)
    return render(request, 'detail.html', {'objects': objects})


def goodfunc(request, pk):
    objects = get_object_or_404(FindoutModel, pk=pk)
    objects.good += 1
    objects.save()
    return redirect('list')


#本番環境には耐えられない
#def readfunc(request, pk):
#    object = FindoutModel.objects.get(pk=pk)
#    username = request.user.get_username()
#    if username in object.readtext:
#        return redirect('list')
#    else:
#        object.read += 1
#        object.readtext = object.readtext + ' ' + username
#        object.save()
#        return redirect('list')


class FindoutCreate(CreateView):
    template_name = 'create.html'
    model = FindoutModel
    fields = ('title', 'content', 'author', 'sns_image')
    success_url = reverse_lazy('list')
