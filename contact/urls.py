from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import ContactView

# api versioning
router = routers.DefaultRouter()
router.register(r'contact', ContactView, 'contact')
urlpatterns = [
    path("api/v1/", include(router.urls)), #this generate GET, POST, PUT, DELETE
    path("docs", include_docs_urls(title="Contact API"))
]