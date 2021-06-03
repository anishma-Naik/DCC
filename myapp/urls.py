from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    #path('', views.home, name="home"),

	path('', views.home, name='home'),
    path('beaches/', views.beaches, name='catalog-beaches'),
    path('hillstations/', views.hillstations, name='catalog-hillstations'),
    path('heritage_sites/', views.heritagesites, name='catalog-heritagesites'),
    


]