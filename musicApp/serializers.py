from rest_framework import serializers

from .models import *

from  rest_framework.serializers import ModelSerializer

class QoshiqchiSerializers(ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = "__all__"


class AlbomSerializers(ModelSerializer):
    class Meta:
        model = Albom
        fields = "__all__"

class QoshiqSerializers(ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = "__all__"
    def validated_audio(self, qiymat):
        if not  str(qiymat).endswith('.mp3'):
            raise serializers.ValidationError("Loyha faqat .mp3   faillar bilan  ishlashi mumkun!")
        return qiymat
    def validated_davomilik(self, qiymat):
        if str(qiymat) > "00:06:00":
            raise serializers.ValidationError("Qo'shiq davomiligi 6 daqiqadan oshmasligi kerak!")
        return qiymat


