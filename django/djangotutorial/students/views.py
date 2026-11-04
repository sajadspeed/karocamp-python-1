from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import Student


def create(request):
    try:
        student = Student(name="Ali")
        student.phone = "0913000212"
        student.std_number = "1234567"

        student.full_clean()
        student.save()

        return HttpResponse("One student add to DB.")
    except IntegrityError as e:
        return HttpResponse(e)
    except ValidationError as e:
        return HttpResponse(e)


def get_all(request):
    students = Student.objects.all()

    result = "<ul>"

    for student in students:
        result += f"<li>{student.std_number} -> {student.name}</li>"

    result += "</ul>"

    return HttpResponse(result)


def search(request):
    return render(request, "search.html")


def get(request):
    try:
        std_number_for_search = request.GET.get("std_number")

        student = Student.objects.get(std_number=std_number_for_search)
        
        result = "<ul>"

        result += f"<li>{student.std_number} -> {student.name}</li>"

        result += "</ul>"

        return HttpResponse(result)
    except Student.DoesNotExist as e:
        return HttpResponse("Not student found.", status=404)
