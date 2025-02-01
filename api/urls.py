from django.urls import path
from myapp  import views
from myapp.views import *

#from rest_framework_simplejwt.views import TokenObtainPairview

urlpatterns  = [

#url for Cleaner
path('Cleaner/',views.manage_Cleaner),
path('Cleaner/<int:id>',views.manage_Cleaner),
path('Cleaner_Login/', CleanerLoginView.as_view(), name='Cleaner_Login'),


#url for Task
path('Task/',views.manage_Task),
path('Task/<int:id>',views.manage_Task),

#admin
path('Admin_Login/', AdminLoginView.as_view(), name='Admin_Login'),


]