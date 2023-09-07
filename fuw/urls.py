from django.urls import path

from fuw.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
