from rest_framework.routers import DefaultRouter
from telecom.calls import views

app_name = "calls"

router = DefaultRouter()
router.register(r"records", views.call_records_view, basename="records")
router.register(r"start", views.start_records_view, basename="start")
router.register(r"end", views.end_records_view, basename="end")

urlpatterns = router.urls
