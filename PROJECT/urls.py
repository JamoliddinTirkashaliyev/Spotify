
from django.contrib import admin
from django.urls import path, include
from musicApp.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("albomlar", AlbomModelViewSet)
router.register("qoshiqchilar", QoshiqchilarModelViewSet)
router.register("qoshiqlar", QoshiqlarModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    # path('qoshiqchilar/', QoshiqchilarAPI.as_view()),
    # path('qoshiqchilar/<int:pk>/', QoshiqchiAPI.as_view()),
    # path('qoshiqlar/', QoshiqlarAPI.as_view()),
]
