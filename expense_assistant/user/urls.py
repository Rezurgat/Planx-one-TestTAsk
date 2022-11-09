from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter

from user.views import UserDataViewSet, SignView

router = DefaultRouter()
router.register('', UserDataViewSet, basename='user-info')

urlpatterns = [
    path('user/', include(router.urls)),

    path('auth/', UserViewSet.as_view({'post': 'create'}), name='auth'),
    path('sign/', SignView.as_view(), name='sign'),
]
