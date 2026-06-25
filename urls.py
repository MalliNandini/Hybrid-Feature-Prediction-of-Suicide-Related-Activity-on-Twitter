from django.contrib import admin
from django.urls import path
from Remote_User import views as user
from Service_Provider import views as service

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', user.login, name='login'),
    path('Register1/', user.Register1, name='Register1'),
    path('Add_DataSet_Details/', user.Add_DataSet_Details, name='Add_DataSet_Details'),
    path('Search_TweetDataSets/', user.Search_TweetDataSets, name='Search_TweetDataSets'),
    path('ViewYourProfile/', user.ViewYourProfile, name='ViewYourProfile'),
    path('ratings/<int:pk>/', user.ratings, name='ratings'),

    path('serviceproviderlogin/', service.serviceproviderlogin, name='serviceproviderlogin'),
    path('View_Remote_Users/', service.View_Remote_Users, name='View_Remote_Users'),
    path('ViewTrendings/', service.ViewTrendings, name='ViewTrendings'),
    path('Search_Tweet/', service.Search_Tweet, name='Search_Tweet'),
    path('View_Suicide_Retweets/', service.View_Suicide_Retweets, name='View_Suicide_Retweets'),
    path('View_Positive_Retweets/', service.View_Positive_Retweets, name='View_Positive_Retweets'),
    path('View_Negative_Retweets/', service.View_Negative_Retweets, name='View_Negative_Retweets'),
    path('View_TweetDataSets_Details/', service.View_TweetDataSets_Details, name='View_TweetDataSets_Details'),
    path('View_Sentiment_Accuracy/', service.View_Sentiment_Accuracy, name='View_Sentiment_Accuracy'),
    path('charts/<str:chart_type>/', service.charts, name='charts'),
    path('negativechart/<str:chart_type>/', service.negativechart, name='negativechart'),
    path('likeschart/<str:like_chart>/', service.likeschart, name='likeschart'),
    path('viewtreandingquestions/<str:chart_type>/', service.viewtreandingquestions, name='viewtreandingquestions'),
]
