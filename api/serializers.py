from django.contrib.auth.models import User

from task.models import Task
from usergroup.models import UserGroup
from userprofile.models import UserProfile

from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'users', 'groups', 'time_estimate']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
    users = UserSerializer(source='userprofile_set')

    class Meta:
        model = UserGroup
        fields = ['name', 'users']

    # def get_user_profiles(self, obj):
    #     user_profiles = obj.userprofile_set.all()
    #     response = UserProfileSerializer(user_profiles, many=True).data
    #     return response


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    groups = UserGroupSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ['url', 'user', 'groups']
