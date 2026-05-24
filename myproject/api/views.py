from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_students(request):

    if request.method == 'GET':

        students = Student.objects.all()

        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def student_detail(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'GET':

        serializer = StudentSerializer(student)

        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:

        serializer = StudentSerializer(
            student,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    elif request.method == 'DELETE':

        student.delete()

        return Response({
            "message": "Deleted successfully"
        })