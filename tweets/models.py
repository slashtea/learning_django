from django.db import models
from user_profile.models import User

# Create your models here.


class Tweet(models.Model):
    """
    Tweet model
    """

    user = models.ForeignKey(User)
    text = models.TextField(max_length=160)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    # Human_readable Formatting
    def __unicode__(self):
        return str(self.text) + ' - @' + str(self.user)


class Hashtag():
    """
    Hashtag Model
    """

    name = models.CharField(max_length=60, unique=True)
    tweet = models.ManyToManyField(Tweet)

    def __unicode__(self):
        return str(self.name)