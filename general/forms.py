from django import forms
from .models import Event, Match

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['match']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Если уже есть start_time (например, при редактировании), фильтруем матчи по этой дате
        if self.instance and self.instance.start_time:
            self.fields['match'].queryset = Match.objects.filter(date__gte=self.instance.start_time.date())
