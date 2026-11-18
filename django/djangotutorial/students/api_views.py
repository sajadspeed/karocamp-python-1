import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from .models import Student


def get_tmplate(request):
    return render(request, "students_api.html")


@csrf_exempt
def students(request):
    if request.method == "GET":
        students = Student.objects.all()

        data = {"students": []}

        for student in students:
            data["students"].append(
                {"name": student.name, "age": student.age, "phone": student.phone}
            )

        return HttpResponse(json.dumps(data))

    elif request.method == "POST":
        data = json.loads(request.body)

        Student.objects.create(name=data["name"], age=data["age"], phone=data["phone"])

        return HttpResponse("Student created successfully")
