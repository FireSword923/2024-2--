from django.shortcuts import render
from questions.models import Question

def question_detail(request, question_id):
    question = Question.objects.get(id = question_id)
    context = {'question' : question}
    return render(request, 'index.html', context)

def question_list(request):
    questions = Question.objects.all()
    context = {'questions' : questions}
    return render(request, 'question_list.html', context)