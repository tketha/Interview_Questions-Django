from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .render import render_to_pdf
from .models import Questions
from .forms import QuestionForm
from django.contrib import messages
from django.views.generic import View


def add_ques(request):
    if request.POST:
        f = QuestionForm(request.POST)
        if f.is_valid():
            ques = f.save()
            messages.add_message(request, messages.INFO, 'Question saved.')
            return redirect('post')

    else:
        f = QuestionForm()

    return render(request, 'add_ques.html', {'form': f})


def ques_list(request):
    questions = Questions.objects.all()
    return render(request, 'list.html', {'questions': questions})


    from django.views.generic import View

    # importing get_template from loader
    from django.template.loader import get_template

    # import render_to_pdf from util.py

    # Creating our view, it is a class based view
class Pdf(View):
    def get(self, request, *args, **kwargs):
        # getting the template
        pdf = render_to_pdf('list.html')

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
