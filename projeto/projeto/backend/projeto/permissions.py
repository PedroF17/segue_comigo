# core/permissions.py
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'administrador')

class IsCondutor(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user.utilizador, 'condutor')

class IsPassageiro(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user.utilizador, 'passageiro')
