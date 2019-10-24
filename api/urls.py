from django.urls import include, path
from rest_framework import routers
from . import views
from .views import TaskViewSet, UserGroupViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'usergroups', views.UserGroupViewSet)
router.register(r'userprofiles', views.UserProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
