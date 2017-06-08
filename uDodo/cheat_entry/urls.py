from django.conf.urls import url

from . import views

app_name = 'cheat_entry'
urlpatterns = [

    #Initial url for entering a cheating entry
    url(r'^$', views.home, name="index"),

    #Simple HTML page that displays successful submission
    url(r'^successful_post$', views.submission, name="successful_post"),

]


#Used for defining urls

