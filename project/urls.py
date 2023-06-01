from rest_framework import routers
from .api import ClientesViewSet
from .api import DepartmentsViewSet

router = routers.DefaultRouter()

router.register("api/project", ClientesViewSet, "project")
router.register('api/departments', DepartmentsViewSet,"departments")

urlpatterns = router.urls