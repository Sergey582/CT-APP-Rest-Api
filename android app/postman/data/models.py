from django.db import models


class Test(models.Model):
    year = models.IntegerField(default=0)
    number = models.IntegerField()
    subject = models.CharField(max_length=250)


class Task(models.Model):
    part = models.CharField(max_length=250)
    number = models.IntegerField()
    task_text = models.TextField()
    test = models.ForeignKey('Test', related_name='tasks', on_delete=models.CASCADE)


class Answer(models.Model):
    answer_text = models.TextField()
    is_true = models.BooleanField(default=False)
    task = models.ForeignKey('Task', related_name='answers', on_delete=models.CASCADE)
