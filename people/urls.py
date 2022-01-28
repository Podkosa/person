from rest_framework import routers
from .views import PeopleViewSet

router = routers.DefaultRouter()
router.register('people', PeopleViewSet)

urlpatterns = router.urls