
from django.contrib import admin
from django.urls import path
from app1.views import homepage,about,maqola,blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path("about/",about),
    path("blog/",blog),
    path("maqola/<int:son>",maqola,name='maqola'),

]
