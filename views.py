from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Avg, Q
from Remote_User.models import (
    hybrid_feature_model,
    ClientRegister_Model,
    review_Model,
    recommend_Model,
    tweet_accuracy_model
)
import openpyxl


def serviceproviderlogin(request):
    if request.method == "POST":
        admin = request.POST.get("username")
        password = request.POST.get("password")

        if admin == "Admin" and password == "Admin":
            tweet_accuracy_model.objects.all().delete()
            return redirect("View_Remote_Users")

    return render(request, "SProvider/serviceproviderlogin.html")


def viewtreandingquestions(request, chart_type):
    dd = {}

    topic = hybrid_feature_model.objects.values("ratings").annotate(
        dcount=Count("ratings")
    ).order_by("-dcount")

    for t in topic:
        rating = t["ratings"]

        pos = 0
        neg = 0
        neu = 0

        pos_count = hybrid_feature_model.objects.filter(
            ratings=rating
        ).values("names").annotate(
            topiccount=Count("ratings")
        )

        for p in pos_count:
            if p["names"] == "positive":
                pos = p["topiccount"]
            elif p["names"] == "negative":
                neg = p["topiccount"]
            elif p["names"] == "neutral":
                neu = p["topiccount"]

        dd[rating] = [pos, neg, neu]

    return render(
        request,
        "SProvider/viewtreandingquestions.html",
        {
            "object": topic,
            "dd": dd,
            "chart_type": chart_type,
        },
    )


def Search_Tweet(request):
    if request.method == "POST":
        keyword = request.POST.get("keyword")

        obj = hybrid_feature_model.objects.filter(
            Q(tweet_desc__icontains=keyword) |
            Q(names__icontains=keyword)
        )

        return render(
            request,
            "SProvider/Search_Tweet.html",
            {"objs": obj},
        )

    return render(request, "SProvider/Search_Tweet.html")
  def View_Suicide_Retweets(request):
    sentiment = "Suicide"

    keywords = [
        "suicide", "death", "sorrow", "died", "die",
        "murder", "fear", "anxious", "bored",
        "alone", "hang", "hanged"
    ]

    query = Q()
    for word in keywords:
        query |= Q(retweet__icontains=word)

    obj = hybrid_feature_model.objects.filter(query)
    total = hybrid_feature_model.objects.count()

    accuracy = 0
    if total > 0:
        accuracy = obj.count() / total

    if accuracy != 0:
        tweet_accuracy_model.objects.create(
            names=sentiment,
            accuracy=accuracy
        )

    return render(
        request,
        "SProvider/View_Suicide_Retweets.html",
        {
            "objs": obj,
            "count": accuracy
        }
    )


def View_Positive_Retweets(request):
    sentiment = "Positive"

    keywords = [
        "good", "beautiful", "fantastic",
        "extraordinary", "best", "healthy",
        "happy", "marvel", "worth",
        "value", "amazing", "excellent"
    ]

    query = Q()
    for word in keywords:
        query |= Q(retweet__icontains=word)

    obj = hybrid_feature_model.objects.filter(query)
    total = hybrid_feature_model.objects.count()

    accuracy = 0
    if total > 0:
        accuracy = obj.count() / total

    if accuracy != 0:
        tweet_accuracy_model.objects.create(
            names=sentiment,
            accuracy=accuracy
        )

    return render(
        request,
        "SProvider/View_Positive_Retweets.html",
        {
            "objs": obj,
            "count": accuracy
        }
    )


def View_Negative_Retweets(request):
    sentiment = "Negative"

    keywords = [
        "bad", "worst", "heavy",
        "ridicules", "sad",
        "damn", "shameful", "failed"
    ]

    query = Q()
    for word in keywords:
        query |= Q(retweet__icontains=word)

    obj = hybrid_feature_model.objects.filter(query)
    total = hybrid_feature_model.objects.count()

    accuracy = 0
    if total > 0:
        accuracy = obj.count() / total

    if accuracy != 0:
        tweet_accuracy_model.objects.create(
            names=sentiment,
            accuracy=accuracy
        )

    return render(
        request,
        "SProvider/View_Negative_Retweets.html",
        {
            "objs": obj,
            "count": accuracy
        }
    )


def View_Remote_Users(request):
    obj = ClientRegister_Model.objects.all()

    return render(
        request,
        "SProvider/View_Remote_Users.html",
        {
            "objects": obj
        }
    )


