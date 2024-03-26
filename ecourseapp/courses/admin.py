from .models import Course, Lesson, Tag, User, Rating, Comment, Category
from django.utils.safestring import mark_safe
from django.contrib import admin
from .form import CourseForm, LessonForm


class LessonInlineAdmin(admin.StackedInline):
    model = Lesson
    fk_name = 'course'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'category']
    list_filter = ['subject', 'created_date', 'category']
    search_fields = ['id', 'subject', 'category']
    readonly_fields = ['course_image']
    inlines = [LessonInlineAdmin, ]
    form = CourseForm

    def course_image(self, course):
        if course.image:
            return mark_safe(f"<img src='{course.image.url}' width='200px' />")


class LessonTagInlineAdmin(admin.TabularInline):
    model = Lesson.tags.through


class TagAdmin(admin.ModelAdmin):
    inlines = [LessonTagInlineAdmin, ]


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'course']
    list_filter = ['subject', 'created_date', 'course']
    search_fields = ['id', 'subject', 'course']
    readonly_fields = ['lesson_image']
    inlines = [LessonTagInlineAdmin, ]
    form = LessonForm

    def lesson_image(self, lesson):
        if lesson.image:
            return mark_safe(f"<img src='{lesson.image.url}' width='200px' />")


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Category)
