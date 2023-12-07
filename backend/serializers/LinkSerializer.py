from backend.NModels.Link import Link
from rest_framework import serializers

class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ('id',)