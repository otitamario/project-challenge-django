from rest_framework.routers import DefaultRouter
from api.views import ProjectViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'projects', ProjectViewSet)

urlpatterns = router.urls