from django.http import HttpResponse, HttpRequest, Http404
from polls.models import Question
from django.shortcuts import render


def index(request: HttpRequest):
    """polls アプリケーションのトップページを表示する"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        # template の変数名 : 対応する変数や値
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """question_id に対応する質問の詳細を見る"""
    try:
        # pk : primary key （主キー）の略
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    """question_id に対応する質問の結果を見る"""
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    """quesntion_id の質問に答える（vote: 投票する）"""
    return HttpResponse("You're voting on question %s." % question_id)
