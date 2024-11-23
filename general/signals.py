# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Match, Event
from datetime import datetime, timedelta

@receiver(post_save, sender=Match)
def create_event_for_match(sender, instance, created, **kwargs):
    if created and not instance.event:  # Если матч только что создан и не имеет события
        event = Event.objects.create(
            match=instance,  # Привязываем событие к матчу
            description=f"Матч {instance.team1} против {instance.team2}",
            start_time=datetime.combine(instance.date, instance.time),
            end_time=datetime.combine(instance.date, instance.time) + timedelta(hours=2)  # Пример продолжительности 2 часа
        )
        instance.event = event
        instance.save()  # Сохраняем матч с привязанным событием
