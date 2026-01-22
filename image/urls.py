from django.urls import path
from .api_views import (
    ImageUploadView,
    ImageDetailView,
    ImageDeleteView
)
from .web_views import upload_page, list_page, view_page, delete_page

urlpatterns = [
    # HTML
    path("images/", upload_page,  name="image-upload"),
    path("images/list/", list_page, name="image-list"),
    path("image/<uuid:uuid>/", view_page, name="image-view"),
    path("image/<uuid:uuid>/delete/", delete_page, name="image-delete"),


    # API
    path("api/images/", ImageUploadView.as_view(), name="api-image-upload"),
    path("api/image/<uuid:uuid>/", ImageDetailView.as_view(), name="api-image-detail"),
    path("api/image/<uuid:uuid>/delete/", ImageDeleteView.as_view(), name="api-image-delete"),
]
