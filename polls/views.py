from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . models import Questions
from django.shortcuts import render


# Create your views here.


def get(request):
    latest_questions = Questions.objects.order_by('-pub_date')[:5]

    context = {
        'latest_questions': latest_questions
    }
    return render(request, 'polls/index.html', context)

