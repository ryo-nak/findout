from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, FindoutCreate


urlpatterns = [
    path('signup/', signupfunc, name='sinup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('create/', FindoutCreate.as_view(), name='create')
    #本番環境には耐えられない既読機能
    #path('read/<int:pk>', readfunc, name='read')
]