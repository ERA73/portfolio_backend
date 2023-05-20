from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import ContactView

# api versioning
urlpatterns = [
    path('api/v1/contact/', ContactView.as_view(), name='contact'),
    # path("api/v1/", include(ContactView)), #this generate GET, POST, PUT, DELETE
    path("docs", include_docs_urls(title="Contact API"))
]