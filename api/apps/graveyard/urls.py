from .views import GraveyardViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', GraveyardViewSet)
urlpatterns = router.urls