from django.urls import path
from . import views

urlpatterns = [
    # get all members
    path('members/', views.GetMembers, name='GetMembers'),

    # get by username
    path('members/byusername/', views.GetMemberByUserName, name='GetMemberByUserName'),

    # add a new member
    path('members/add/', views.AddMember, name='AddMember')
    
]
