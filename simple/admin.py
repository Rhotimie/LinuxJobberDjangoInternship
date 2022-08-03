from django.contrib import admin
from .models import Article, Song, Album, GoalStatus, ScrumyGoals, ScrumyHistory

# Register your models here.

admin.site.register([Article, Song, Album, GoalStatus, ScrumyGoals, ScrumyHistory])
