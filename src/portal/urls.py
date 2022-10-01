from django.urls import path
from portal import views


urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.loginUser,name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logoutUser,name='logout'),
    path('apply/<str:id>/', views.applyPage,name='apply'),
    path('post/', views.jobposting,name='posting'),

]