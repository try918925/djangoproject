from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from booktest.models import Userinfo
from booktest.serializers.serializers import UserinfoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action


class UserinfoViewSet(viewsets.ModelViewSet):
    queryset = Userinfo.objects.all()
    serializer_class = UserinfoSerializer
    print(serializer_class)
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



    def get_personnel(self, request, *args, **kwargs):
        personnel_id = kwargs.get('personnel_id')
        if personnel_id and isinstance(personnel_id, int):
            try:
                userinfo = Userinfo.objects.get(id=personnel_id)  # 获取指定 id 的对象
                serializer = UserinfoSerializer(userinfo)  # 使用序列化器序列化单个对象
                return Response(serializer.data)
            except Userinfo.DoesNotExist:
                return Response({"message": "Userinfo not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Invalid personnel_id"}, status=status.HTTP_400_BAD_REQUEST)


