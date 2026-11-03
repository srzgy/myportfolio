from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change education entries."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )

class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        
        # allows PUT/PATCH if the user has the specific change permission
        return (
            request.method in ("PUT", "PATCH")
            and request.user.has_perm("main.change_education")
        )
    
    