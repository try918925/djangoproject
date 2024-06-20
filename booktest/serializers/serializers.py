from rest_framework import serializers
from ..models import Userinfo
import re



class UserinfoSerializer(serializers.ModelSerializer):

    def validate_phone_number(self, value):
        phone_regex = r'^1[3-9]\d{9}$'
        if not re.match(phone_regex, value):
            raise serializers.ValidationError("请输入有效的手机号")
        return value


    class Meta:
        model = Userinfo
        fields = "__all__"

