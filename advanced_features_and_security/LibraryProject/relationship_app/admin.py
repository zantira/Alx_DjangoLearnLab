from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

# Register your models here.


class CustomUserAdmin(UserAdmin):
    # Fields to display in the user list view
    list_display = ('email', 'username', 'is_staff', 'is_superuser', 'is_active', 'profile_photo')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    # Enable search by email and username
    search_fields = ('email', 'username')
    ordering = ('email',)  # Order by email by default

    # Fieldsets for organizing fields in the user detail view
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username', 'profile_photo')}),
        (_('Permissions'), {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to display in the add user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )

# Register the custom user model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
