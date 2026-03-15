from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from course_certification_mapping.models import CourseCertificationMapping

from .models import Certification
from .serializers import CertificationSerializer


class CertificationListCreateAPIView(APIView):

    def get(self, request):
        certifications = Certification.objects.all()
    
        course_id = request.query_params.get('course_id')
    
        if course_id:
            certification_ids = CourseCertificationMapping.objects.filter(
                course_id=course_id
            ).values_list('certification_id', flat=True)
    
            certifications = certifications.filter(id__in=certification_ids)
    
        serializer = CertificationSerializer(certifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):

        serializer = CertificationSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CertificationDetailAPIView(APIView):

    def get_object(self, pk):

        return get_object_or_404(Certification, pk=pk)


    def get(self, request, pk):

        certification = self.get_object(pk)
        serializer = CertificationSerializer(certification)

        return Response(serializer.data)


    def put(self, request, pk):

        certification = self.get_object(pk)
        serializer = CertificationSerializer(certification, data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):

        certification = self.get_object(pk)
        serializer = CertificationSerializer(
            certification,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):

        certification = self.get_object(pk)
        certification.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)