from django.contrib import admin
from django.urls import path
from .models import Posts, Quotes


# Register your models here.

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.register(Posts)


@admin.register(Quotes)
class QuoteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'content'
    ]
