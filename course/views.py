from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from product_course_mapping.models import ProductCourseMapping

from .models import Course
from .serializers import CourseSerializer


class CourseListCreateAPIView(APIView):

    def get(self, request):
        courses = Course.objects.all()
    
        product_id = request.query_params.get('product_id')
    
        if product_id:
            course_ids = ProductCourseMapping.objects.filter(
                product_id=product_id
            ).values_list('course_id', flat=True)
    
            courses = courses.filter(id__in=course_ids)
    
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):

        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CourseDetailAPIView(APIView):

    def get_object(self, pk):

        return get_object_or_404(Course, pk=pk)


    def get(self, request, pk):

        course = self.get_object(pk)

        serializer = CourseSerializer(course)

        return Response(serializer.data)


    def put(self, request, pk):

        course = self.get_object(pk)

        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):

        course = self.get_object(pk)

        serializer = CourseSerializer(course, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):

        course = self.get_object(pk)

        course.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)