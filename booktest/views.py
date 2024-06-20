from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Userinfo
from .serializers.serializers import UserinfoSerializer


class UserinfoViewSet(viewsets.ModelViewSet):
    queryset = Userinfo.objects.all()
    serializer_class = UserinfoSerializer
    print(serializer_class)
    # permission_classes = [IsAuthenticated]

