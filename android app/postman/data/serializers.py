from rest_framework import serializers
from .models import Task, Test, Answer
from django.forms.models import model_to_dict


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
        depth = 1


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["answer_text", "is_true"]
        depth = 2


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["part", "number", "task_text"]
        depth = 1

    def to_representation(self, instance):
        ret = super(TaskSerializer, self).to_representation(instance)
        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        answers = Answer.objects.filter(task=instance)
        list_answers = [model_to_dict(obj) for obj in answers]
        extra_ret = {'answers': list_answers}
        ret.update(extra_ret)
        return ret
