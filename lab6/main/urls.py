from django.urls import path

from main.views import albums
from main.views import authors

urlpatterns = [
    path('', authors),
    path('albums/<int:author_id>', albums),
]