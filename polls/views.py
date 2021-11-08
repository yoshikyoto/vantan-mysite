from django.http import HttpResponse, HttpRequest
from polls.models import Question
from django.template import loader


def index(request: HttpRequest):
    """polls アプリケーションのトップページを表示する"""
    # latest_question_list は Question オブジェクトの配列になっている
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # [q.question_text for q in latest_question_list] → question_text の配列になる
    output = '<br>'.join([q.question_text for q in latest_question_list])

    # 後置 for を、後置じゃない形式に直した場合
    a = []
    for q in latest_question_list:
        a.append(q.question_text)

    # joinの部分は、 ', '.join(strの配列)　とすると、配列の中身をカンマで結合する
    a = ["a", "b", "c"]
    joined = '/'.join(a)
    # joined = "a/b/c"

    return HttpResponse(output)


def detail(request, question_id):
    """question_id に対応する質問の詳細を見る"""
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    """question_id に対応する質問の結果を見る"""
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    """quesntion_id の質問に答える（vote: 投票する）"""
    return HttpResponse("You're voting on question %s." % question_id)
