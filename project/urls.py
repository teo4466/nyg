from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register("api/project", ClientesViewSet, "project")
router.register('api/departments', DepartmentsViewSet,"departments")
router.register('api/empleados', EmpleadosViewSet,"empleados")
"""router.register('api/perfile', PerfilempleadoViewSet,"perfile")
router.register('api/accesoriose', AccesoriosempleadoViewSet,"accesoriose")
router.register('api/accesorioent', AccesorioentregadoViewset,"accesorioent")
router.register('api/habilitaciones', HabilitacionesempleadoViewSet,"habilitaciones")
router.register('api/capacitacion', CapacitacionViewSet,"capacitacion")
router.register('api/jornadas', JornadasViewSet,"jornadas")
router.register('api/visitas', VisitasViewSet,"visitas")
router.register('api/detvisitas', DetvisitasViewSet,"detvisitas")
router.register('api/camiones', CamionesViewSet,"camiones")
router.register('api/accesoriosc', AccessoriocamionViewSet,"accesoriosc")
router.register('api/checks', CheckcamionViewSet,"checks")
router.register('api/mantenimientoc', MantenimientocamionViewSet,"mantenimientoc")
router.register('api/service', ServicecamionViewset,"service")
router.register('api/cubiertas', CubiertasViewSet,"cubiertas")"""

urlpatterns = router.urls