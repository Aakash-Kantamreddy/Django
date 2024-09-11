from django.urls import path
from . views import Home,login,signup,About,contact,Team,Services

urlpatterns = [
    path('',Home,name="Home"),
    path('login',login,name="login"),
    path('signup',signup,name="signup"),
    path('About',About,name="About"),
    path('contact',contact,name="contact"),
    path('Team',Team,name="Team"),
    path('Services',Services,name="Services"),
    #  path('contact/', ContactForm, name='ContactForm'),
     
    

]
