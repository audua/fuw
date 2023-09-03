from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, FormView
from fuw.models import Student
from fuw.forms import StudentForm


class IndexView(FormView):
    template_name = 'fuw/index.html'
    form_class = StudentForm

    def form_valid(self, form):
        matric_number = form.cleaned_data['matric_number'].upper()
        self.success_url = reverse('fuw:student-detail', kwargs={'matric_number': matric_number})
        return super().form_valid(form)


class StudentDetailView(DetailView):

    model = Student
    template_name = 'fuw/student.html'
    context_object_name = 'student'
    slug_url_kwarg = "matric_number"
    slug_field = "matric_number"
