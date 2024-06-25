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

    @action(detail=False, methods=['POST'])
    def building_area(self, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        address = request.data.get('address')
        is_active = request.data.get('is_active')

        # 如果请求体中没有任何参数，则返回空数据响应
        if not first_name and not address and not is_active:
            return Response({"detail": "没有数据"})

        queryset = Userinfo.objects.all()

        # 根据传入的参数过滤数据集
        if first_name:
            queryset = queryset.filter(first_name=first_name)
        if queryset and address:
            queryset = queryset.filter(address=address)
        if queryset and isinstance(is_active,bool):  # 注意处理布尔类型的参数
            queryset = queryset.filter(is_active=is_active)


        # 只返回id和username字段
        if not queryset:
            return Response({"detail": "没有数据"})
        queryset = queryset.values("id", "username")
        return Response([data for data in queryset])
