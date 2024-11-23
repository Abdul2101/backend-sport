from django.db import models
from datetime import datetime

class Event(models.Model):
    match = models.ForeignKey('Match', on_delete=models.CASCADE, null=True, blank=True, related_name='events')
    
    def __str__(self):
        if self.match:
            return f"Событие для матча {self.match.team1} vs {self.match.team2}"
        return "Событие без привязанного матча"

    @property
    def start_time(self):
        if self.match:
            return datetime.combine(self.match.date, self.match.time)
        return None

class League(models.Model):
    SPORT_CHOICES = [
        ('Футбол', 'Футбол'),
        ('Хоккей', 'Хоккей'),
        ('Баскетбол', 'Баскетбол'),
        ('Волейбол', 'Волейбол'),
    ]
    sport = models.CharField(max_length=100, choices=SPORT_CHOICES)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.sport})"

class Match(models.Model):
    date = models.DateField()
    time = models.TimeField()
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='matches', null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='matches', null=True)
    location = models.CharField(max_length=200)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('предстоящий', 'Предстоящий'),
        ('идет', 'Идет'),
        ('завершен', 'Завершен')
    ])

    def __str__(self) -> str:
        return f"{self.team1} vs {self.team2} ({self.date})"
    
    def sport(self):
        return self.league.sport
