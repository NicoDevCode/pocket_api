from rest_framework import serializers
from .models import Pocket, CurentSpend


class PocketSerializer(serializers.ModelSerializer):
    number_initial = serializers.ReadOnlyField(source='initial_amount')
    amount = serializers.ReadOnlyField(source='humanize_amount')
    spend_history = serializers.ReadOnlyField(source='spend_humanize')

    class Meta:
        model = Pocket
        fields = (
            'id',
            'name',
            'amount',
            'spend_history',
            'number_initial',
            'date_one',
            'date_two',
            'user'
        )


class CurentSpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurentSpend
        fields = (
            'id',
            'description',
            'amount',
            'register',
            'pocket'
        )
