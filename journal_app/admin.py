from django.contrib import admin
from django.urls import path
from .models import Posts

# Register your models here.

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.register(Posts)
