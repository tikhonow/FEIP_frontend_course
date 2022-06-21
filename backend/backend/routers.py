from rest_framework.routers import SimpleRouter
from news.views import NewsViewSet


routes = SimpleRouter()
routes.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    *routes.urls
]
