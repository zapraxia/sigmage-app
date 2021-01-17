from django.urls import path

from .views import QueryCreateView, QueryUpdateView

urlpatterns = [
    path('', QueryCreateView.as_view(), name='query-create'),
    path('<int:pk>/', QueryUpdateView.as_view(), name='query-update'),
]
