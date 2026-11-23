from django.shortcuts import render
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


def get_tmplate(request):
    return render(request, "students_api.html")


from rest_framework.views import APIView
from rest_framework.response import Response


class StudentsView(APIView):
    def get(self, request):
        students = Student.objects.all()

        serializer = StudentSerializer(students, many=True)

        return Response({"students": serializer.data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Student created successfully"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)