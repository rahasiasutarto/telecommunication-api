from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Telecom API")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", schema_view, name="docs"),
    path("calls/", include("telecom.calls.urls")),
    path("bills/", include("telecom.bills.urls")),
]
