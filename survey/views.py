import random
from uuid import UUID, uuid4

from django.shortcuts import redirect, render

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
    context = {
        "question_no": question_no,
        "question_text": question_text,
        "question_variant": question_variant,
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
    answer = models.SentimentAnswer(
        user_id=user_id,
        question_id=question_id,
        question_variant=question_variant,
        question_text=question_text,
        sentiment=sentiment,
    )
    answer.save()

    if question_no >= len(questions.QUESTIONS) * 2:
        return redirect("importance")

    request.session["question_no"] = question_no + 1
    request.session["prev_sentiment"] = sentiment
    return redirect("question")


def importance(request):
    topics = ["Pohodlí a zábava", "Ekonomický vývoj", "Vojenské konflikty"]
    random.shuffle(topics)
    user_id = request.session.get("user_id", None)
    if user_id is None:
        request.session["user_id"] = str(uuid4())

    context = {
        "topics": topics,
    }
    return render(request, "importance.html", context)


def submit_importance(request):
    user_id = UUID(request.session.get("user_id", None))

    for key in request.POST.keys():
        if key.startswith("csrf"):
            continue
        topic = key
        importance = int(request.POST[key])
        answer = models.ImportanceAnswer(
            user_id=user_id,
            topic=topic,
            importance=importance,
        )
        answer.save()
    return redirect("end")


def reset(request):
    request.session["question_no"] = 1
    request.session["prev_sentiment"] = 50
    request.session["user_id"] = str(uuid4())
    return redirect("question")


def end(request):
    request.session["question_no"] = 1
    request.session["prev_sentiment"] = 50
    request.session["user_id"] = str(uuid4())
    return render(request, "end.html")
