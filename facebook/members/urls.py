from django.urls import path
from . import views

urlpatterns = [
    # this is the folder path
    path('members/', views.GetMembers, name='GetMembers'),
    path('members/', views.GetMemberByUserName, name='GetMemberByUserName')
]


