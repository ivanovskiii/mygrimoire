from django.contrib import admin
from .models import Course, TarotCard


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("title",)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False


admin.site.register(Course, CourseAdmin)


class TarotCardAdmin(admin.ModelAdmin):
    list_display = ("name", "isMajorArcana")
    list_filter = ("name",)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False


admin.site.register(TarotCard, TarotCardAdmin)
