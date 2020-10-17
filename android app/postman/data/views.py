from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Test, Task
from .serializers import TaskSerializer, TestSerializer


class TestView(ListAPIView):
    # permission_classes = (IsAuthenticated,)  # <-- And here
    serializer_class = TaskSerializer

    def get_queryset(self):
        number = int(self.request.GET.get("number", 1))
        subject = self.request.GET.get("subject", 1)
        year = int(self.request.GET.get("year", 1))
        test = Test.objects.filter(number=number, year=year, subject=subject)[0]
        queryset = Task.objects.filter(test=test)
        # queryset = Task.objects.all()
        return queryset
