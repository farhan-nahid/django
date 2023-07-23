from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . models import Questions


# Create your views here.


def get(request):
    latest_questions = Questions.objects.order_by('-pub_date')[:5]
    output = ''
    for question in latest_questions:
        output += question.question_text + '\n'
        # output += f"Python{newline}Java{newline}Cpp"
    print(output)
    return HttpResponse(output)


