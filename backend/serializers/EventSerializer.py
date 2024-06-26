from backend.NModels.Event import Event
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id',)