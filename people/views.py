from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from .models import People
from .serializers import PeopleSerializer

class PeopleViewSet(GenericViewSet, RetrieveModelMixin, CreateModelMixin):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer