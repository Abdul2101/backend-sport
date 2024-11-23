from django.contrib import admin
from .models import Event, League, Match
from .forms import EventForm  # Импортируем форму

# admin.py

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventForm  # Подключаем кастомную форму с фильтрацией матчей
    list_display = ('match',)  # Отображаем только match и время события

    def event_start_time(self, obj):
        return obj.start_time()  # Время начала события, связанного с матчем
    event_start_time.short_description = 'Start Time'  # Заголовок для столбца

    def event_end_time(self, obj):
        return obj.end_time()  # Время окончания события
    event_end_time.short_description = 'End Time'  # Заголовок для столбца

    

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:  # Если редактируется существующее событие
            form.base_fields['match'].queryset = Match.objects.filter(date__gte=obj.match.date)
        return form


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport')
    list_filter = ('sport',)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'event', 'league', 'date')
    list_filter = ('league', 'event')

    def sport(self, obj):
        return obj.league.sport  # Получаем спорт через лигу

    def event(self, obj):
        return obj.event.title  # Отображаем название события

    sport.admin_order_field = 'league__sport'  # Для сортировки по виду спорта
    event.short_description = 'Event'  # Заголовок для события
