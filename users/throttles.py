from rest_framework.throttling import SimpleRateThrottle

class AdminUserRateThrottle(SimpleRateThrottle):
    def allow_request(self, request, view):
        if request.user.is_staff:
            return True
        else:
            return super().allow_request(request, view)