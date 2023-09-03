from django.urls import path

from fuw.views import StudentDetailView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('student-detail/<path:matric_number>/', StudentDetailView.as_view(), name='student-detail'),
]
