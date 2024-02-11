from django.urls import path
from .views import *

urlpatterns = [
   path("say_hello/", say_hello),
   path("profile/", get_profile),
   path("filters/<int:query_id>/",filter_queries),
   path("queries/", QueryView.as_view())
]