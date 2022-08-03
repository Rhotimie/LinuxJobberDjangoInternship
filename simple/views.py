from django.template import loader
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus
from django.http import Http404


# Create your views here.


# def index(request):
#     return HttpResponse("Hello, world")

# def index(request):
#     latest_goals_list = GoalStatus.objects.order_by('-status_name')
#     output = ', '.join([t.status_name for t in latest_goals_list])
#     return HttpResponse(output)


# def index(request):
#     latest_goals_list = GoalStatus.objects.order_by('-status_name')
#     template = loader.get_template('simple/index.html')
#     context = {"latest_goals_list": latest_goals_list}
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_goals_list = GoalStatus.objects.order_by('-status_name')
    context = {"latest_goals_lists": latest_goals_list}
    return render(request, 'simple/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the result for the question %s." % question_id)


def vote(request, question_id):
    response = "You're voting on question %s."
    return HttpResponse(response % question_id)


def mine(request, question_id):
    return HttpResponse("You're looking at my own {} views".format(question_id))

# def article_list(request):
#     return render(request, 'articles/article_list.html')
