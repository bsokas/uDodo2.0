from django.conf.urls import url

from . import views

app_name = "cheat_entry"

urlpatterns = [

    url(r'^$', views.home, name="Home"),
    url(r'^successful_post$', views.submission, name="successful_post")

]


#Used for defining urls

