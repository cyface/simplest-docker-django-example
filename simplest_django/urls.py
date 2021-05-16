# Django URLs

from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html", extra_context={"magic": settings.MAGIC_MESSAGE})),
]
