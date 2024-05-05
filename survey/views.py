from uuid import UUID, uuid4
from django.shortcuts import render, redirect
from . import questions
from . import models


def question(request):
    user_id = request.session.get("user_id", None)
    if user_id is None:
        request.session["user_id"] = str(uuid4())

    question_no = int(request.session.get("question_no", "1"))
    question = questions.QUESTIONS[(question_no - 1) // 2]
    if question_no % 2 == 1:
        question_text = question.get_empty()
        question_variant = -1
        sentiment = 50
    else:
        question_text, question_variant = question.get_random_filled()
        sentiment = int(request.session.get("prev_sentiment", 50))
    show_importance = question_no % 2 == 0
    context = {
        "question_no": question_no,
        "question_text": question_text,
        "question_variant": question_variant,
        "show_importance": show_importance,
        "sentiment": sentiment,
    }
    return render(request, "question.html", context)


def submit(request):
    user_id = UUID(request.session.get("user_id", None))
    question_no = int(request.session.get("question_no", "1"))
    question_id = (question_no - 1) // 2
    question = questions.QUESTIONS[question_id]
    question_variant = int(request.POST["variant"])
    if question_variant == -1:
        question_text = question.get_empty()
    else:
        question_text = question.filled_texts[question_variant]
    sentiment = int(request.POST["sentiment"])
    importance = int(request.POST.get("importance", "-1"))

    answer = models.SentimentAnswer(
        user_id=user_id,
        question_id=question_id,
        question_variant=question_variant,
        question_text=question_text,
        sentiment=sentiment,
        importance=importance,
    )
    answer.save()
    print(user_id, question_id, question_variant, question_text, sentiment, importance)

    request.session["question_no"] = question_no + 1
    request.session["prev_sentiment"] = sentiment
    return redirect("question")


def reset(request):
    request.session["question_no"] = 1
    request.session["prev_sentiment"] = 50
    request.session["user_id"] = str(uuid4())
    return redirect("question")