def ViewTrendings(request):
    topic = hybrid_feature_model.objects.values(
        "topics"
    ).annotate(
        dcount=Count("topics")
    ).order_by("-dcount")

    return render(
        request,
        "SProvider/ViewTrendings.html",
        {
            "objects": topic
        }
    )
  def negativechart(request, chart_type):
    dd = {}

    topic = hybrid_feature_model.objects.values(
        "ratings"
    ).annotate(
        dcount=Count("ratings")
    ).order_by("-dcount")

    for t in topic:
        rating = t["ratings"]

        pos = 0
        neg = 0
        neu = 0

        result = hybrid_feature_model.objects.filter(
            ratings=rating
        ).values("names").annotate(
            topiccount=Count("ratings")
        )

        for r in result:
            if r["names"] == "positive":
                pos = r["topiccount"]
            elif r["names"] == "negative":
                neg = r["topiccount"]
            elif r["names"] == "neutral":
                neu = r["topiccount"]

        dd[rating] = [pos, neg, neu]

    return render(
        request,
        "SProvider/negativechart.html",
        {
            "object": topic,
            "dd": dd,
            "chart_type": chart_type,
        },
    )


def charts(request, chart_type):
    chart = tweet_accuracy_model.objects.values(
        "names"
    ).annotate(
        dcount=Avg("accuracy")
    )

    return render(
        request,
        "SProvider/charts.html",
        {
            "form": chart,
            "chart_type": chart_type,
        },
    )


def View_TweetDataSets_Details(request):
    obj = hybrid_feature_model.objects.all()

    return render(
        request,
        "SProvider/View_TweetDataSets_Details.html",
        {
            "list_objects": obj
        },
    )


def View_Sentiment_Accuracy(request):
    obj = tweet_accuracy_model.objects.all()

    return render(
        request,
        "SProvider/View_Sentiment_Accuracy.html",
        {
            "list_objects": obj
        },
    )


def likeschart(request, like_chart):
    charts = hybrid_feature_model.objects.values(
        "names"
    ).annotate(
        dcount=Avg("tweet_score")
    )

    return render(
        request,
        "SProvider/likeschart.html",
        {
            "form": charts,
            "like_chart": like_chart,
        },
    )
  from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
import openpyxl


def login(request):
    if request.method == "POST" and "submit1" in request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = ClientRegister_Model.objects.get(
                username=username,
                password=password
            )
            request.session["userid"] = user.id
            return redirect("Add_DataSet_Details")
        except ClientRegister_Model.DoesNotExist:
            pass

    return render(request, "RUser/login.html")


def Add_DataSet_Details(request):
    if request.method == "GET":
        return render(request, "RUser/Add_DataSet_Details.html")

    excel_file = request.FILES["excel_file"]

    wb = openpyxl.load_workbook(excel_file)
    sheet = wb.active

    hybrid_feature_model.objects.all().delete()
    tweet_accuracy_model.objects.all().delete()

    excel_data = []

    for row in sheet.iter_rows(values_only=True):
        excel_data.append(list(row))

        hybrid_feature_model.objects.create(
            names=row[0],
            creator=row[1],
            tweet_desc=row[2],
            tweet_loc=row[3],
            tweet_date=row[4],
            retweet=row[5],
            retweet_date=row[6],
            retweet_loc=row[7],
            tweet_score=row[8],
        )

    return render(
        request,
        "RUser/Add_DataSet_Details.html",
        {"excel_data": excel_data},
    )


def Register1(request):
    if request.method == "POST":
        ClientRegister_Model.objects.create(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            password=request.POST.get("password"),
            phoneno=request.POST.get("phoneno"),
            country=request.POST.get("country"),
            state=request.POST.get("state"),
            city=request.POST.get("city"),
        )

    return render(request, "RUser/Register1.html")


def ViewYourProfile(request):
    userid = request.session.get("userid")

    obj = get_object_or_404(
        ClientRegister_Model,
        id=userid
    )

    return render(
        request,
        "RUser/ViewYourProfile.html",
        {"object": obj},
    )


def Search_TweetDataSets(request):
    if request.method == "POST":
        keyword = request.POST.get("keyword")

        obj = hybrid_feature_model.objects.filter(
            Q(tweet_desc__icontains=keyword)
            | Q(names__icontains=keyword)
        )

        return render(
            request,
            "RUser/Search_TweetDataSets.html",
            {"objs": obj},
        )

    return render(request, "RUser/Search_TweetDataSets.html")


def ratings(request, pk):
    obj = get_object_or_404(
        hybrid_feature_model,
        id=pk
    )

    obj.ratings += 1
    obj.save(update_fields=["ratings"])

    return redirect("Add_DataSet_Details")
