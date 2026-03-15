from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer


class VendorProductMappingListCreateAPIView(APIView):

    def get(self, request):
        mappings = VendorProductMapping.objects.all()
        serializer = VendorProductMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VendorProductMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorProductMappingDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(VendorProductMapping, pk=pk)

    def get(self, request, pk):
        mapping = self.get_object(pk)
        serializer = VendorProductMappingSerializer(mapping)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        mapping = self.get_object(pk)
        serializer = VendorProductMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        mapping = self.get_object(pk)
        serializer = VendorProductMappingSerializer(
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