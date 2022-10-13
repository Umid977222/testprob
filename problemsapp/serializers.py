from .models import Problems
from rest_framework import serializers


class ProblemSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Problems
        fields = ['id', 'product_model', 'img', 'description', 'add_bot_button', 'created_at']

