from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import Student


from .forms import StudentForm


def create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect("students:create")

            except IntegrityError:
                form.add_error("std_number", "This student number already exists.")
    else:
        form = StudentForm()

    return render(request, "create.html", {"form": form})


def get_all(request):
    students = Student.objects.all()

    context = {"students": students}

    return render(request, "students.html", context)


def test(request):
    print("Start")
    students = Student.objects.all()
    print("After all()")
    students = students.filter(age__gte=18)
    print("After filter()")
    students = students[0:3]
    print("After [0:3]")

    result = ""

    for student in students:
        result += student.name + ", "

    print("After for")

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
