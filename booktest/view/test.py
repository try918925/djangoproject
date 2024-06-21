from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from booktest.models import Userinfo
from booktest.serializers.serializers import UserinfoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from booktest.models import Userinfo
from booktest.serializers.serializers import UserinfoSerializer



class UserinfoViewSet(viewsets.ModelViewSet):
    get_personnel = Userinfo.objects.all()
    serializer_class = UserinfoSerializer

    def get_personnel(self, request, *args, **kwargs):
        pass


