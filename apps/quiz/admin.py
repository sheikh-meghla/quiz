from django.contrib import admin
from .models import Quiz, Question, Result


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "quiz", "question_text", "correct_option")
    list_filter = ("quiz",)
    search_fields = ("question_text",)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "quiz", "score")
    list_filter = ("quiz", "user")