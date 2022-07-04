from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name="snippets"),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name="snippet_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)