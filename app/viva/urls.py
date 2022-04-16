from django.urls import path
from .views import APIviews

urlpatterns = [
    path('stories/', APIviews.as_view(), name='stories'),
    path('stories/<int:idx>/<int:n_max>', APIviews.as_view(), name='stories'),
    path('stories/delete', APIviews.delete, name='delete'),
]
