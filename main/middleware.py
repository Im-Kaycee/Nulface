from django.http import Http404

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is trying to access the admin page and is not an admin
        if request.path.startswith('/admin/') and not request.user.is_superuser:
            raise Http404("Page not found")
        response = self.get_response(request)
        return response
