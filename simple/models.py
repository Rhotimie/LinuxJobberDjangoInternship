from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
Each class represent a table in the database
A model is used to create or manipulate instance of records in the database
ORM bridges the gap between the models and the database
ORM is used to interact with the database
    --save instance of the models
    --retrieve model from the database
    --update a model
The command below can be used to create interactive console shell to interact with the database from the shell
--python manage.py shell
--ctrl z: will exit the shell
To import a model use
--from simple.models import Article
call Article type with
--Article
To retrieve every objects in the article table from the database
--Article.objects.all()
To create an object Instance, use
--article = Article()
--article1 = Article(title='django')
--article2 = Article(title='test', slug='test-sample', body='test sample is here')

--from rhotimie3421scrumy.models import User, GoalStatus, ScrumyGoals, ScrumyHistory
--ScrumyGoals.objects.create(goal_name= "Learn Django", goal_id=1, created_by="Louis", moved_by="Louis", owner="Louis", goal_status=wg, user=user1)
--ScrumyGoals.objects.filter(id=3)
--ScrumyGoals.objects.filter(goal_name__startswith ="Learn Django")
--GoalStatus.objects.exclude(status_name__startswith ="Daily Goal")

--sg = Article.objects.create(title='test', slug='test-sample', body='test sample is here')
--
--article.title = "hello world"
To update an object Instance, use
--article.title = "I am here"
To delete an object Instance, use
--article1.delete()
call article type with
--article
call the command below to retrieve the data inserted into the article.title
--article.title
To save the article object record created into the database use
--article.save()
use the command below to retrieve every objects in the article table from the database
--Article.objects.all()
retrieve the first row
--Article.objects.all()[0]
--Article.objects.all()[0].title
retrieve a row with it's primary key
--Article.objects.get(pk=1)
"""


class MySimpleModel(models.Model):
    col = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    dates = models.DateTimeField(auto_now_add=True)

    # to return object attributes, instead of Article object whenever Article is referenced use the method below,

    def __str__(self):
        return self.title


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    genre = models.CharField(max_length=250)

    def __str__(self):
        return self.file_type


class GoalStatus(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name


class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=300)
    goal_id = models.IntegerField(serialize=True)
    created_by = models.CharField(max_length=300)
    moved_by = models.CharField(max_length=300)
    owner = models.CharField(max_length=300)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.goal_name


class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=300)
    created_by = models.CharField(max_length=300)
    moved_from = models.CharField(max_length=300)
    moved_to = models.CharField(max_length=300)
    time_of_action = models.DateTimeField()
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.moved_by, self.created_by)

