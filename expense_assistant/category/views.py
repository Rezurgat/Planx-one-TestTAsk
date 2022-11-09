from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from category.serializers import CategorySerializer
from category.models import Category



class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Category.objects.filter(activity_status=True)

        return Category.objects.filter(user=self.request.user, activity_status=True)

