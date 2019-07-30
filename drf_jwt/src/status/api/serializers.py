from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from status.models import Status
from accounts.api.serializers import UserPublicSerializer

'''
Serializers -> JSON
Serializers -> validate data

'''


class StatusSerializer(serializers.ModelSerializer):

    user = UserPublicSerializer(read_only=True)
    userid = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    user_id = serializers.HyperlinkedRelatedField(
        source='user',  # user foreign key
        lookup_field='username',
        view_name='api-user:detail',
        read_only=True
    )
    email = serializers.SlugRelatedField(source='user', read_only=True, slug_field='email')
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'userid',
            'user_id',
            'email',
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
        request = self.context.get('request')
        return api_reverse('api-status:detail', kwargs={"id": obj.id}, request=request)

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data


class StatusInlineUserSerializer(StatusSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'content',
            'image'
        ]

    # def get_uri(self, obj):
    #     request = self.context.get('request')
    #     return api_reverse('api-status:detail', kwargs={"id": obj.id}, request=request)
