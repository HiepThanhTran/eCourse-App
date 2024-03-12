from .form import CourseForm
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Course, Lesson, Tag, User, Rating, Comment, Category


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'updated_date', 'active', 'category']
    list_filter = ['subject', 'created_date']
    search_fields = ['id', 'subject']
    readonly_fields = ['myimg']
    form = CourseForm

    def myimg(self, course):
        if course.image:
            return mark_safe(f"<img src='{course.image.url}' width='200px' />")


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Category)
