from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = 'You do not have Permission for thi Resource'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        
        return obj.user == request.user