from rest_framework import serializers
from .models import Poll, Choice

# Choice Model Serializer.
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']

# Poll Model Serializer.
class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Poll
        fields = ['id', 'questions','choices' ,'pub_date', 'expiry_date']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices', [])
        poll = Poll.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(poll=poll, **choice_data)
        return poll