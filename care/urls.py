from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PractitionerViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'practitioners', PractitionerViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = router.urls
