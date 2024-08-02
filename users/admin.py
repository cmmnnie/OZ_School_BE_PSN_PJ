# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User

# class UserAdmin(BaseUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         ('Important dates', {'fields': ('last_login',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('username', 'is_staff')
#     search_fields = ('username',)
#     ordering = ('username',)

# admin.site.register(User, UserAdmin)




from django.contrib import admin
from .models import User  # 커스텀 유저 모델
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # filter_horizontal = ('groups', 'user_permissions')
    filter_horizontal = []
admin.site.register(User, UserAdmin)
