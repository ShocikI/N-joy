from backend.NModels.EventLink import EventLink
from rest_framework import serializers

class EventLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLink
        fields = ('id',)