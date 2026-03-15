from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer


class CourseCertificationMappingListCreateAPIView(APIView):

    def get(self, request):
        mappings = CourseCertificationMapping.objects.all()
        serializer = CourseCertificationMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCertificationMappingDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(CourseCertificationMapping, pk=pk)

    def get(self, request, pk):
        mapping = self.get_object(pk)
        serializer = CourseCertificationMappingSerializer(mapping)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        mapping = self.get_object(pk)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        mapping = self.get_object(pk)
        serializer = CourseCertificationMappingSerializer(
            mapping,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mapping = self.get_object(pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)