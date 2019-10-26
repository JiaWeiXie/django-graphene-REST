import rest_framework
from graphene_django.views import GraphQLView

from rest_framework.settings import api_settings
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes, parser_classes, throttle_classes
)
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt


class DRFGraphQLView(GraphQLView):
    def parse_body(self, request):
        if isinstance(request, rest_framework.request.Request):
            return request.data
        return super().parse_body(request)

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = permission_classes((IsAuthenticated,))(view)
        view = authentication_classes(api_settings.DEFAULT_AUTHENTICATION_CLASSES)(view)
        view = parser_classes(api_settings.DEFAULT_PARSER_CLASSES)(view)
        view = throttle_classes(api_settings.DEFAULT_THROTTLE_CLASSES)(view)
        view = api_view(["GET", "POST"])(view)
        view = csrf_exempt(view)
        return view
