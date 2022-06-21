from rest_framework.routers import DefaultRouter
from .views import NewsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='user')
urlpatterns = router.urls
