from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RadioUser
# Register your models here.

class RadioUserAdmin(UserAdmin):
    # Add RadioUser fields to the admin view
    list_display = ('username', 'email', 'first_name', 'last_name', 'bio', 'birthday', 'profilePicture', 'is_staff')
    
    # Add / edit custom fields to the user creation and edit view
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
                    'bio', 'birthday', 'profilePicture' 
                ) 
            }
        ),
    )

    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
                    'bio', 'birthday', 'profilePicture' 
                ) 
            }
        ),
    )


admin.site.register(RadioUser, RadioUserAdmin)