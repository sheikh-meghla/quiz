from django.contrib import admin
from .models import Quiz, Question, Result
from unfold.admin import ModelAdmin


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Quiz)
class QuizAdmin(ModelAdmin):
    list_display = ("id", "title")
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("id", "quiz", "question_text", "correct_option")
    list_filter = ("quiz",)
    search_fields = ("question_text",)


@admin.register(Result)
class ResultAdmin(ModelAdmin):
    list_display = ("id", "user", "quiz", "score")
    list_filter = ("quiz", "user")