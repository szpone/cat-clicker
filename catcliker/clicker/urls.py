from clicker.views import ClickViewSet
from django.conf.urls import url, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'click', ClickViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
