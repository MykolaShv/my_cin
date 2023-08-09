from django.contrib import admin
from .models import Hall, Release, ScheduleDay, Session, Seat, Ticket


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    fields = ('name', 'rows', 'seats', 'photo')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    fields = ('movie', 'start_date', 'end_date')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(ScheduleDay)
class ScheduleDayAdmin(admin.ModelAdmin):
    fields = ('hall', 'day', 'start_at', 'release')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    fields = ('one_session', 'price')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    fields = ('session', 'row', 'seat')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    fields = ('spectator', 'amount', 'session', 'order', 'seat')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'
