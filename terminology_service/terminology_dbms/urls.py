from django.urls import include, path
from rest_framework import routers
from terminology_service.terminology_dbms import views


router = routers.DefaultRouter()
router.register(r'directories', views.DirectoryViewSet)
router.register(r'items', views.DirectoryItemViewSet)


urlpatterns = [
    path('', views.info, name='info'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
