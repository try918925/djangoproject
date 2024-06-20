from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from booktest.views import UserinfoViewSet


router = SimpleRouter()


router.register(r"", UserinfoViewSet)




urlpatterns = [
    # path('login/', ""),
    # path('exit/', ""),
]

urlpatterns += router.urls