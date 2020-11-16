from rest_framework import serializers
from .models import Mode, Word


class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields = ('id', 'name', 'description', 'min_time_sec', 'max_time_sec')


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'name', 'weight', 'use', 'mode')