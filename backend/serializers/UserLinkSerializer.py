from backend.NModels.UserLink import UserLink
from rest_framework import serializers

class UserLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLink
        fields = ('id',)