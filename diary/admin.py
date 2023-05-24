from django.contrib import admin
from .models import Diary
# Register your models here.

@admin.register(Diary)
class DiaryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'writer', 'description', 'created', 'edited')
    list_filter = ('created','edited' )