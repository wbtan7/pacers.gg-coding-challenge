from rest_framework import serializers

from Main.models import ScoreLog

class ScoreLogSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = ScoreLog
        fields = ["id", "username", "score"]