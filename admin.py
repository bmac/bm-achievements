from django.contrib import admin
from cowpuncher.achievements.models import Achievement 

class AchievementAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Achievement, AchievementAdmin)
