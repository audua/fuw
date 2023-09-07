from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView
from fuw.models import Student
from fuw.forms import StudentForm


class IndexView(FormView):
    template_name = 'fuw/index.html'
    form_class = StudentForm

    def form_valid(self, form):
        matric_number = form.cleaned_data['matric_number'].upper()
        context = self.get_context_data()
        context['matric_number'] = matric_number
        context['students'] = Student.objects.filter(matric_number=matric_number)
        return render(self.request, 'fuw/student.html', context)
