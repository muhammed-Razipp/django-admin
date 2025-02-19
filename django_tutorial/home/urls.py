from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('home1/', views.home1, name='home1'),
    path('member/',views.member,name="member"),
    path('add/',views.add,name="add"),
    path('addrec/',views.addrec,name="addrec"),
    path('delete/<int:id>/',views.delete,name="delete_member"),
    path('member/update/<int:id>/',views.update,name="update"),
    path('member/update/uprec/<int:id>/',views.uprec,name="uprec"),
]
