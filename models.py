from django.db import models


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class hybrid_feature_model(models.Model):
    names = models.CharField(max_length=200)
    creator = models.CharField(max_length=200)
    tweet_desc = models.TextField()
    tweet_loc = models.CharField(max_length=200)
    tweet_date = models.CharField(max_length=100)
    retweet = models.TextField()
    retweet_date = models.CharField(max_length=100)
    retweet_loc = models.CharField(max_length=200)
    tweet_score = models.FloatField(default=0)
    ratings = models.IntegerField(default=0)
    topics = models.CharField(max_length=200, default="")
    
    def __str__(self):
        return self.names


class review_Model(models.Model):
    username = models.CharField(max_length=100)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class recommend_Model(models.Model):
    username = models.CharField(max_length=100)
    recommendation = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class tweet_accuracy_model(models.Model):
    names = models.CharField(max_length=100)
    accuracy = models.FloatField()

    def __str__(self):
        return self.names
