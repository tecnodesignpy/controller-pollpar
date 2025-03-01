from django.db.models import Q
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from app.api.serializers import *
from ..models import *
from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import generics
# Create your views here.

		

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
 
from .permissions import IsStaffOrTargetUser


		


class UserPermissionsObj(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return obj == request.user
		
		
class MarcacioneViewSet(generics.ListAPIView):
    serializer_class = MarcacioneSerializer
    permission_classes=(IsAuthenticated,UserPermissionsObj)

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        usuario = str(self.kwargs['usuario'])
        usuario2 = str(self.request.user.id)
        usuariofinal = 0
        if usuario == usuario2:
            usuariofinal = usuario
        elif usuario2 == "AnonymousUser":
            usuariofinal = 0
        else:
            print("No son iguales")
        return Marcacione.objects.filter(usuario=usuariofinal).order_by('-id')
		
class MarcacionesViewSet(ModelViewSet):
    serializer_class = MarcacioneSerializer
    queryset = Marcacione.objects.all().order_by('-id')
    permission_classes=(IsAuthenticated,UserPermissionsObj)
		
class LastCheckViewSet(ModelViewSet):
    serializer_class = UltimaMarcacionSerializer
    queryset = Marcacione.objects.all().order_by('-id')
    permission_classes=(IsAuthenticated,UserPermissionsObj)
		
class UserView(ModelViewSet):
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()
 
    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),