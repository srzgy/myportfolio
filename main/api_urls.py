from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    # list and create
    path("educations/", api_views.education_list, name="education-list"),
    # detail, update, and delete
    path("educations/<uuid:education_id>/", api_views.education_detail, name="education-detail"),
    # toggle star
    path("educations/<uuid:education_id>/star/", api_views.education_star, name="education-star"),
]