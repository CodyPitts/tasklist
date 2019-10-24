from django.contrib.auth.models import User

from task.models import Task
from usergroup.models import UserGroup
from userprofile.models import UserProfile
from .serializers import TaskSerializer, UserSerializer, UserGroupSerializer, UserProfileSerializer

from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
