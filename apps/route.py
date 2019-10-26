from rest_framework import routers

from .account.views import UserViewSet, GroupViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urls = router.urls
