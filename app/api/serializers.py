from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib import admin
from django.contrib.auth.models import User
from ..models import *
import rest_framework.serializers



class MarcacioneSerializer(ModelSerializer):
    class Meta:
        model = Marcacione
        fields = ('usuario','lugar','latitud','longitud','fecha','hora','observaciones','estado','device_id','zona')
		
class UltimaMarcacionSerializer(ModelSerializer):
    class Meta:
        model = Marcacione
        fields = ('usuario','estado','timestamp','fecha','hora')
		
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
 
    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user