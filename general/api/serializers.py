from rest_framework import serializers
from general.models import League, Match, Event

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'sport', 'name']


class MatchSerializers(serializers.ModelSerializer):
    league = LeagueSerializer

    class Meta:
        model = Match
        fields = ['id', 'date', 'time', 'league', 'event', 'location', 'team1', 'team2', 'status']


class EventSerializer(serializers.ModelSerializer):
    match = MatchSerializers()

    class Meta:
        model = Event
        fields = ['id', 'match', 'start_time']