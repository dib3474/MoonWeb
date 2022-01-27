from re import search
from django.contrib import admin
from .models import Question
from django.contrib import admin

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)