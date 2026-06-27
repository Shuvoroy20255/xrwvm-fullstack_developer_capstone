from rest_framework import serializers
from .models import CarMake, CarModel, Dealer, Review

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_user_name(self, obj):
        return obj.user.username