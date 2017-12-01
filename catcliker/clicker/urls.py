from competition.views import ClickView
from django.conf.urls import url, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'click', ClickView.as_view())

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
