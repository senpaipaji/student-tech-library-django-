from django.urls import path
from . import views


urlpatterns = [
    
    path('login/' , views.loginUser , name='login'),
    path('register/' , views.registerUser , name='register'),
    path('logout/' , views.logoutUser , name='logout'),
    
    path('' , views.home , name='home'),
    path('library/home',views.libraryhome,name='library'),
    path('library/<base>/<branch>/<sem>',views.libraryOut, name='libraryOut'),
    path('contact',views.contact,name='contact'),
    path('courses/home',views.courses,name="courses"),
    path('courses/insert',views.createVideo,name="insert")
    
]
