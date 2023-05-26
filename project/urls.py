from rest_framework import routers
from .api import ClientesViewSet

router = routers.DefaultRouter()

router.register("api/project", ClientesViewSet, "project")

urlpatterns = router.urls