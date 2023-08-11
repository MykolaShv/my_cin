from django.contrib import admin
from .models import Hall, Release, Session, Seat, Ticket


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    fields = ('name', 'rows', 'cols', 'photo')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    fields = ('movie', 'hall', 'start_date', 'end_date')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'



@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    fields = ('time_start',  'time_end' 'session', 'end_next_day', 'price')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    fields = ('hall', 'row', 'col')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    fields = ('spectator', 'session_timeframe', 'seat')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'
