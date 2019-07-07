from django.contrib import admin
from django.urls import path

from adoptions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home, name='home'),
    path('adoptions/<int:id>', views.pet_detail, name='pet_detail'),
]
