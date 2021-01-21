from django.urls import path, include
from .views import Mobile_verification

urlpatterns = [
    path("<mobile>/", Mobile_verification.as_view(), name="Verification"),
]