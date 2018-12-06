from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class JWTMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token is None:
            return
        jwt_auth = JSONWebTokenAuthentication()
        try:
            auth = jwt_auth.authenticate(request)
            request.user = auth[0]
        except Exception:
            return
        