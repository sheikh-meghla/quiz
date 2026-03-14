from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("name","email", "is_staff", "is_active",)
    list_filter = ("name","email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("name")}),
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )

    search_fields = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)