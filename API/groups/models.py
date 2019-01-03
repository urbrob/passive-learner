from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    content = models.TextField()

    def __str__(self):
    	return self.content


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    true = models.BooleanField()


class QuestionSet(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)
    public = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
    	return self.name


class Copy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
    	return self.name


class Membership():
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ROLES = (
            (MEMBER, 'Member'),
            (MODERATOR, 'Moderator')
    )
    role = models.CharField(max_length=10, choices=ROLES)


class Categories(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    question_sets = models.ManyToManyField(QuestionSet)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

    def __str__(self):
    	return self.name
