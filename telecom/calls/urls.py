from rest_framework.routers import DefaultRouter
from telecom.calls import views

app_name = "calls"

router = DefaultRouter()
router.register(r"records", views.CallRecordsViewSet, basename="records")
router.register(r"start", views.StartRecordViewSet, basename="start")
router.register(r"end", views.EndRecordViewSet, basename="end")

urlpatterns = router.urls
