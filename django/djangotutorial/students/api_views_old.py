import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student


def get_tmplate(request):
    return render(request, "students_api.html")


from rest_framework.views import APIView
from rest_framework.response import Response


class StudentsView(APIView):
    def get(self, request):
        students = Student.objects.all()

        data = {"students": []}

        for student in students:
            data["students"].append(
                {"name": student.name, "age": student.age, "phone": student.phone}
            )

        return Response(data)

    def post(self, request):
        data = request.data

        Student.objects.create(name=data["name"], age=data["age"], phone=data["phone"])

        return Response({"message": "Student created successfully"}, status=201)
