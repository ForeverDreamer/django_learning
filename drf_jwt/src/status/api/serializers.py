from rest_framework import serializers

from status.models import Status
from accounts.api.serializers import UserPublicSerializer

'''
Serializers -> JSON
Serializers -> validate data

'''


class StatusSerializer(serializers.ModelSerializer):

    user = UserPublicSerializer(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'uri'
        ]
        read_only_fields = ['user']  # GET

    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is wayy too long.")
    #     return value

    def get_uri(self, obj):
        return "/api/status/{id}/".format(id=obj.id)

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data
