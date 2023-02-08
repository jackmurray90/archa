from django.contrib import admin
from django.urls import path, include
from archa.router import ArchaRouter
from archa.views import MeView, CardViewSet, AdminCardViewSet

router = ArchaRouter()
router.register('me', MeView, 'me')
router.register('cards', CardViewSet)
router.register('admin/cards', AdminCardViewSet, basename='admin-cards')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
