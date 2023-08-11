from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'name', 'surname', 'email', 'phone', 'birth_date', 'ticket',
              'city',  'image', 'is_staff', 'is_superuser', 'is_active' )

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'

# Register your models here.
