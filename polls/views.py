from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Questions


# Create your views here.


def get(request):
    latest_questions = Questions.objects.order_by('-pub_date')[:5]
    context = {
        'latest_questions': latest_questions
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    print(question)
    context = {
        'question': question
    }
    return render(request, 'polls/details.html', context)
